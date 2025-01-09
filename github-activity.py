# Description: This script will get the latest activity of a user on GitHub
# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/larisabarabas/events
# CreateEvent -- payload -> ref_type: branch | tag | repository
# PushEvent == commits

import requests
import json
import argparse



def create_parser():
    parser = argparse.ArgumentParser(description='GitHub Activity')
    parser.add_argument('-u', "--user", metavar="", help="GitHub username")
    return parser

def get_user_activity(username):
    response = requests.get(f'https://api.github.com/users/{username}/events')
    data = response.json()
    print("\n")
    print("Activity of the latest repositories:")

    pushEventsCount = 0
    createEventsCount = 0
    branchCreateEventsCount = 0
    repositoryCreateEventsCount = 0
    tagsCreateEventsCount = 0
    reposCount = 0

    for index, element in enumerate(data):
        if element['type'] == 'PushEvent':
            pushEventsCount += 1
        elif element['type'] == 'CreateEvent' and element['payload']['ref_type'] == 'repository':
            createEventsCount += 1
            repositoryCreateEventsCount += 1
        elif element['type'] == 'CreateEvent' and element['payload']['ref_type'] == 'branch':
            createEventsCount += 1
            branchCreateEventsCount += 1
        elif element['type'] == 'CreateEvent' and element['payload']['ref_type'] == 'tag':
            createEventsCount += 1
            tagsCreateEventsCount += 1
        
        if index > 0 and data[index - 1]["repo"]['name'] == element["repo"]['name']:
            continue
        reposCount += 1
        print(f'{reposCount}. {element["repo"]['name']}')

    print("\n")
    print("Activity:")
    print(f'Pushed {pushEventsCount} commits in total')
    print(f'Created {repositoryCreateEventsCount} repositories')
    print(f'Created {branchCreateEventsCount} branches')
    print(f'Created {tagsCreateEventsCount} tags')
    print(f'CreateEvents count: {createEventsCount}')
    print(f'Total events: {len(data)}')

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.user:
        get_user_activity(args.user)
    else:
        print("Please provide a github username")

if __name__ == "__main__":  
    main()



