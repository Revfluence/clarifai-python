from setuptools import setup, find_packages

setup(
    name="clarifai",
    description='Clarifai API Python Client',
    version='2.2.2',
    author='Clarifai',
    maintainer='Robert Wen',
    maintainer_email='robert@clarifai.com',
    url='https://github.com/clarifai/clarifai-python',
    author_email='support@clarifai.com',
    python_requires='>=3.8',
    install_requires=['requests>=2.13, <3',
                      'jsonschema>=2.5, <3'],
    packages=find_packages(),
    license="Apache 2.0",
    scripts=['scripts/clarifai'],
)
