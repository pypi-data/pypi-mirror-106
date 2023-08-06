#!/usr/bin/env python

import argparse
import python_console_package
from python_console_package.models.mymodel import MyModelClass
from python_console_package.models.module_functions import multiply
import python_console_package.models.module_functions

def main():

    parser = argparse.ArgumentParser(
        description="Template for building python console packages"
    )

    basegroup = parser.add_mutually_exclusive_group()
    basegroup.add_argument('source', nargs='?', help="A source file path for your application")
    basegroup.add_argument('-setup','--setup', action="store_true", help="Setup the prerequisites of your console application")
    basegroup.add_argument('-v','--version', action="store_true", help="Show version")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-o','--option', help="print optional text")
    group.add_argument('-m','--multiply', nargs='+', type=int, help="Multiply passed numbers")
    group.add_argument('-p','--printm', action="store_true", help="Print module stuff")
    
    # Parse the arguments
    arguments = parser.parse_args()

    if(arguments.setup):
        print("Calling application setup procedure")
    elif(arguments.version):
        print(python_console_package.__version__)
    elif(arguments.option):
        print(arguments.source)
        print(arguments.option)
    elif(arguments.multiply):
        print("Multiplying: ")
        print(arguments.multiply)
        print("Result: ")
        print(str(multiply(arguments.multiply)))
    elif(arguments.printm):
        python_console_package.models.module_functions.print_module()
        my_model_instance = MyModelClass()
        print(my_model_instance.some_basic_text)
        my_model_instance.call_something()
        print(my_model_instance.some_basic_text)
    else:
        print("Execute default module function for: " + arguments.source)