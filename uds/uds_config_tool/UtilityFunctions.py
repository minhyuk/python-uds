"""
This script contains utility functions for extracting and processing information from XML elements.
"""

def getSdgsData(diagServiceElement):
    """
    Retrieves the SDGS data elements from a diagnostic service element.

    Args:
    diagServiceElement: a diagnostic service element

    Returns:
    A dictionary with the SDGS data elements
    """

def getSdgsDataItem(diagServiceElement, itemName):
    """
    Gets a specific entry from the SDGS params, given a diagnostic service element and an item name.

    Args:
    diagServiceElement: a diagnostic service element
    itemName: a string representing the SI attribute

    Returns:
    A specific entry from the SDGS params, or None if it does not exist
    """

def getShortName(xmlElement):
    """
    Retrieves the short name from an XML element.

    Args:
    xmlElement: an XML element

    Returns:
    A string with the short name, or None if no short name exists
    """

def getLongName(xmlElement):
    """
    Retrieves the long name from an XML element.

    Args:
    xmlElement: an XML element

    Returns:
    A string with the long name, or None if no long name exists
    """

def getServiceIdFromDiagService(diagServiceElement, xmlElements):
    """
    Obtains the service ID from a diagnostic service element.

    Args:
    diagServiceElement: a diagnostic service element
    xmlElements: a list of other XML elements

    Returns:
    An integer representing the service ID
    """

def getResponseIdFromDiagService(diagServiceElement, xmlElements):
    """
    Gets the response ID from a diagnostic service element.

    Args:
    diagServiceElement: a diagnostic service element
    xmlElements: a list of other XML elements

    Returns:
    An integer representing the response ID
    """

def getParamWithSemantic(xmlElement, semanticName):
    """
    Retrieves a parameter matching the semantic from an XML element.

    Args:
    xmlElement: an XML element
    semanticName: the name of a semantic to match

    Returns:
    A single parameter matching the semantic, or a list of parameters which match the semantic
    """

def getPositiveResponse(diagServiceElement, xmlElements):
    """
    Extracts the positive response elements related to a diagnostic service element.

    Args:
    diagServiceElement: a diagnostic service element
    xmlElements: the dictionary of all possible XML elements

    Returns:
    If only 1 element, then a single XML element, else a list of XML elements, or None if no positive responses
    """

def getDiagObjectProp(paramElement, xmlElements):
    """
    Retrieves the diagnostic object property from an XML element.

    Args:
    paramElement: an XML element
    xmlElements: the dictionary of all possible XML elements

    Returns:
    The diagnostic object property element
    """

def getBitLengthFromDop(diagObjectPropElement):
    """
    Gets the bit length from a diagnostic object property element.

    Args:
    diagObjectPropElement: a diagnostic object property element

    Returns:
    The bit length
    """

def isDiagServiceTransmissionOnly(diagServiceElement):
    """
    Checks if the diagnostic service transmission is only.

    Args:
    diagServiceElement: a diagnostic service element

    Returns:
    Boolean indicating whether the diagnostic service transmission is only
    """
