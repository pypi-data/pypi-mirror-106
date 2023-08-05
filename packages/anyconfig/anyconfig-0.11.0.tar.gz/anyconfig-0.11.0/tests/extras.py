#
# Copyright (C) 2016 - 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring

import unittest
import sys


class TestImportErrors(unittest.TestCase):

    def test_20_ac_parsers(self):
        for mod in ("yaml", "msgpack", "toml", "bson"):
            sys.modules[mod] = None
            import anyconfig.parsers

            self.assertTrue(sys.modules[mod] is None)
            self.assertFalse(anyconfig.parsers is None)

    def test_30_ac_schema(self):
        mod = "jsonschema"
        sys.modules[mod] = None
        import anyconfig.schema

        self.assertTrue(sys.modules[mod] is None)
        self.assertFalse(anyconfig.schema is None)

# vim:sw=4:ts=4:et:
