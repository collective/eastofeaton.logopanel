from zope.schema import Bytes
from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts
from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from plone.app.controlpanel.form import ControlPanelForm

from Products.CMFPlone.interfaces import IPloneSiteRoot

_ = MessageFactory('LogoPanel')


class ILogoPanelSchema(Interface):

    logo = Bytes(title=_(u'New Logo File'),
                 description=_(u'Upload a new file to replace the site logo'),
                 required=False)


class LogoPanelAdapter(object):

    adapts(IPloneSiteRoot)
    implements(ILogoPanelSchema)

    def __init__(self, context):
        self.context = context

    def get_logo(self):
        print 'I am the getter method'
        import pdb; pdb.set_trace( )
        return ''

    def set_logo(self, value):
        import pdb; pdb.set_trace( )
        print 'I am the setter method'

    logo = property(get_logo, set_logo)


class LogoPanel(ControlPanelForm):
    form_fields = form.FormFields(ILogoPanelSchema)
    form_name = _(u'Site Logo Control Panel')
    label = _(u'Site Logo Control Panel')
    description = _(u'Replace the site-wide logo')

    def _on_save(self):
        print('I am the _on_save method')
        import pdb; pdb.set_trace( )
