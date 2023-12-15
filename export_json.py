## export_tree_json.py - json file to serialize the trees
import json

def serialize_tree(node):
    tree_dict = {"name": node.name, "children": [serialize_tree(child) for child in node.children]}
    return tree_dict

# Assuming 'root' is your tree root
tree_data = serialize_tree(root)
with open('tree.json', 'w') as f:
    json.dump(tree_data, f, indent=4)