""" doc """

import pathlib as pa
from posixpath import join

import pkg_resources
import setuptools

import rlogging

with pa.Path('requirements.txt').open() as requirements_txt:
    install_requirements = [
        str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

long_description = pa.Path('readme.md').read_text()

setuptools.setup(
    name='rLogging',
    version='.'.join(map(str, rlogging.__version__[:3])),

    packages=setuptools.find_packages(where='rlogging', exclude=('tests', )),
    install_requires=install_requirements,
    python_requires='>=3.9',

    author='rocshers',
    author_email='rocshers@gmail.com',
    # url='rlogging.python.rocshers.com',

    description=rlogging.__doc__,
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
)
