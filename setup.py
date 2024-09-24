import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EZLog-RCL",
    version="1.0.0.0",
    author="Rei-Chi Lin",
    author_email="fatalframe0719@gmail.com",
    description="an easy logger without setting on PIP platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rickiarty/EZLog_Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
