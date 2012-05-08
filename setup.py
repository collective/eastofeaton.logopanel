from setuptools import setup, find_packages

version = '1.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='eastofeaton.logopanel',
      version=version,
      description="A Plone control panel  to allow overriding the plone site logo",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='eleddy',
      author_email='eleddy@eastofeaton.com',
      url='https://github.com/cewing/eastofeaton.logopanel',
      license='gpl',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['eastofeaton'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
	  extras_require={'test': ['plone.app.testing']},
	  entry_points="""
	  [z3c.autoinclude.plugin]
	  target = plone
	  """,
      )
