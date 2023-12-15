class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def get_rating_category(rating):
    if rating > 4.5:
        return ">4.5"
    elif 4.0 <= rating <= 4.5:
        return "4.0-4.5"
    else:
        return "<4.0"

def get_distance_category(distance):
    if distance < 500:
        return "<500m"
    elif 500 <= distance <= 1500:
        return "500-1500m"
    else:
        return ">1500m"

# Create root node
root = TreeNode("Restaurants")

# Create category nodes and price range nodes
category_nodes = {}
for category in yelp_data['main_category'].unique():
    category_node = TreeNode(category)
    root.add_child(category_node)
    category_nodes[category] = category_node

    # Subdivide by price range
    for price in yelp_data[yelp_data['main_category'] == category]['price'].unique():
        price_node = TreeNode(price)
        category_node.add_child(price_node)

        # Subdivide by rating category
        for rating_category in [">4.5", "4.0-4.5", "<4.0"]:
            rating_node = TreeNode(rating_category)
            price_node.add_child(rating_node)

            # Subdivide by distance category
            for distance_category in ["<500m", "500-1500m", ">1500m"]:
                distance_node = TreeNode(distance_category)
                rating_node.add_child(distance_node)

                # Add restaurants as children of the corresponding distance category
                for _, row in yelp_data[(yelp_data['main_category'] == category) & 
                                        (yelp_data['price'] == price) & 
                                        (get_rating_category(row['rating']) == rating_category)].iterrows():
                    if get_distance_category(row['distance']) == distance_category:
                        restaurant_node = TreeNode(row['name'])
                        distance_node.add_child(restaurant_node)