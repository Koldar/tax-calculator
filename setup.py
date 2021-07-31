import os
from setuptools import setup, find_packages

from tax_calculator import version


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tax-calculator",
    version=version.VERSION,
    author="Massimo Bono",
    author_email="massimobono1@gmail.com",
    description="Allows you to compute taxes",
    license="MIT",
    keywords="tax",
    url="https://github.com/Koldar/tax-calculator",
    packages=find_packages(),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    license_files="LICEN[SC]E*.md",
    python_requires=">=3.6",
    install_requires=[
        "arrow>=1.1.1",
        "beautifulsoup4>=4.9.3",
        "python-dateutil>=2.8.2",
        "requests>=2.26.0",
        "soupsieve>=2.2.1",
        "stringcase>=1.2.0",
        "urllib3>=1.26.6",
    ],
    include_package_data=True,
    package_data={
        "": ["package_data/*.*"],
    },
    entry_points={"console_scripts": [f"tax-calculator=tax_calculator.main:main"]},
)