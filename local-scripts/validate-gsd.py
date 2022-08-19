#!/usr/bin/env python3

import sys
import json
import jsonschema
from jsonschema import validate

# Read the json file into memory and close it
# Validate it
# Print results

file = sys.argv[1]
with open(file, "r") as f:
    gsd_file_data = json.load(f)
    f.close()

OSV_file_data = gsd_file_data["OSV"]

# https://github.com/ossf/osv-schema/blob/main/validation/schema.json
# copied locally as osv-schema.json
with open('osv-schema.json') as osvschema_file:
    osvschema = json.load(osvschema_file)


def validateJson(data):
    try:
        validate(instance=data, schema=osvschema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True


# validate it
isValid = validateJson(OSV_file_data)
if isValid:
#    print(OSV_file_data)
    print("Given JSON data is Valid")
else:
#    print(OSV_file_data)
    print("Given JSON data is InValid")
