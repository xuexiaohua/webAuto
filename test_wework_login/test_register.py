#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_wework_login.indexPO import IndexPO


class TestRegister:
    def setup(self):
        self.index = IndexPO()

    def test_register(self):
        result = self.index.goto_register().register()
        assert result