from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='osmcha',
      version='0.1',
      description="Python package to detect suspicious OSM changesets",
      long_description=long_description,
      classifiers=[],
      keywords=['openstreetmap', 'osm', 'QA'],
      author="Wille Marcel",
      author_email='wille@wille.blog.br',
      url='https://github.com/willemarcel/osmcha',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data={'osmcha': ['models/autovandal.pkl']},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'requests',
          'homura',
          'shapely',
          'python-dateutil',
          'numpy',
          'scipy',
          'scikit-learn',
          'gabbar==0.2'
      ],
      dependency_links=['https://github.com/mapbox/gabbar/tarball/master#egg=gabbar-0.2'],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      osmcha=osmcha.scripts.cli:cli
      """
      )
