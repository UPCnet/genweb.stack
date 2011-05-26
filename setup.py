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
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='UPCnet Plone Team',
      author_email='plone.team@upcnet.es',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.LinguaPlone',
          'plone.app.discussion',
          'plone.app.caching',
          'Products.PloneFormGen',
          'Products.Collage',
          'Products.Ploneboard',
          'Products.Poi',
          'Products.windowZ',
          'Products.PlonePopoll',
          # Experimental GW4
          'collective.collage.ploneformgen',
          'pfg.drafts',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
