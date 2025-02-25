import setuptools


def parse_requirements(filename, session=None):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

dependencies = [
    "ipdb",
    "nptyping==1.3.0",
    "numpy==1.22.3",
    "PyJWT",
    "torch",
    "tqdm"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stringlifier39",
    version="0.1.1.7",
    author="Multiple authors",
    author_email="garvit.ism@gmail.com",
    description="Python module for detecting password, api keys hashes and any other string that resembles a randomly generated character sequence.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adobe/stringlifier",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    classifiers=(
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    include_package_data=True,
    package_data={
        '': ['data/string-c.encodings', 'data/string-c.conf', 'data/string-c.bestType', 'data/enhanced-c.encodings',
             'data/enhanced-c.conf', 'data/enhanced-c.bestType']

    },
    # data_files=['data/string-c.encodings', 'data/string-c.conf', 'data/string-c.bestType'],
    zip_safe=False
)
