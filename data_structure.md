# Graph Structure for Yelp Data

## Overview
This project uses NetworkX to create a graph structure from Yelp data. The graph represents restaurants as nodes and connects them through edges based on shared categories.

## Structure
- Graph Creation: Constructs the graph using Yelp data.
- JSON Serialization: Converts the graph into a JSON format.
- JSON Reader: A standalone Python script to read and process the graph from the JSON file.

## Usage
### Setup
- Ensure you have NetworkX installed: `pip install networkx`

### Creating the Graph
- Run `create_graph.py` to construct the graph from Yelp data.

### Exporting to JSON
- Run `export_json.py` to serialize the graph into a JSON file.

### Reading from JSON
- Use `read_json.py` to load and process the graph from the JSON file.
