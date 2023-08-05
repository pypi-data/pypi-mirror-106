"""Setup script for cmc_dataeng_internship_maudeplucker"""

import os.path
import setuptools 
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
#README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cmc_dataeng_internship_maudeplucker",
    version="1.0.0",
    description="Find out what our moto is!",
    #long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/maudeplucker/cmc_dataeng_internship_maudeplucker",
    author="Maude Plucker",
    author_email="mplucker@posteo.net",
    license="None",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    #packages=["cmc_dataeng_internship_maudeplucker"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "cmc_dataeng_internship_maudeplucker=cmc_dataeng_internship_maudeplucker.__main__:main",
        ]
    },
)

