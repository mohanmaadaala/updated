import networkx as nx
import pandas as pd

# Sample dataset from the generated data
flight_data = [
    ["AirBlue", "New York", "Los Angeles", "Direct"],
    ["SkyWays", "Los Angeles", "Miami", "One Stop"],
    ["JetLine", "Chicago", "Seattle", "Direct"],
    ["GlobalAir", "Miami", "Boston", "Direct"],
    ["AirBlue", "Boston", "Denver", "One Stop"],
    ["JetLine", "San Francisco", "Houston", "Direct"],
    ["SkyWays", "Dallas", "Atlanta", "One Stop"],
    ["GlobalAir", "Seattle", "New York", "Direct"],
    ["AirFlyer", "Atlanta", "Orlando", "Direct"],
    ["JetFly", "Denver", "Philadelphia", "One Stop"],
    # Add more rows if necessary
]

# Create a DataFrame
flights_df = pd.DataFrame(flight_data, columns=["Flight Company", "Departure City", "Arrival City", "Type of Flight"])

# Create a directed graph to represent the cities and their connections
G = nx.DiGraph()

# Add nodes and edges (direct and one-stop flights)
for index, row in flights_df.iterrows():
    dep_city = row['Departure City']
    arr_city = row['Arrival City']
    flight_type = row['Type of Flight']

    # Add edge with weight 0 for direct flights and 1 for one-stop flights
    if flight_type == "Direct":
        G.add_edge(dep_city, arr_city, stops=0, flight_company=row['Flight Company'])
    else:
        G.add_edge(dep_city, arr_city, stops=1, flight_company=row['Flight Company'])

# Function to find the best route with the fewest stops
def find_best_route(G, source, target):
    try:
        # Use BFS to find the shortest path based on the number of stops
        shortest_path = nx.shortest_path(G, source=source, target=target, weight='stops')
        # Gather information about the flights in the path
        route_info = []
        for i in range(len(shortest_path) - 1):
            flight_company = G[shortest_path[i]][shortest_path[i + 1]]['flight_company']
            stops = G[shortest_path[i]][shortest_path[i + 1]]['stops']
            route_info.append(f"Flight by {flight_company} from {shortest_path[i]} to {shortest_path[i + 1]} (Stops: {stops})")
        return shortest_path, route_info
    except nx.NetworkXNoPath:
        return None, []

# User input for source and target cities
source_city = input("Enter the departure city: ")
target_city = input("Enter the destination city: ")

# Find the best route
best_route, route_details = find_best_route(G, source_city, target_city)

# Output the result
if best_route:
    print(f"\nThe best route from {source_city} to {target_city} is: {' -> '.join(best_route)}\n")
    print("Route details:")
    for detail in route_details:
        print(detail)
else:
    print(f"No route found from {source_city} to {target_city}.")
