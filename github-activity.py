# Description: This script will get the latest activity of a user on GitHub
# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/larisabarabas/events

import requests
import json

pushEventsCount = 0
createEventsCount = 0
reposCount = 0

response = requests.get("https://api.github.com/users/larisabarabas/events")
data = response.json()
print(f'Data length: {len(data)}')

print("Repos:")
for index, element in enumerate(data):
    if element['type'] == 'PushEvent':
        pushEventsCount += 1
    elif element['type'] == 'CreateEvent':
        createEventsCount += 1
    
    if index > 0 and data[index - 1]["repo"]['name'] == element["repo"]['name']:
        continue
    reposCount += 1
    print(f'{reposCount}. {element["repo"]['name']}')

print("Activity:")
print(f'Pushed {pushEventsCount} commits in total')
print(f'Created {createEventsCount} repositories')





