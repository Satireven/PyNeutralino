from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyneutralino",
    version="1.0.1",
    author="Satireven",
    author_email="satireven@gmail.com",
    description="A little Python module for making simple HTML/JS GUI apps with Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Satireven/PyNeutralino",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)