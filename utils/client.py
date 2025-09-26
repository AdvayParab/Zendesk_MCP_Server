"""
Client utility functions to interact with the Zendesk API.
Supports GET, POST, PUT, DELETE requests and pagination.
"""

import requests
from config import BASE_URL, AUTH


# ---------- GET ----------
def get(endpoint: str) -> dict:
    """
    Send a GET request to Zendesk API.
    """
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, auth=AUTH, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ---------- POST ----------
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


# ---------- PUT ----------
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


# ---------- DELETE ----------
def delete(endpoint: str) -> dict:
    """
    Send a DELETE request to Zendesk API.
    """
    url = BASE_URL + endpoint
    try:
        response = requests.delete(url, auth=AUTH, timeout=10)
        response.raise_for_status()
        # Zendesk delete returns empty {} on success
        return response.json() if response.text else {}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ---------- PAGINATION (fetch all pages) ----------
def get_all(endpoint: str) -> dict:
    """
    Fetch all results from a paginated Zendesk API endpoint.
    """
    url = BASE_URL + endpoint
    all_data = []

    try:
        while url:
            response = requests.get(url, auth=AUTH, timeout=10)
            response.raise_for_status()
            data = response.json()

            # merge results
            if "tickets" in data:
                all_data.extend(data["tickets"])
            elif "users" in data:
                all_data.extend(data["users"])
            elif "results" in data:
                all_data.extend(data["results"])

            # move to next page if available
            url = data.get("next_page")

        return {"success": True, "data": all_data}

    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}
