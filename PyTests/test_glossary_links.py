"""
Created on September 29, 2025
Tests all links on the glossary page 2 levels deep.
Internal links: http/https, no failure on 404 (soft-404s logged)
External links: must use HTTPS, fail on HTTP status >=400 or soft-404 keywords
Ignored domain: bhmgiapp14ld.jax.org
Opens each link in a new tab and closes afterward
Verbose console logging with [Level 1] and [Level 2]
@author: jeffc
"""

import unittest
from urllib.parse import urlparse, urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import config


class TestGlossaryLinks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up WebDriver
        browser = getattr(config, "BROWSER", "chrome").lower()
        if browser == "chrome":
            cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            cls.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        cls.driver.set_window_size(1500, 1000)
        cls.base_url = "http://scrum.informatics.jax.org/glossary"
        cls.driver.get(cls.base_url)

        # Domains
        cls.internal_domain = "scrum.informatics.jax.org"
        cls.ignored_domain = "bhmgiapp14ld.jax.org"

        # Soft 404 indicators (external links only)
        cls.soft_404_indicators = [
            "not found", "page not found", "404", "does not exist",
            "unavailable", "missing", "cannot be"
        ]

        # Requests headers for status checks
        cls.request_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def extract_links(self, base=None):
        """
        Extract all valid hrefs from the current page.
        If base is provided, resolve relative URLs against base; otherwise use current driver URL.
        """
        links = []
        if base is None:
            base = self.driver.current_url
        anchors = self.driver.find_elements(By.TAG_NAME, "a")
        for a in anchors:
            href = a.get_attribute("href")
            if not href or href.startswith(("javascript:", "#", "mailto:")):
                continue
            # Resolve relative links against the provided base
            resolved = urljoin(base, href)

            # Skip ignored domain
            parsed = urlparse(resolved)
            if str(parsed.netloc) == self.ignored_domain:
                print(f"  SKIP (ignored domain): {resolved}")
                continue

            # Skip PowerPoint files
            if resolved.lower().endswith((".ppt", ".pptx")):
                print(f"  SKIP (PowerPoint file): {resolved}")
                continue

            links.append(resolved)
        return links

    def safe_is_internal(self, parsed):
        return str(parsed.netloc).endswith(self.internal_domain)

    def check_external_status(self, href):
        """
        Check HTTP status for external link using requests.
        Returns (ok:bool, status_or_error)
        """
        try:
            # HEAD first for speed, but some servers respond oddly; use GET fallback
            resp = requests.head(href, allow_redirects=True, timeout=10, headers=self.request_headers)
            if resp.status_code >= 400 or resp.status_code == 405:
                resp = requests.get(href, allow_redirects=True, timeout=10, headers=self.request_headers)
            return (resp.status_code < 400, resp.status_code)
        except Exception as e:
            return (False, str(e))

    def visit_links(self, links, depth=1, visited=None, parent_window=None, level_label="Level 1"):
        """
        Visit links recursively up to depth.
        - links: list of absolute URLs to visit
        - depth: integer; when depth==1, we will recurse one more level for internal pages
        - visited: set of URLs already processed
        - parent_window: handle to switch back to after closing child tabs
        - level_label: textual label for logging ("Level 1" or "Level 2")
        Returns (invalid_links, non_https_links)
        """
        if visited is None:
            visited = set()
        if parent_window is None:
            parent_window = self.driver.current_window_handle

        invalid_links = []
        non_https_links = []

        for href in links:
            if href in visited:
                print(f"[{level_label}] SKIP (already visited): {href}")
                continue
            visited.add(href)

            parsed = urlparse(href)
            is_internal = self.safe_is_internal(parsed)

            if is_internal:
                print(f"[{level_label}][INTERNAL] Visiting: {href}")
            else:
                print(f"[{level_label}][EXTERNAL] Visiting: {href}")

            # External non-HTTPS -> warn and record
            if not is_internal and parsed.scheme != "https":
                print(f"[{level_label}][WARNING] External non-HTTPS skipped: {href}")
                non_https_links.append(href)
                continue

            # Before opening, for external links we can do a status check via requests
            if not is_internal:
                ok, status = self.check_external_status(href)
                if not ok:
                    print(f"[{level_label}][INVALID] External link status failure: {href} -> {status}")
                    invalid_links.append((href, status))
                    continue
                else:
                    print(f"[{level_label}][INFO] External link HTTP OK: {href} -> {status}")

            # Open link in new tab
            try:
                self.driver.execute_script("window.open(arguments[0]);", href)
                # switch to new tab
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(2)  # allow page to load
            except Exception as e:
                print(f"[{level_label}][ERROR] Failed to open tab for {href}: {e}")
                invalid_links.append((href, str(e)))
                # try to ensure we are back to parent
                try:
                    self.driver.switch_to.window(parent_window)
                except Exception:
                    pass
                continue

            # inspect rendered page
            try:
                new_url = self.driver.current_url
                new_parsed = urlparse(new_url)
                new_is_internal = self.safe_is_internal(new_parsed)
            except Exception as e:
                print(f"[{level_label}][ERROR] Could not read current_url for {href}: {e}")
                new_is_internal = False

            # For external pages: check soft-404 keywords in page source/title
            if not new_is_internal:
                try:
                    page_source = self.driver.page_source.lower()
                except Exception as e:
                    page_source = ""
                    print(f"[{level_label}][WARN] Could not get page_source for {href}: {e}")

                try:
                    title = (self.driver.title or "").lower()
                except Exception:
                    title = ""

                found_soft_404 = any(k in page_source for k in self.soft_404_indicators) or \
                                 any(k in title for k in self.soft_404_indicators) or \
                                 any(p in new_url.lower() for p in ["404", "notfound", "error", "missing"])

                if found_soft_404:
                    print(f"[{level_label}][INVALID - Soft 404] {href}")
                    invalid_links.append((href, "Soft 404"))
                else:
                    print(f"[{level_label}][VALID] External link appears valid: {href}")

            else:
                # Internal pages: if soft-404-like content exists, log but DO NOT fail
                try:
                    page_source = self.driver.page_source.lower()
                    title = (self.driver.title or "").lower()
                    found_soft_404_internal = any(k in page_source for k in self.soft_404_indicators) or \
                                              any(k in title for k in self.soft_404_indicators) or \
                                              any(p in new_url.lower() for p in ["404", "notfound", "error", "missing"])
                    if found_soft_404_internal:
                        print(f"[{level_label}][INTERNAL - LOG Soft 404] {href}")
                    else:
                        print(f"[{level_label}][INTERNAL] Page loaded OK: {href}")
                except Exception as e:
                    print(f"[{level_label}][INTERNAL][WARN] Could not inspect internal page {href}: {e}")

            # Recurse one more level for internal links (only when depth == 1)
            if depth == 1 and new_is_internal:
                # extract links from the current page; resolve relative URLs against current page URL
                try:
                    sub_links = self.extract_links(base=self.driver.current_url)
                    print(f"[{level_label}] Found {len(sub_links)} links on {href} (to be processed at Level 2)")
                except Exception as e:
                    sub_links = []
                    print(f"[{level_label}][WARN] Failed to extract links on {href}: {e}")

                if sub_links:
                    # recurse with depth 0 and Level 2 label, pass current tab as parent_window
                    sub_invalid, sub_non_https = self.visit_links(
                        sub_links,
                        depth=0,
                        visited=visited,
                        parent_window=self.driver.current_window_handle,
                        level_label="Level 2"
                    )
                    invalid_links.extend(sub_invalid)
                    non_https_links.extend(sub_non_https)

            # Close this tab and return to parent window
            try:
                self.driver.close()
            except Exception as e:
                print(f"[{level_label}][WARN] Error closing tab for {href}: {e}")
            try:
                self.driver.switch_to.window(parent_window)
            except Exception as e:
                print(f"[{level_label}][ERROR] Could not switch back to parent window after {href}: {e}")
                # Attempt to recover: if there are windows, switch to the first
                try:
                    if self.driver.window_handles:
                        self.driver.switch_to.window(self.driver.window_handles[0])
                except Exception:
                    pass

        return invalid_links, non_https_links

    def test_links_recursive_two_levels(self):
        print("[Level 1] Starting crawl at:", self.base_url)
        level1_links = self.extract_links(base=self.base_url)
        print(f"[Level 1] Found {len(level1_links)} links on the start page")
        invalid_links, non_https_links = self.visit_links(level1_links, depth=1, visited=set(), parent_window=self.driver.current_window_handle, level_label="Level 1")

        # Summary
        print("\n=== SUMMARY ===")
        if invalid_links:
            print("Invalid links (will fail test):")
            for u, e in invalid_links:
                print(f" - {u} -> {e}")
        else:
            print("No invalid external links found.")

        if non_https_links:
            print("\nExternal links not using HTTPS (will fail test):")
            for u in non_https_links:
                print(f" - {u}")
        else:
            print("No external non-HTTPS links found.")

        # Fail the test if any invalid or non-HTTPS external links were found
        if invalid_links:
            self.fail("Invalid links found:\n" + "\n".join([f"{u} -> {e}" for u, e in invalid_links]))
        if non_https_links:
            self.fail("External links not using HTTPS:\n" + "\n".join(non_https_links))


if __name__ == "__main__":
    unittest.main()