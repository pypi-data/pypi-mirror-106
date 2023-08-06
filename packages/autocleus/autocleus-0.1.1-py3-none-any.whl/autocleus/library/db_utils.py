#!/usr/bin/env python3

from sqlalchemy.types import VARCHAR
from sqlalchemy import func


class HashColumn(VARCHAR):

    def bind_expression(self, bindvalue):
        """Convert the bind's type from String to HEX encoded"""
        return func.HEX(bindvalue)

    def column_expression(self, col):
        """Convert select value from HEX encoded to String"""
        return func.UNHEX(col)
