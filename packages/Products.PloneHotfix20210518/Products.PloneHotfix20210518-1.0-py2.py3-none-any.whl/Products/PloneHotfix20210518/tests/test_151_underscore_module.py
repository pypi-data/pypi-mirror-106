# -*- coding: utf-8 -*-
from Products.PageTemplates.Expressions import boboAwareZopeTraverse
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.PloneHotfix20210518.tests import BaseTest
from zExceptions import NotFound

import os
import random
import string
import unittest


try:
    # Python 3.7+
    from random import _os
except ImportError:
    # Python 3.6- is not vulnerable.
    _os = None

# Path of this directory:
path = os.path.dirname(__file__)


class TestAttackVector(BaseTest):
    def _makeOne(self, name):
        return PageTemplateFile(os.path.join(path, name)).__of__(self.portal)

    @unittest.skipIf(_os is None, "This Python version has no random._os.")
    def test_template_bad1(self):
        template = self._makeOne("bad1.pt")
        # In some versions, random is not globally available, so we get a NameError.
        # Otherwise our patch should make sure we get a NotFound.
        with self.assertRaises((NotFound, NameError)):
            template()

    def test_template_bad2(self):
        template = self._makeOne("bad2.pt")
        with self.assertRaises(NotFound):
            template()


class TestDirectAttackVector(unittest.TestCase):

    @unittest.skipIf(_os is None, "This Python version has no random._os.")
    def test_boboAwareZopeTraverse_random(self):
        with self.assertRaises(NotFound):
            boboAwareZopeTraverse(random, ("_os", "system"), None)

    def test_boboAwareZopeTraverse_string(self):
        with self.assertRaises(NotFound):
            boboAwareZopeTraverse(string, ("_re", "purge"), None)
