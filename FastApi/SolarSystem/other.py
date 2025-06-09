
help_text = {
    "endpoints": {
        "/planets": "List all available planet names.",
        "/planets/{name}": "Retrieve all available data about a specific planet.",
        "/planets/{name}/{attribute}": "Retrieve a specific attribute (e.g., 'moons', 'temperature_c', 'diameter_km') for a specific planet.",
        "/help": "Show usage instructions and endpoint descriptions."
    },
    "example_usage": {
        "List all planets": "/planets",
        "Details for Earth": "/planets/earth",
        "Number of moons on Mars": "/planets/mars/moons",
        "Surface temperature of Venus": "/planets/venus/temperature_c"
    }
}

about_text = {
    "copyright": {
        "name": "Solar System API",
        "date": "2025",
        "owner": "Paul Pritchard"
    }
}
