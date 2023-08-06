from setuptools import setup

setup(
    name='bufcrypt',
    packages=["bufcrypt"],
    version='0.1.0',
    author='Perzan',
    author_email='PerzanDevelopment@gmail.com',
    install_requires = [
        "cryptography~=3.4"
    ]
)