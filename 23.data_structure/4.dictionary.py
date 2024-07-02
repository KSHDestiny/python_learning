states_to_capitals = {
    "Texas" : "Austin",
    "New York" : "Albany"
}

print(states_to_capitals["New York"])

for key, value in states_to_capitals.items():
    print(key + " | " + value)

user_preferences = {
    "language" : "English",
    "font_size" : "14px",
    "timezone" : "GMT",
    "currency" : "USD",
    "enable_location" : False,
    "volume_level" : 80,
    "date_format" : "MM/DD/YYYY"
}

user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50
user_preferences["highlight_color"] = "yellow"

del user_preferences["currency"]
user_preferences.pop("date_format", "N/A")

print(user_preferences) # {'language': 'Spanish', 'font_size': '14px', 'timezone': 'GMT', 'enable_location': False, 'volume_level': 50, 'highlight_color': 'yellow'}

dictionaries = {
    "timezone" : "GMT",
    "language" : "English",
    "notifications" : None,
    "currency" : "USD",
    "theme" : None
}

#! linear time complexity
# def update_dictionaries(dictionary):
#     update_dictionaries = {}
#     for key, value in dictionary.items():
#         if value is not None:
#             update_dictionaries[key] = value
#     return update_dictionaries

def update_dictionaries(dictionaries):
    return {key: value for key, value in dictionaries.items() if value is not None}

print(update_dictionaries(dictionaries))    # {'timezone': 'GMT', 'language': 'English', 'currency': 'USD'}