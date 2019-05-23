#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pprint
from functools import partial
p = partial(pprint.pprint, width=1)


def main():
    print('Hello')
    p({'foo': 'F', 'bar': 'B'})


if __name__ == '__main__':
    main()
