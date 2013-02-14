import unittest2 as unittest
from genweb.stack.testing import GENWEBUPCSTACK_INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import applyProfile

from plone.testing import z2
from plone.app.folder.utils import findObjects
from zope.component import getMultiAdapter
from os.path import abspath
from os.path import dirname
from os.path import join
from Products.CMFCore.utils import getToolByName
from plone.locking.interfaces import ILockable


class IntegrationTest(unittest.TestCase):

    layer = GENWEBUPCSTACK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def testBasicProducts(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'f1', title=u"Soc una carpeta")
        f1 = portal['f1']

        # Collage
        f1.invokeFactory('Collage', 'collage', title=u"Soc un collage")
        self.assertEqual(f1['collage'].Title(), u"Soc un collage")
        # PloneFormGen
        f1.invokeFactory('FormFolder', 'formulari', title=u"Soc un formulari")
        self.assertEqual(f1['formulari'].Title(), u"Soc un formulari")
        # PlonePopoll
        f1.invokeFactory('PlonePopoll', 'enquesta', title=u"Soc una enquesta")
        self.assertEqual(f1['enquesta'].Title(), u"Soc una enquesta")
        # windowZ
        f1.invokeFactory('Window', 'window', title=u"Soc un window")
        self.assertEqual(f1['window'].Title(), u"Soc un window")
        # Ploneboard
        f1.invokeFactory('Ploneboard', 'forum', title=u"Soc un forum")
        self.assertEqual(f1['forum'].Title(), u"Soc un forum")
        # PloneSurvey
        f1.invokeFactory('Survey', 'questionari', title=u"Soc un questionari")
        self.assertEqual(f1['questionari'].Title(), u"Soc un questionari")
        # Meeting
        f1.invokeFactory('Meeting', 'reunio', title=u"Soc una reunio")
        self.assertEqual(f1['reunio'].Title(), u"Soc una reunio")
        # Tasques
        f1.invokeFactory('simpleTask', 'tasca', title=u"Soc una tasca")
        self.assertEqual(f1['tasca'].Title(), u"Soc una tasca")

    def testAdditionalProducts(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'f1', title=u"Soc una carpeta")
        f1 = portal['f1']

        # Serveis
        applyProfile(portal, 'upc.genweb.serveis:default')
        f1.invokeFactory('Servei', 'servei', title=u"Soc un servei")
        self.assertEqual(f1['servei'].Title(), u"Soc un servei")

        # Descriptor TIC
        applyProfile(portal, 'upc.genweb.descriptorTIC:default')
        f1.invokeFactory('CarpetaTIC', 'carpetaTIC', title=u"Soc una carpetaTIC")
        self.assertEqual(f1['carpetaTIC'].Title(), u"Soc una carpetaTIC")

        # ObjectiusCG
        applyProfile(portal, 'upc.genweb.objectiusCG:default')
        f1.invokeFactory('ObjectiuGeneralCG', 'objectiuGeneralCG', title=u"Soc una objectiuGeneralCG")
        self.assertEqual(f1['objectiuGeneralCG'].Title(), u"Soc una objectiuGeneralCG")

    def testFolderConstrains(self):
        from genweb.stack.events import CONSTRAINED_TYPES, IMMEDIATELY_ADDABLE_TYPES
        from zope.event import notify
        from Products.Archetypes.event import ObjectInitializedEvent
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Folder', 'userfolder', title=u"Soc una carpeta")
        folder = self.portal['userfolder']
        notify(ObjectInitializedEvent(folder))
        self.assertEqual(sorted(folder.getLocallyAllowedTypes()), sorted(CONSTRAINED_TYPES))
        self.assertEqual(sorted(folder.getImmediatelyAddableTypes()), sorted(IMMEDIATELY_ADDABLE_TYPES))

    # Worked, but it stopped working when refactor the independence of genweb.core from the rest of the stack
    # def test_migrateSecciotype(self):
    #     z2.installProduct(self.layer['app'], 'Products.LinguaPlone')
    #     path = join(abspath(dirname(__file__)), 'seccio.zexp')
    #     path_ca = join(abspath(dirname(__file__)), 'seccio-ca.zexp')
    #     setRoles(self.portal, TEST_USER_ID, ['Manager'])
    #     login(self.portal, TEST_USER_NAME)
    #     ptypes = getToolByName(self.portal, 'portal_types')
    #     ptypes['Plone Site'].allowed_content_types = ['Document', 'File', 'Folder', 'Image', 'Seccio']
    #     pw = getToolByName(self.portal, 'portal_workflow')
    #     pw.setDefaultChain('genweb_simple')
    #     pw.setChainForPortalTypes(('Seccio',), 'genweb_simple')
    #     self.portal._importObjectFromFile(path)
    #     self.portal._importObjectFromFile(path_ca)

    #     self.assertEqual(len([obj for obj in findObjects(self.portal['arealseccio'])]), 6)
    #     test_page = self.portal['arealseccio'].unrestrictedTraverse('/plone/arealseccio/anotherfolder/withotherfolder/otherpage')
    #     self.assertEqual(test_page.id, 'otherpage')

    #     # Lock a page for testing
    #     ILockable(test_page).lock()
    #     self.assertEqual(ILockable(test_page).locked(), True)

    #     # Once we have the fixture in place, test the migration
    #     migrationview = getMultiAdapter((self.portal, self.request), name='migrateSeccioType')
    #     migrationview.render()

    #     # Test the new objects are the same, and are correct.
    #     self.assertEqual(self.portal['arealseccio'].portal_type, 'Folder')
    #     self.assertEqual(self.portal['arealseccio_old'].portal_type, 'Seccio')
    #     self.assertEqual(self.portal['arealseccio_old'].objectIds(), [])
    #     self.assertEqual(len([obj for obj in findObjects(self.portal['arealseccio'])]), 6)
    #     self.assertEqual(test_page.id, 'otherpage')

    #     self.assertEqual(self.portal['arealseccio'].getLanguage(), 'en')
    #     self.assertEqual(self.portal['arealseccio'].getTranslations().keys(), ['ca', 'en'])
    #     self.assertEqual(self.portal['arealseccio'].getTranslations()['ca'][0], self.portal['arealseccio-ca'])
