# Restaurant Finder Application: Data Organization
## Overview
- The Restaurant Finder Application utilizes a tree data structure to organize and manage the information about restaurants. This hierarchical organization allows for efficient data retrieval and querying, enhancing the user experience by providing an intuitive way to filter and select restaurants based on various criteria.
## Tree Structure
- Root Node: The root of the tree is labeled 'Restaurants', representing the entire dataset of restaurant listings.
- Cuisine Nodes (First Level):
  - Directly under the root, the tree branches into various cuisine types, such as 'Italian', 'Chinese', 'Japanese', etc.
Each of these nodes represents a main category for filtering restaurants, allowing users to quickly narrow down their search based on their preferred cuisine.
Price Range Nodes (Second Level):

Under each cuisine node, there are further subdivisions based on price ranges: '$', '$$', and '$$$'.
This level allows users to refine their search based on their budget preferences within a selected cuisine.
Rating Nodes (Third Level):

The next level of the tree can be implemented to categorize restaurants based on ratings, such as '>= 4.5 Stars', '4.0 - 4.5 Stars', and '< 4.0 Stars'.
This classification helps users find highly-rated restaurants or explore less-known options.
Leaf Nodes:

The final leaves of the tree are the individual restaurants themselves.
Each leaf node contains detailed information about a specific restaurant, including its name, rating, price range, distance from downtown, and a link to its Yelp page.
