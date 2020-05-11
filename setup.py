import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IM_text-Adam-Hede", # Replace with your own username
    version="0.0.2",
    author="Adam Hede",
    author_email="adhe@implement.dk",
    description="A package to do basic text analysis in Danish very quickly and easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
                'pandas~=0.25.1',
                'wordcloud~=1.7.0',
                # 'easybert~=1.0.3',        Too touch a requirement. Forces installs to TensorFlow 1.x
                'vadersentiment~=3.2.1',
                'afinn~=0.1',
                'numpy~=1.17.2',
                'sklearn~=0.0',
                'scikit-learn~=0.21.3',
                'matplotlib~=3.1.1',
                'setuptools~=46.0.0'
          ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)