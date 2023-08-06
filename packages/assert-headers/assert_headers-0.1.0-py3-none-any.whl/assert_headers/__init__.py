#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Classes
from assert_headers.HeaderAssertionError import HeaderAssertionError

# Functions in order they depend on each other
from assert_headers.getMeta import getMeta
from assert_headers.assertHeaders import assertHeaders
from assert_headers.assertHeadersFromUrl import assertHeadersFromUrl

# CLI Scripts
from assert_headers.cli import cli

# if __name__ == '__main__':
#     cli()
