#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pprint
from functools import partial
p = partial(pprint.pprint, width=1)


def foo():
    print('foo')




def main():
    print('Hello') #E262!
    p({'foo': 'F', 'bar':'B'})
    print("Python", ("Hello",
                "World"))
    x = 6
    y = 1
    if x > 5: y = 10

    z = (x +
         y)

    my_tuple = 1,	2,	3 # E242




#E265!
## E266!


if __name__ == '__main__':
    main()
