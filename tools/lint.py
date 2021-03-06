#!/usr/bin/env python
# Does google-lint on c++ files and ts-lint on typescript files

import os
from util import run

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
third_party_path = os.path.join(root_path, "third_party")
cpplint = os.path.join(third_party_path, "cpplint", "cpplint.py")
tslint = os.path.join(third_party_path, "node_modules", "tslint", "bin",
                      "tslint")

os.chdir(root_path)
run([
    "python", cpplint, "--filter=-build/include_subdir", "--repository=src",
    "--extensions=cc,h", "--recursive", "src/."
])
run(["node", tslint, "-p", ".", "--exclude", "**/gen/**/*.ts"])
