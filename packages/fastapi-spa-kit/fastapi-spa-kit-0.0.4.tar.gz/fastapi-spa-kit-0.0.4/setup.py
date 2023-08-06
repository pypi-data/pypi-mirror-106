from setuptools import setup, find_packages


__version__ = '0.0.4'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fastapi-spa-kit',
    author='Dmitry Vasiliev',
    description='Kit for developing SPA with FastAPI.',
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=('tests',)),
    project_urls={
        'Bug Tracker': 'https://github.com/swimmwatch/fastapi-spa-kit/issues'
    },
    url='https://github.com/swimmwatch/fastapi-spa-kit',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
