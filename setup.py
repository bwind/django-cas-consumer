
from setuptools import setup, find_packages

setup(
    name='django-cas-consumer',
    version='0.1dev',
    description='A "consumer" for the Central Authentication Service (http://jasig.org/cas)',
    author='Chris Williams',
    author_email='chris@nitron.org',
    url='http://nitron.org/',
    packages=find_packages(),
    zip_safe=False,
)
