# -*- coding: utf-8 -*-

import os
import unittest

from yuansfer.client import Client


class ApiTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 60
        cls.assert_precision = 0.01
        cls.client = Client(environment='sandbox',merchantNo='200043',storeNo='300014',token='0c2bac90bffefbbbf84f4b17667710fd')
