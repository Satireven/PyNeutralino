import io
import re

from setuptools import setup
from setuptools import find_packages

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("src/pyneutralino/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="pyneutralino",
    version=version,
    author="Satireven",
    author_email="satireven@gmail.com",
    keywords=["GUI","Flask","HTML","JavaScript","Neutralino"],
    description="A little Python module for making simple HTML/JS GUI apps with Flask",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Satireven/PyNeutralino",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    package_data={
        "neutralino": [
            "src/pyneutralino/neutralino-linux",
            "src/pyneutralino/neutralino-linux",
            "src/pyneutralino/neutralino-linux",],
        "app": [
            "src/pyneutralino/app/index.html",
            "src/pyneutralino/app/settings.json",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)