# Copyright 2013 New Dream Network, LLC (DreamHost)
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import sys

from sqlalchemy_schemadisplay import create_uml_graph
from sqlalchemy.orm import class_mapper

def build_finished_handler(app, exception):
    app.info("Creating the db schema")
    skip_folders = ""
    if app.config.model_skip_folders:
        skip_folders = app.config.model_skip_folders.split(",")

    for root, directories, filenames in os.walk(os.getcwd()):
        for filename in filenames:
             folder = str(root)
             if not folder in skip_folders: continue
             if filename.endswith(".py"):
                 if filename.startswith("__") : continue
                 name = filename[:-3]
                 module = folder.replace("/", ".") + "." + name
                 try:
                     globals()[name] = __import__(module)
                 except:
                     pass

    str_model_cls = app.config.model_class_name
    if not str_model_cls: return
    model_class = getattr(sys.modules[str_model_cls[:str_model_cls.rfind(".")]],
                          str_model_cls[str_model_cls.rfind(".")+1:])
    
    mappers = []
    for cls in model_class.__subclasses__():
        for attr in cls.__dict__.keys():
            try:
                mappers.append(class_mapper(cls))
            except:
                pass

    graph = create_uml_graph(mappers,
        show_operations=False,
        show_multiplicity_one=False
    )
    graph.write_png(app.config.model_schema_filename)

def setup(app):
    app.add_config_value('model_class_name', '', 'html')
    app.add_config_value('model_schema_filename', 'db-schema.png', 'html')
    app.add_config_value('model_skip_folders', 'tests', 'html')
    app.connect('build-finished', build_finished_handler)
