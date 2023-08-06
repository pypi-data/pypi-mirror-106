from setuptools import setup

with open("README.rst", "r") as file:
   long_description = file.read()

setup(
    name='whirlcalc',
    version='2b0',    
    description='''A Python module made for use with numbers and data''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Whirlpool-Programmer/whirlcalc',
    author='Whirlpool-Programmer',
    author_email='whirlpool.programmer@outlook.com',
    license='MIT License',
    packages=['whirlcalc'],
    classifiers =[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ]
)
