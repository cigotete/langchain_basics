import os
import requests


def scrape_gutendex(page: int, limit: int):
    # Fetch the JSON data from the external resource
    response = requests.get("https://gutendex.com/books/?page=" + str(page))
    data = response.json()

    # Extract values from the "results" key
    results = data["results"]

    # Extract desired values for each result
    parsed_results = []
    for result in results[:limit]:
        parsed_result = {
            "id": result["id"],
            "title": result["title"],
            "authors": [author["name"] for author in result["authors"]],
            "subjects": result["subjects"]
        }
        parsed_results.append(parsed_result)

    # Print the parsed results
    return parsed_results
