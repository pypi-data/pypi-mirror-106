import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SprinklrClient", 
    version="0.21.5.17.5",
    author="Steven Dzilvelis",
    author_email="steven_dzilvelis@hotmail.com",
    description="A Python client for using the Sprinklr API",
    license="GNU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DzRepo/SprinklrClient",
    project_urls={
        "Bug Tracker": "https://github.com/dzrepo/sprinklrclient/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
    install_requires=[
        "requests",
    ],
)
