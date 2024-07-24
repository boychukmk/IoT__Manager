from models import ApiUser, Location, Device, initialize_db

def populate_db():
    initialize_db()

    # Sample data
    locations = [
        {'name': 'Living Room'},
        {'name': 'Kitchen'}
    ]

    users = [
        {'name': 'Alice', 'email': 'alice@example.com', 'password': 'password123'},
        {'name': 'Bob', 'email': 'bob@example.com', 'password': 'password456'}
    ]

    devices = [
        {'name': 'Thermostat', 'type': 'Temperature', 'login': 'thermo1', 'password': 'thermo1pass', 'location_id': 1, 'api_user_id': 1},
        {'name': 'Light Bulb', 'type': 'Lighting', 'login': 'light1', 'password': 'light1pass', 'location_id': 2, 'api_user_id': 2},
        {'name': 'Security Camera', 'type': 'Camera', 'login': 'camera1', 'password': 'camera1pass', 'location_id': 1, 'api_user_id': 1}
    ]

    for loc in locations:
        Location.create(**loc)

    for user in users:
        ApiUser.create(**user)

    for device in devices:
        Device.create(**device)

    print("Database populated successfully.")

if __name__ == '__main__':
    populate_db()
