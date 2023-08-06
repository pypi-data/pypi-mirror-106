import setuptools, os

PACKAGE_NAME = "algodata"
VERSION = "0.0.0"
AUTHOR = "Tim Esler"
EMAIL = "tim.esler@gmail.com"
DESCRIPTION = "Tools for interacting with financial timeseries for algorithmic trading"
GITHUB_URL = "https://github.com/timesler/algodata"

parent_dir = os.path.dirname(os.path.realpath(__file__))

with open(f"{parent_dir}/docs/README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="."),
    install_requires=[
        "numpy",
        "pandas",
        "attrdict",
        "xt-training",
        "dash",
        "jupyter-dash",
    ],
    python_requires=">=3.6",
)
