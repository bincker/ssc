#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       ssc.py
#       
#       Copyright 2013 Victor Dorneanu
#       
#       Main file
#

import sys
from utils import mypath
import ModuleBase       
from ModuleCollection import ModuleCollection
from discovery.Testing import Testing


def test_module_collection():
    collection = ModuleCollection("./lib/modules")
    collection.print_collection()
    print(len(collection))

    
def main():
    # Some testing
    test_params = 'a=b,a=c,a=d,b=e,x=123,z=6'
    t = Testing()
    test_module_collection()
    print(t.read_parameters(test_params))


if __name__ == '__main__':
	main()

