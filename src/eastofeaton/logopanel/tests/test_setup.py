import unittest2 as unittest

# from plone.app.testing import TEST_USER_ID, TEST_USER_PASSWORD
# from plone.app.testing import applyProfile
# from plone.app.testing import setRoles

from Products.CMFCore.utils import getToolByName

from eastofeaton.logopanel.testing import\
    EASTOFEATON_LOGOPANEL_INTEGRATION_TESTING


class TestSetup(unittest.TestCase):

    layer = EASTOFEATON_LOGOPANEL_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.cp = getToolByName(self.portal, 'portal_controlpanel')

    def test_product_installed(self):
        """ validate that our product GS profile has been run and installed
        """
        pid = 'eastofeaton.logopanel'
        installed = [p['id'] for p in self.qi_tool.listInstalledProducts()]
        self.assertTrue(pid in installed,
                        "Package appears not to be installed")
    
    def test_panel_available(self):
        """ validate that the logopanel is registered with portal controlpanel
        """
        all_configlets = [c.id for c in self.cp.listActions()]
        expected_id = "LogoPanel"
        self.assertTrue(expected_id in all_configlets,
                        "%s configlet not in control panel" % expected_id)
        # assert configlet is in correct category
        for configlet in self.cp.listActions():
            if configlet.id == expected_id:
                self.assertTrue(configlet.category == 'Plone',
                                "%s configlet appears to be in the wrong category")
