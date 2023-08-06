from setuptools import setup, find_packages

setup(
    name='dataingestion',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An python package to read and write from the snowflake database.',
    long_description=open('README.md').read(),
    install_requires=['retrying', 'snowflake-connector-python'],
    url='https://pypi.org/project/dataingestion/',
    author='Dadakhalandar Mudugoti',
    author_email='dadakhalandar.mudugoti@gmail.com'
)
