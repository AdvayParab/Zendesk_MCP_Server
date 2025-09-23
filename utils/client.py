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
