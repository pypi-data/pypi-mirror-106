from setuptools import setup
import sys
import os 

#this_directory = path.abspath(path.dirname(__file__))
#with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(name='logregnumpy',
      version='0.1.1',
      description='Logistic Regression Classifier',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['logregnumpy'],
      author_email='kir.klyukvin@gmail.com',
      zip_safe=False)
