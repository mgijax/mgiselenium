"""
Functions for iterating over selenium WebDriverElements
"""

def getTextAsList(elements):
    """
    Return convert a list of elements into
        a list of their text attributes
    """
    
    textItems = []
    for element in elements:
        textItems.append(element.text)
        
    return textItems