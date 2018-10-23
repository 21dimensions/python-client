import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyeasy",
    version="1.0.2",
    author="EasyEasy.io",
    author_email="feedback@easyeasy.io",
    description="Client for EasyEasy.io cloud database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EasyEasyio/python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
)