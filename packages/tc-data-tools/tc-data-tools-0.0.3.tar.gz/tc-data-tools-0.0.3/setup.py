from setuptools import setup, find_packages

VERSION = "0.0.3"

setup(
    name="tc-data-tools",
    version=VERSION,
    description="Data tools to help our daily job",
    url="https://github.com/ciro-tc/tc-data-tools",
    author="TC Data Science",
    author_email="ciro.oliveira@tc.com.br",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas==1.2.4",
        "pandas-gbq==0.15.0",
        "google-cloud-bigquery==2.15.0",
        "google-cloud-storage==1.38.0",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
