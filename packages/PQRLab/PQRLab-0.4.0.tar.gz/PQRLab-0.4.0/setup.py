#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="PQRLab",
  version="0.4.0",
  author="PQR Team",
  author_email="carrollxiang@gmail.com",
  description="Controll System for PQR.",
  long_description="Controll System for PQR.",
  long_description_content_type="text/markdown",
  url="https://gitee.com/teshenghsiang/PQRLab",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  include_package_data=True,
  package_data={'PQRLab': ['pqrcore/*']}
)