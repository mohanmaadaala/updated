import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define a list of cities (nodes)
cities = ["New York", "London", "Tokyo", "Paris", "Dubai", "Sydney"]

# Create an adjacency matrix representing direct flights between cities
adjacency_matrix = np.array([
    [0, 1, 1, 1, 0, 1],  # New York has direct flights to London, Tokyo, Paris, and Sydney
    [1, 0, 1, 1, 1, 0],  # London has direct flights to New York, Tokyo, Paris, and Dubai
    [1, 1, 0, 0, 0, 1],  # Tokyo has direct flights to New York, London, Dubai, and Sydney
    [1, 1, 0, 0, 1, 0],  # Paris has direct flights to New York, London, and Dubai
    [0, 1, 1, 1, 0, 0],  # Dubai has direct flights to London, Tokyo, Paris, and Sydney
    [1, 0, 0, 0, 1, 0]   # Sydney has direct flights to New York, Tokyo, and Dubai
])

# Create a directed graph from the adjacency matrix
G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)

# Set node labels to city names
G = nx.relabel_nodes(G, dict(enumerate(cities)))

# Calculate the eigenvector centrality (similar to PageRank)
eigen_centrality = nx.eigenvector_centrality_numpy(G)

# Define thresholds for different importance levels (for example: low, medium, high)
high_threshold = 0.4
medium_threshold = 0.2

# Assign different shapes (symbols), sizes, and colors based on the centrality scores
node_shapes = {}
for city, score in eigen_centrality.items():
    if score >= high_threshold:
        node_shapes[city] = {"shape": "s", "size": 1500, "color": "red", "importance": "High"}  # Square for high importance
    elif score >= medium_threshold:
        node_shapes[city] = {"shape": "o", "size": 1000, "color": "orange", "importance": "Medium"}  # Circle for medium importance
    else:
        node_shapes[city] = {"shape": "v", "size": 2000, "color": "blue", "importance": "Low"}  # Triangle for low importance

# Set up the graph layout
pos = nx.spring_layout(G)

# Draw nodes with different symbols based on their importance
for shape in set(d["shape"] for d in node_shapes.values()):
    nodes_with_shape = [city for city, attr in node_shapes.items() if attr["shape"] == shape]
    nx.draw_networkx_nodes(
        G, pos, nodelist=nodes_with_shape,
        node_shape=shape, node_color=[node_shapes[city]["color"] for city in nodes_with_shape],
        node_size=[node_shapes[city]["size"] for city in nodes_with_shape], alpha=0.8
    )

# Draw edges (flights between cities)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15, edge_color="gray")

# Add labels for each city
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# Display the title and the plot
plt.title("Travel Network: City Connections and Importance Based on Eigenvector Centrality")
plt.show()

# Print city rankings and visual attributes (with proper indication of shapes and colors)
print("City Rankings and Visual Indicators Based on Travel Connectivity (Eigenvector Centrality):")
for city, attr in node_shapes.items():
    print(f"{city}: {attr['importance']} importance, Shape: {attr['shape']}, Color: {attr['color']}")

