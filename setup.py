from setuptools import setup, find_packages

setup(
    name='multiOAuthenticator',
    version='0.2.1',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=[
        'oauthenticator',
        'aiohttp'
    ]
)
