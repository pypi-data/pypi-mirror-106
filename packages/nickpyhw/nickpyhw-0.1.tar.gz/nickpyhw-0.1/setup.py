from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='nickpyhw',
      version='0.1',
      long_description = long_description,
      long_description_content_type="text/markdown",
      description='Taiwan No. 1',
      url='http://github.com/storborg/nickpyhw',
      author='NICK Hsieh',
      author_email='f226609234@gmail.com',
      license='MIT',
      packages=['nickpyhw'],
      zip_safe=False)