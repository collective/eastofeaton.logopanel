from zope.schema import Bytes
from zope.schema import ValidationError
from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts
from zope.formlib import form
from zope.i18nmessageid import MessageFactory
from plone.app.controlpanel.form import ControlPanelForm

from OFS.Image import Image
from OFS.Image import getImageInfo
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.utils import getToolByName

_ = MessageFactory('LogoPanel')

LOGO_ID = 'logo.png'


class ImageValidationError(ValidationError):
    """Supplied file does not appear to be an image"""


def validateLogoIsImage(value):
    ct, w, h = getImageInfo(value)
    if ct == '':
        raise ImageValidationError(value)
    return True


class ILogoPanelSchema(Interface):

    logo = Bytes(title=_(u'New Logo File'),
                 description=_(u'Upload a new file to replace the site logo'),
                 required=True,
                 constraint=validateLogoIsImage)


class LogoPanelAdapter(object):

    adapts(IPloneSiteRoot)
    implements(ILogoPanelSchema)

    def __init__(self, context):
        self.context = context

    def get_logo(self):
        logo = ''
        try:
            logo = self.context.restrictedTraverse(LOGO_ID)
        except KeyError:
            # there is no logo.png that can be traversed to, punt
            pass

        return logo

    def set_logo(self, value):
        # it just seems better to do this in the 'on save' method below
        pass

    logo = property(get_logo, set_logo)


class LogoPanel(ControlPanelForm):

    template = ViewPageTemplateFile('logopanel.pt')

    form_fields = form.FormFields(ILogoPanelSchema)
    form_name = _(u'Logo Upload Form')
    label = _(u'Site Logo Control Panel')
    description = _(u'Replace the site-wide logo')

    @property
    def current_logo(self):
        tag = '<span class="discreet"><No Logo Found></span>'
        try:
            logo = self.context.restrictedTraverse(LOGO_ID)
            tag = logo.tag()
        except KeyError:
            # none was found, return the default tag
            pass

        return tag

    def _on_save(self, data=None):
        if data is None:
            # no form data, return without doing anything
            return

        new_logo = data['logo']
        if not new_logo:
            # logo not uploaded, return without doing anything
            return

        skins = getToolByName(self.context, 'portal_skins')
        target = self.context
        if 'custom' in skins:
            target = skins['custom']

        if LOGO_ID in target:
            img = target[LOGO_ID]
            if isinstance(img, Image):
                # this is an OFS image, or subclass, we should have the
                # update_data method
                try:
                    img.update_data(new_logo)
                    return
                except TypeError, e:
                    # there is a problem with the logo data, it's unicode
                    raise e
                except AttributeError, e:
                    # no update_data method.  make a new one and replace this
                    # one
                    pass
            else:
                # let's override it, it isn't an expected type.
                pass

        img = Image(LOGO_ID, 'Custom Site Logo', new_logo)
        target._setObject(LOGO_ID, img)
        return
