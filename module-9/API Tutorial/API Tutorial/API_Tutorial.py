# Noah McCarthy, 2/28/2025, Module 9.2 Assignment
#Project goal is practice using API'S
import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():

    response = requests.get("http://api.open-notify.org/astros")
    print(response.status_code)
    print(response.json())
    jprint(response.json())


    response = requests.get("https://api-server.dataquest.io/economic_data/countries")

    # Some APIs return JSON as a string that needs extra parsing
    data = json.loads(response.json())
    print(f"Total countries: {len(data)}")
    print(f"First country: {data[0]['short_name']}")
    
    #Using a query parameter
    params = {
    'filter_by': 'region=Sub-Saharan Africa'
    }

    response = requests.get(
        "https://api-server.dataquest.io/economic_data/countries",
        params=params
    )
    data = json.loads(response.json())
    print(f"Filtered countries: {len(data)}")
    print(f"First country: {data[0]['short_name']}")





#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()
