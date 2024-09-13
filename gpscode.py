import gps3

# Create a GPS object
track= gps3.GPS()

# Initialize the GPS
track.stream()

# Loop indefinitely to track GPS data
while True:
    # Get the latest GPS data
    info = track`````````````````````````````````````````````````````````````````````````````````````````````.next()

    # Extract relevant data
    latitude = info.lat
    longitude = info.lon
    altitude = info.alt
    speed = info.speed
    timestamp = info.time

    # Print the GPS data
    print(f"Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude}, Speed: {speed}, Timestamp: {timestamp}")
