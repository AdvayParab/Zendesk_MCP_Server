"""Zendesk API client wrapper."""

import requests
from config import BASE_URL, AUTH


def post(endpoint: str, payload: dict) -> dict:
    """
    Send a POST request to Zendesk API.
    """
    url = BASE_URL + endpoint
    try:
        response = requests.post(url, json=payload, auth=AUTH, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def put(endpoint: str, payload: dict) -> dict:
    """
    Send a PUT request to Zendesk API.
    """
    url = BASE_URL + endpoint
    try:
        response = requests.put(url, json=payload, auth=AUTH, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get(endpoint: str) -> dict:
    """
    Send a GET request to Zendesk API.
    Returns the JSON response.
    """
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, auth=AUTH, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_all(endpoint: str) -> dict:
    """
    Fetch all results for a paginated GET endpoint.
    Returns a dict with 'success' and 'data' keys.
    """
    results = []
    next_endpoint = endpoint

    while next_endpoint:
        data = get(next_endpoint)
        if "error" in data:
            return {"success": False, "error": data["error"]}

        if not isinstance(data, dict) or "tickets" not in data:
            return {"success": False, "error": "Invalid response", "details": [str(data)]}

        results.extend(data["tickets"])

        next_endpoint = data.get("next_page")
        if next_endpoint and next_endpoint.startswith(BASE_URL):
            next_endpoint = next_endpoint.replace(BASE_URL, "")

    return {"success": True, "data": results}
