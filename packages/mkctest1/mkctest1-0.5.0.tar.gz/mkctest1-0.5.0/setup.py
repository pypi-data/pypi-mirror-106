from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

MAJOR_VERSION = '0'
MINOR_VERSION = '5'
MICRO_VERSION = '0'
VERSION = f"{MAJOR_VERSION}.{MINOR_VERSION}.{MICRO_VERSION}"
__version__ = VERSION

setup(name='mkctest1',
      version=VERSION,
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/funniest',
      author='Michael Chen',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['mkctest1'],
      zip_safe=False)