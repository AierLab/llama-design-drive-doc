from app.tool.gtfs.data_loader import GTFS_data
import googlemaps
import json

api_key = "YOUR_GOOGLE_MAPS_API_KEY"

def google_maps_navigation(start_longitude, start_latitude, destination_longitude, destination_latitude, api_key=api_key):
    """
    Utilizes the Google Maps API to return the full navigation path given the longitude and latitude of the start and destination points.
    
    Parameters:
    - start_longitude (float): The longitude of the starting point.
    - start_latitude (float): The latitude of the starting point.
    - end_longitude (float): The longitude of the destination point.
    - end_latitude (float): The latitude of the destination point.
    - api_key (str): The API key for accessing Google Maps services.
    
    Returns:
    - dict: The navigation path details.
    """
    gmaps = googlemaps.Client(key=api_key)
    
    # Request directions via driving mode
    directions_result = gmaps.directions(
        (start_latitude, start_longitude),
        (destination_latitude, destination_longitude),
        mode="driving"
    )
    
    if not directions_result:
        return {"error": "No route found"}
    
    # Extract the relevant information from the directions result
    route = directions_result[0]
    legs = route.get("legs", [])
    steps = []
    
    for leg in legs:
        for step in leg.get("steps", []):
            steps.append({
                "start_location": step["start_location"],
                "end_location": step["end_location"],
                "instructions": step["html_instructions"],
                "distance": step["distance"]["text"],
                "duration": step["duration"]["text"]
            })
    
    return {
        "start_location": {"lat": start_latitude, "lng": start_longitude},
        "end_location": {"lat": destination_latitude, "lng": destination_longitude},
        "steps": steps
    }

# Example usage
""" if __name__ == "__main__":
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    start_longitude = -122.084
    start_latitude = 37.422
    end_longitude = -122.084
    end_latitude = 37.422
    navigation_path = google_maps_navigation(start_longitude, start_latitude, end_longitude, end_latitude, api_key)
    print(json.dumps(navigation_path, indent=2)) """

