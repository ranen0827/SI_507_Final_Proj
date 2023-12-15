## Standalone Python File for Reading JSON
import json

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
def deserialize_tree(data):
    node = TreeNode(data['name'])
    for child_data in data.get('children', []):
        child_node = deserialize_tree(child_data)
        node.add_child(child_node)
    return node

with open('tree.json', 'r') as f:
    tree_data = json.load(f)
    root = deserialize_tree(tree_data)
