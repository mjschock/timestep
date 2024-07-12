#!/usr/bin/env python3

import sys
from ruamel.yaml import YAML

def set_yaml_indent(file_path):
    yaml = YAML()
    yaml.indent(mapping=4, offset=4, sequence=6)  # Adjust the offset to ensure proper indentation
    yaml.preserve_quotes = True
    
    # Read the YAML file
    with open(file_path, 'r') as file:
        data = yaml.load(file)
    
    # Write the YAML file with indent set to 4 spaces
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: set_yaml_indent.py <path_to_yaml_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    set_yaml_indent(file_path)
