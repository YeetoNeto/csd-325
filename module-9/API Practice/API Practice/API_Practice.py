# Noah McCarthy, 2/28/2025, Module 9.2 Assignment
#Project goal is practice using API'S
import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():
    response = requests.get("https://www.dnd5eapi.co/api/2014")
    print(response.status_code)
    print('\n\n\n\n')
    print(response.json())
    jprint(response.json())

    response = requests.get("https://www.dnd5eapi.co/api/2014/classes")
    jprint(response.json())

    response = requests.get("https://www.dnd5eapi.co/api/2014/classes/wizard") 
    jprint(response.json())
    

#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()

