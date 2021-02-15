#!/bin/python3
# Program: cdb.py
# Author: Tian Niezing
# Date: 14-02-2021
#

import xml.etree.ElementTree as ET 

def get_adjectives(filename):
    cdbdocument = ET.parse(filename)
    root = cdbdocument.getroot()
        
    is_adj = [cid.get('form') for cid in root.findall('cid') if cid.attrib['pos'] == 'ADJ']
    return(set(is_adj))

def main():
    print(get_adjectives('cdb-sample.xml'))
    

if __name__ == '__main__':
    main()