from setuptools import setup, find_packages

setup(
    name='generate_account',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    author='andy-dang',
    description='Generate password and username',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
