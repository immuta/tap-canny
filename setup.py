#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="tap-canny",
    version="0.0.1",
    description="Singer.io tap for extracting data",
    author="Zane Patten",
    url="http://github.com/immuta/tap-canny",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    packages=setuptools.find_packages(),
    py_modules=["tap_canny"],
    entry_points="""
        [console_scripts]
        tap-canny=tap_canny.tap:cli
    """,
    package_data={"schemas": ["tap_canny/schemas/*.json"]},
    install_requires=["singer-sdk"],
    include_package_data=True,
)
