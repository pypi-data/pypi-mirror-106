import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="countapi",
    version="1.0",
    author="Ben Godfrey",
    author_email="BenJetson@users.noreply.github.com",
    description="An unofficial Python client library for CountAPI (countapi.xyz).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenJetson/py-countapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
