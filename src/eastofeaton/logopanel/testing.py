from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class EastofeatonLogoPanel(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import eastofeaton.logopanel
        xmlconfig.file('configure.zcml',
                       eastofeaton.logopanel,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eastofeaton.logopanel:default')

EASTOFEATON_LOGOPANEL_FIXTURE = EastofeatonLogoPanel()
EASTOFEATON_LOGOPANEL_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(EASTOFEATON_LOGOPANEL_FIXTURE, ),
                       name="EastofeatonLogoPanel:Integration")
EASTOFEATON_LOGOPANEL_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(EASTOFEATON_LOGOPANEL_FIXTURE, ),
                      name="EastofeatonLogoPanel:Functional")
