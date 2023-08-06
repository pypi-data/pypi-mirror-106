import setuptools
# from resource.config import EzConfig

import os, sys
import json

python_path = os.path.realpath(__file__).split(os.sep)[:-1]
# print(python_path)
config_path = python_path + ['resource','config.json']
config_path = os.sep.join(config_path)

with open(config_path, 'r') as f:
    version = json.load(f)['version']

# print(version)

# import json

# import configparser

# config_path = './resource/config.properties'
# # read config
# parser = configparser.ConfigParser()
# parser.read(config_path)
# config = parser['default']
# version = config['version']


# save README.md as var
with open("README.md", "r") as fh:
    long_description = fh.read()


# with open("./resource/config.json") as configfile:
#     version = json.load(configfile)["version"]

requirements = [
    "pandas",
    "numpy",
    "sklearn",
    "xgboost",
]

# version = EzConfig().__version__


setuptools.setup(
    name="ggwp", 
    version=version,
    license='MIT',
    author="Pathompol Nilchaikovit",
    author_email="data.noob.lol@gmail.com",
    description="Prepare Fast, Analyze Faster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datanooblol/ggwp",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)