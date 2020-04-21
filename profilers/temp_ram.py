from custom_classes import Thanos
from memory_profiler import profile
import ast
import argparse
import sys
import json


@profile
def test_class_function(a, b):
    obj = Thanos(a)
    res = obj.custom_function(b - 1)
    c = [2] * 10**b
    return res

if __name__ == "__main__":     
        parser = argparse.ArgumentParser()
        parser.add_argument('-dummy_pos', nargs='*')
        parser.add_argument('--dummy_optional', nargs="?")    
        args = parser.parse_args()

        star_args = args.dummy_pos
        optional_args = args.dummy_optional

        if optional_args:
            optional_args = optional_args.replace("'", '"')
            optional_args = json.loads(json.loads(json.dumps(optional_args)))
        else:
            optional_args = {} 

        dummy_args = []
        for arg in star_args:
            if arg.isnumeric():
                dummy_args.append(ast.literal_eval(arg))
            else:
                dummy_args.append(arg)


        test_class_function(*dummy_args, **optional_args)
                        