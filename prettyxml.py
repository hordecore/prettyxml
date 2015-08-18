import sys
import xml.dom.minidom

print xml.dom.minidom.parse(sys.argv[1]).toprettyxml().encode('utf-8')
