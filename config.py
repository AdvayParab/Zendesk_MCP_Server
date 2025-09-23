"""Configuration for Zendesk MCP server."""

import os
from dotenv import load_dotenv

load_dotenv()

ZENDESK_SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
ZENDESK_EMAIL = os.getenv("ZENDESK_EMAIL")
ZENDESK_API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

BASE_URL = f"https://{ZENDESK_SUBDOMAIN}.zendesk.com"

AUTH = (f"{ZENDESK_EMAIL}/token", ZENDESK_API_TOKEN)
if not all([ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, ZENDESK_API_TOKEN]):
    raise ValueError("Missing one or more Zendesk configuration values in .env")
