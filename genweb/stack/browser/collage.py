# -*- coding: utf-8 -*-
from zope.component import getMultiAdapter
from zope.component import getSiteManager
from zope.component import ComponentLookupError
from zope.interface import providedBy
from zope.interface import Interface
from zope.i18n import translate
from plone.memoize.view import memoize_contextless
from Products.CMFCore.utils import getToolByName
from Products.Collage.interfaces import IDynamicViewManager, IPortletSkin
from Products.Collage.interfaces import ICollageBrowserLayer
from Products.Collage.utilities import getCollageSiteOptions
from Products.Collage.browser.views import BaseView
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

from genweb.core import GenwebMessageFactory as _

try:
    from zope.location.interfaces import LocationError
except ImportError:
    LocationError = AttributeError


class InheritFolderView(BaseView):
    """Inherits view from folder's display setting."""

    title = _(u'Inherit')

    mapping = {
        'folder_listing': 'standard',
        'folder_full_view': 'fullview',
        'folder_summary_view': 'summary',
        'folder_tabular_view': 'tabular',
        'atct_album_view': 'album',
        'folder_extended': 'extended',
    }

    error_view_name = "error_collage-view-not-found"
    fallback_view_name = "fallback"

    def __call__(self):
        """Determine inherited view and attempt to find suitable
        collage view.

        If a view can't be determined, render fallback view. If the
        view does not exist, render an error message.
        """

        layout = self.context.getLayout()
        name = self.mapping.get(layout, self.fallback_view_name)
        spec = providedBy(self.context), ICollageBrowserLayer
        lookup = getSiteManager().adapters.lookup
        factory = lookup(spec, Interface, name=name)
        if factory is None:
            name = None
            factory = lookup(spec, Interface, name=self.error_view_name)
            if factory is None:
                raise ComponentLookupError(
                    "Layout not found: %s (and unable to render error view)." %
                    layout)
        view = factory(self.context, self.request)
        if name is None:
            view.notfoundlayoutname = layout

        view.__alias__ = self.__alias__
        return view()


class TabularFolderView(BaseView):
    title = _(u'Tabular view')


class SummaryFolderView(BaseView):
    title = _(u'Summary view')


class FullFolderView(BaseView):
    title = _(u'All content')


class AlbumFolderView(BaseView):
    title = _(u'Thumbnail view')


class ExtendedFolderView(BaseView):
    title = _(u'Extended view')
