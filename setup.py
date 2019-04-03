#!/usr/bin/env python
"""setuptools script for installing trellnotes"""

from setuptools import setup

setup(
    name="trellnotes",
    version="0.0.1",
    author="Ryan Himmelwright",
    author_email="ryan.himmelwright@gmail.com",
    url='http://gitlab.himmelwright.net/trello-notes/',
    description='Parses trello json exports and outputs it in note form',
    license="GPL-3.0",
    keywords=["json", "notes", "trello"],
    packages=['trellnotes'],
    scripts=['bin/trellnotes']
)
