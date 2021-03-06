This is a tool for running browser-driven automated tests using selenium against MGI webapps.

# Requirements
These must all be installed locally

 * python 2.7
 * up to date python selenium module

    Run either
    ``pip install --upgrade selenium``
    
    or
    ``easy_install --upgrade selenium``
 * geckodriver on system PATH (when running Firefox tests)
 
    Download latest geckodriver here:
    [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
    Ensure directory where geckodriver/geckodriver.exe file is on your system PATH.
 * chromedriver on system PATH (when running Chrome tests)
 
    Download latest chromedriver here:
    [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    Ensure directory where chromedriver/chromedriver.exe file is on your system PATH.
    
 * You must create a config/config.py file.

    Use config.py.default as a template
    ``cp config.py.default config.py``


# Usage
See [Selenium Docs](http://selenium-python.readthedocs.org/index.html) for help with the selenium library.


## Running Tests
Tests can be run either in Eclipse (with PyDev) or via command line.

### Command Line
Some examples

1. Run all tests in a directory

    	# all_tests.py is our convention for master test suites
    	python all_tests.py

2. single test suite
    
    	python searchtest.py
    
3. single test Class

	    # SearchTest is the name of a unittest.TestCase class
	    python searchtest.py SearchTest
    
4. single test method
    
    	python searchtest.py SearchTest.testBasicSearch
    
