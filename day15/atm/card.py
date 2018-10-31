#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


class Card:
    def __init__(self, cardNum, psd, money, islock=False):
        self.cardNum = cardNum
        self.psd = psd
        self.money = money
        self.islock = islock
