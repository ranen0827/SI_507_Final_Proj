# README for Restaurant Finder Flask Application
## Name: `Shushun Ren`, UM-ID: `24284779`, email: `shushunr@umich.edu`
This is the folder for the final project of SI 507 (Fall 2023) course

## Overview
This Flask application helps users find restaurants based on **cuisine, price range, rating, and distance** from a specified location. It uses a tree data structure to organize and navigate through restaurant data.

## Requirements
### Python Version
- Python 3.x

### Required Python Packages
#### Built-in Packages
- Json (for loading and handling data)
- os
#### Non Built-in Packages
- flask
- requests
- urlparse, parse_qs (from urllib.parse)

## Setup and Installation
1. **Clone/Download the repository**: Make sure you have the complete project files, including the Python scripts and the `templates` folder.
2. **Install dependencies**: If Flask is not installed, run the following command:
```python
pip install Flask
```
3. **Prepare data**: Ensure you have a JSON file (e.g., `tree.json`) with the restaurant data structured as a tree. The tree should be built according to the specifications of the `TreeNode` class and should categorize restaurants by cuisine, price, rating, and distance.

## Data Structure
**Note!** - For tree **data structure**, please refer to the `data_structure.md` file, which fully explained how data is organized into data structure.
- `read_json.py`, `export_json.py`, `create_tree.py` and `tree.json` are provided that demonstrate organization of data into data structures, where:
  - `create_tree.py` is a python file that constructs your graphs or trees from your stored data using classes, note you should replace `combined_df` with the final dataframe (ready to create a tree with) before running the code.
  - `export_json.py` is json file to serialize the trees.
  - `tree.json` is a json file with the trees data structure.
  - `read_json.py` is a stand alone python file that reads the json of your graphs or trees.
- The `Final_project.ipynb` file combines those files together in different chunks. Feel free to do the above steps within this file.
 
## Running the Application
1. **Start the Flask server**: Navigate to the directory containing the `app.py` file in the command line and run the command:
```python
python app.py
```
2. **Accessing the application**: After running app.py, there will be a link `http://127.0.0.1:5000`. Clicking that link will load the main page of the application.

## Interacting with the program
1. **Making selections**: On the main page, you will be presented with a series of options, starting with cuisine types. Select your preference to proceed to the next set of options (price range, rating, and distance).
2. **Navigating through choices**: Continue selecting options at each level. After each choice, the application will present the next relevant set of options based on the tree structure.
3. **Viewing recommendations**: Once you've made selections at all levels, click "Search", the application will display a list of restaurant recommendations that match your criteria.
4. **Restarting or Changing Criteria**: To start over or change your criteria, simply navigate back to the home page (`http://127.0.0.1:5000`). Note that you are free to select one or more criteria based on your needs. **Remember to click `Search` after selecting your criteria of interest.**

## Special Instructions
- If the application relies on external APIs or data sources, ensure you have the necessary API keys or data files in place as required by your implementation.
- The tree data structure must be correctly set up in the `tree.json` file for the application to function properly.

## Troubleshooting
- If you encounter errors related to missing templates, verify that the templates folder is in the same directory as `app.py` and contains `template.html`
- For issues related to data, ensure that the JSON file is correctly formatted and accessible to the Flask application.

For further assistance or bug reports, feel free to contact `shushunr@umich.edu`.
