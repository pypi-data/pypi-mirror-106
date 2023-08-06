#!/usr/bin/env python

from distutils.core import setup

setup(
    name="floodgate",
    version="1.1.1",
    description="Request rate limiter for Flask",
    author="Bhavesh Pareek",
    author_email="bhavesh.pareek36@gmail.com",
    packages=["floodgate", "floodgate/gates", "floodgate/fastapi", "floodgate/flask"],
    license="MIT",
    extras_require={"flask": ["Flask"], "fastapi": ["fastapi"]},
)
