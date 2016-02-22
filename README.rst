==============================
Schemadisplay Sphinx Extension
==============================

.. image:: https://img.shields.io/pypi/v/schemadisplay-sphinx.svg
       :target: https://pypi.python.org/pypi/schemadisplay-sphinx/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/schemadisplay-sphinx.svg
       :target: https://pypi.python.org/pypi/schemadisplay-sphinx/
    :alt: Downloads

This extension creates the Entitiy Relationship Diagram(ERD) of the
project in an image file.  The idea is that Database information
documentation keeps syncronized with the source code.

Configuration
-------------

    1. Add `schemadisplay_sphinx` module in sphinx entensions array.
    2. Define the `model_class_name` class.
    3. Specify the image path for the output in `model_schema_filename`.
    4. List folders to be ignored for the schema creation using `model_skip_folders`.

* Free software: Apache License, Version 2.0
