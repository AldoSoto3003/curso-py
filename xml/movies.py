import xml.etree.ElementTree as ET

tree = ET.parse(r'movies.xml')
root = tree.getroot()
print(root.tag)