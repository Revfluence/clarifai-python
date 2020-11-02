from setuptools import setup, find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="clarifai",
    description='Clarifai API Python Client',
    version='2.0.27',
    author='Clarifai',
    maintainer='Robert Wen',
    maintainer_email='robert@clarifai.com',
    url='https://github.com/clarifai/clarifai-python',
    author_email='support@clarifai.com',
<<<<<<< HEAD
    install_requires=['future==0.15.2',
                       'requests==2.13.0',
                       'configparser==3.5.0',
                       'jsonschema==2.5.1',
                       'Pillow==2.9.0'],
=======
    install_requires=['future>=0.15, <2',
                      'requests>=2.13, <3',
                      'configparser>=3.5, <4',
                      'jsonschema>=2.5, <3'] +
                     [] if has_enum else ['enum34>=1.1, <2'],
>>>>>>> parent of b1fbdba... Version 2.2.2. Fixed installing dependencies for Python <3.4.
    packages=find_packages(),
    license="Apache 2.0",
    scripts=['scripts/clarifai'],
)
