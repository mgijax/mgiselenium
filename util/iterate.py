"""
Functions for iterating over selenium WebDriverElements
"""
import json
from selenium.webdriver.common.by import By

def getTextAsList(elements):
    """
    Return convert a list of elements into
        a list of their text attributes
    """
    
    textItems = []
    for element in elements:
        textItems.append(element.text)
        
    return textItems


def getJsonData(driver):

    return json.loads(driver.find_element_by_tag_name(By.TAG_NAME, "pre").text);
