#!/usr/bin/env python
"""setuptools script for installing trellnotes"""
import os
from setuptools import find_packages, setup

_project_root = os.path.abspath(os.path.dirname(__file__))

setup(
    name="trellnotes",
    version="0.0.1",
    author="Ryan Himmelwright",
    author_email="ryan.himmelwright@gmail.com",
    url='http://gitlab.himmelwright.net/trello-notes/',
    description='Parses trello json exports and outputs it in note form',
    license="GPL-3.0",
    keywords=["json", "notes", "trello"],
    packages=find_packages(include=['trellnotes*']),
    scripts=['bin/trellnotes']
)
