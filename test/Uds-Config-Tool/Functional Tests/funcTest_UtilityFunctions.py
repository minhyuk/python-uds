"""
The script is focused on parsing and extracting information from an ODX (Open Diagnostic Data Exchange) file "Bootloader.odx" to understand the diagnostic services and their attributes defined within the file.

Key Functionalities:

1. Imports:
    - Importing utility functions to extract specific data attributes from the ODX file.

2. ODX Parsing and Data Extraction:
    - Using ElementTree to parse the ODX file and extract the necessary information into a dictionary "xmlElements".
  
3. Iterating Over Diagnostic Services:
    - For each DIAG-SERVICE tag in the ODX file:
        - Extracting Short Name, Long Name, SDGS parameters, Service Id, DiagInstanceName, and Positive Responses related to the service.
        - Printing the extracted information for analysis.
  
4. Data Extraction Functions:
    - Utilizing various utility functions to retrieve specific parameter data associated with a diagnostic service from the ODX file.
  
5. Output:
    - Displaying the extracted details such as Short Name, Long Name, SDGS parameters, Service Id, DiagInstanceName, and Positive Responses for each diagnostic service present in the ODX file.

Overall, the script provides a structured approach to read and extract diagnostic service information from the provided ODX file "Bootloader.odx", offering insights into the characteristics and attributes of each service defined within the diagnostic tool.
"""

from uds.uds_config_tool.UtilityFunctions import getSdgsDataItem, getParamWithSemantic, getServiceIdFromDiagService, \
                                                 getLongName, getShortName, getSdgsData, getPositiveResponse

if __name__ == "__main__":
    import xml.etree.ElementTree as ET

    filename = "Bootloader.odx"

    root = ET.parse(filename)

    xmlElements = {}

    for child in root.iter():
        currTag = child.tag
        try:
            xmlElements[child.attrib['ID']] = child
        except KeyError:
            pass

    for key, value in xmlElements.items():
        if value.tag == 'DIAG-SERVICE':
            print(value)
            shortName = getShortName(value)
            longName = getLongName(value)
            sdgsParams = getSdgsData(value)
            print("Short Name: {0}".format(shortName))
            print("Long Name: {0}".format(longName))
            for i, j in sdgsParams.items():
                print("{0}: {1}".format(i, j))
            print("Service Id: {0:#x}".format(getServiceIdFromDiagService(value, xmlElements)))
            print("DiagInstanceName: {0}".format(getSdgsDataItem(value, "DiagInstanceName")))
            requestElement = xmlElements[value.find("REQUEST-REF").attrib["ID-REF"]]
            positiveResponses = getPositiveResponse(value, xmlElements)
            print(positiveResponses)
            print("")

    pass
"""
