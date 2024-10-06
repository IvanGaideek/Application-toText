import json


def get_settings_for_splash():  # Path to the gif: main splash screen
    # Open and read the JSON (settings) file
    with open('Settings/cur_settings.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    path_gif = data["FOR_begin_splash"]["path_to_gif"]
    progressbar_value = data["FOR_begin_splash"]["progressbar_value"]
    return path_gif, progressbar_value


def get_data_settings():
    with open("Settings/cur_settings.json", "r") as file:
        data = json.load(file)
    return data


def get_data_default_settings():
    with open("Settings/default_settings.json", "r") as file:
        data = json.load(file)
    return data


def change_in_settings(data):
    with open("Settings/cur_settings.json", "w") as file:
        json.dump(data, file)
