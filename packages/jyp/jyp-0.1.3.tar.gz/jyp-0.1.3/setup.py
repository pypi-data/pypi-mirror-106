import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jyp",
    version="0.1.3",
    author="Michael Lindner-D'Addario",
    author_email="michael.lindner.daddario@gmail.com",
    description="Pocket converter for Korean to Canadian currency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MDAddario/jyp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['src/twice'],
    python_requires=">=3.6",
    install_requires=[
        'numpy>=1.20.3',
        'pandas'
    ],
    scripts=['bin/jyp'],
)