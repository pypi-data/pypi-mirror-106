"""from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
   name='Speed Test Runner',
   version='0.0.1',
   description='Runs Speed Test For Given Frequency And Duration.',
   long_description=readme(),
   long_description_content_type='text/markdown',
   license="MIT",
   author='trinetra',
   keywords='core package',
   author_email='trinetra.s@vcti.io',
   packages=['speedtest'],  #same as name
   install_requires=['speedtest-cli', 'schedule', 'argparse', 'tqdm'], #external packages as dependencies
)"""



from setuptools import setup, find_packages
#from setuptools import setup, Extension, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'SpeeTest For Routers'
LONG_DESCRIPTION = 'A package that allows to run speedtest in given duration and frequency.'

# Setting up
setup(
    name="routerspeedtest",
    version=VERSION,
    author="Trinetra S",
    author_email="trinetra.s@vcti.io",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['speedtest-cli', 'schedule', 'argparse', 'tqdm'],
    keywords=['python', 'routerspeedtest'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
