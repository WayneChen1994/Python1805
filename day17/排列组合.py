#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import itertools


res = itertools.product("0123456789", repeat=6)
print(len(list(res)))
