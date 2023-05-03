from setuptools import setup, find_packages

setup(
    name='multiOAuthenticator',
    version='0.2',
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=[
        'oauthenticator',
        'aiohttp'
    ]
)
