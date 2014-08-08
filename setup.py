from setuptools import setup, find_packages
import os

version = '2.0'

README = open("README.rst").read()
HISTORY = open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='genweb.stack',
      version=version,
      description="Genweb generic stack of products",
      long_description=README + "\n" + HISTORY,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='',
      author='UPCnet Plone Team',
      author_email='plone.team@upcnet.es',
      url='https://github.com/upcnet/genweb.core',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['genweb'],
      extras_require={'test': ['plone.app.testing']},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'genweb.packets',
          'Products.PloneLDAP',
          'Products.PloneFormGen',
          'Products.Collage',
          'Products.windowZ',
          'upcnet.cas',
          'upcnet.stats',
          'genweb.banners',
          # To improve/migrate to dexterity
          'upc.genweb.logosfooter',
          # Experimental GW4
          'collective.polls',
          'collective.pfg.dexterity',
          'collective.collage.ploneformgen',
          'pfg.drafts',
          'collective.recaptcha',
          'plone.formwidget.recaptcha',
          # Disabled by default until needed
          # 'upc.genweb.serveis',
          # 'upc.genweb.descriptorTIC',
          # 'upc.genweb.kbpuc',
          # 'upc.genweb.objectiusCG',
          # 'upc.genweb.soa',
          # 'upc.cloudPrivat',
          # Deprecated
          # 'upc.genwebupc',
          # 'upc.genwebupctheme',
          # 'upc.genweb.recaptcha',
          # 'Products.Poi',
          # 'Products.PloneSurvey',
          # 'Products.DataGridField',
          # 'Products.Ploneboard',
          # 'Products.LinguaPlone',
          # 'upcnet.simpleTask',
          # 'upc.genweb.meetings',
          # 'Products.PlonePopoll',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
