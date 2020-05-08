import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IM_text-Adam-Hede", # Replace with your own username
    version="0.0.1",
    author="Adam Hede",
    author_email="adhe@implement.dk",
    description="A package to do basic text analysis in Danish very quickly and easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)