import unittest2 as unittest

from plone.app.testing import TEST_USER_ID, TEST_USER_PASSWORD
from plone.app.testing import applyProfile
from plone.app.testing import setRoles

from eastofeaton.logopanel.testing import EASTOFEATON_LOGOPANEL_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = EASTOFEATON_LOGOPANEL_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_foo(self):
        import pdb; pdb.set_trace()
        self.assertTrue(False, 'this test will fail, right?')
