from os.path import abspath, join

from setuptools import setup, find_packages

from asyncdex import version

with open(abspath(join(__file__, "..", "README.rst"))) as file:
    long_desc = file.read()

setup(
    name="AsyncDex",
    version=version,
    packages=find_packages(exclude=("tests",)),
    url="https://github.com/PythonCoderAS/AsyncDex",
    license="MIT",
    author="PythonCoderAS",
    author_email="pokestarfan@yahoo.com",
    description="Async MangaDex library",
    long_description=long_desc,
    install_requires=["aiohttp", "natsort"],
    extras_require={"docs": ["sphinx", "sphinx-rtd-theme"], "tests": ['pytest', 'asynctest', 'pytest-asyncio',
                                                                  'pytest-recording', 'vcrpy', "pytest-mypy"]},
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
