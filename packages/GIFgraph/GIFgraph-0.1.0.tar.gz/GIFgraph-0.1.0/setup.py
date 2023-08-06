from setuptools import setup, find_packages

VERSION = '0.1.0'
PACKAGE_NAME = 'GIFgraph'
AUTHOR = 'Henry Taylor'
AUTHOR_EMAIL = 'henrysrtaylor@gmail.com'
URL = 'https://github.com/henrysrtaylor/GIFgraph'
LICENSE = 'LICENSE.txt'
DESCRIPTION = 'GIFgraph provides animated data visuals in the form of GIFs.'
LONG_DESCRIPTION =open('README.txt').read()
LONG_DESC_TYPE = "text/markdown"
package_data = {'': ['*.txt', '*gif']}
INSTALL_REQUIRES = [
      'pillow',
      'glob2',
      'matplotlib',
      'pyglet',
      'numpy'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      package_data= package_data,
      include_package_data=True
      )
