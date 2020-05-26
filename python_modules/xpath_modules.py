#! /usr/bin/env python3

from lxml import etree
import re

def pretty_print( to_print_selection ):
    if type(to_print_selection) != list:
        to_print_selection = [to_print_selection]
    
    
    for el in to_print_selection:
        if type(el) == etree._Element or type(el) == etree._ElementTree:
            xml_string = etree.tostring(el).decode()

            tabs_to_delete = len(re.sub(r'[^\t]','',xml_string.split('\n')[-1]))

            xml_parts = xml_string.split('\n')

            for part in xml_parts:
                counter = 0
                
                while len(part) > 0 and part[0] == '\t' and counter < tabs_to_delete:
                    part = part[1:]
                    counter += 1
                
                print(part)
        else:
            print(el)

def evaluate_xpath(element, xpath_statement, returnObject=False):
    if returnObject:
        return element.xpath(xpath_statement)
    else:
        pretty_print(element.xpath(xpath_statement))

def load_xml( xml_path ):
    with open( xml_path ) as xml_file:
        return etree.parse(xml_file)