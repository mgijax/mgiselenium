"""
Functions for iterating over selenium WebDriverElements
"""
import json

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

    return json.loads(driver.find_element_by_tag_name("pre").text);
