from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyneutralino",
    version="1.0.0",
    author="Satireven",
    author="satireven@gmail.com",
    description="A little Python module for making simple HTML/JS GUI apps with Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)