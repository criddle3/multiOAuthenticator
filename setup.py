from setuptools import setup, find_packages

setup(
    name='2sigma-multioauthenticator',
    version='0.1',
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=[
        'oauthenticator',
        'aiohttp'
    ]
)
