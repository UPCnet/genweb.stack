from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='genweb.stack',
      version=version,
      description="Genweb generic stack of products",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
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
          'upc.genweb.meetings',
          'upc.genweb.serveis',
          'upc.genweb.descriptorTIC',
          'upc.genweb.kbpuc',
          'upc.genweb.objectiusCG',
          'upc.genweb.soa',
          'upc.cloudPrivat',
          'upcnet.cas',
          'upcnet.stats',
          'upcnet.simpleTask',
          'Products.LinguaPlone',
          'Products.PloneLDAP',
          'Products.PloneFormGen',
          'Products.Collage',
          'Products.Ploneboard',
          'Products.Poi',
          'Products.windowZ',
          'Products.PlonePopoll',
          'Products.PloneSurvey',
          'Products.DataGridField',
          # Experimental GW4
          'Solgema.fullcalendar',
          'collective.pfg.dexterity',
          'collective.collage.ploneformgen',
          'pfg.drafts',
          # 'collective.recaptcha',
          'plone.formwidget.recaptcha',
          'collective.tinymcetemplates',
          # To extinct
          'upc.genwebupc',
          'upc.genwebupctheme',
          'upc.genweb.recaptcha',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
