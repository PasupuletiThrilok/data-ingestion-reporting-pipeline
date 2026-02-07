def transform_weather_data(raw: dict):
    return {
        "city": raw["name"],
        "temperature": raw["main"]["temp"],
        "humidity": raw["main"]["humidity"],
        "condition": raw["weather"][0]["main"]
    }
