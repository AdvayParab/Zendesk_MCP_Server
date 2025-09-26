"""Ticket Manager: Handles create, update, fetch, and other Zendesk ticket operations."""

from ticket_validator import TicketValidator
from utils.client import (
    post,
    put,
    get_all,
    delete,
    get,
)  # make sure you have delete + get in client.py


class TicketManager:
    """
    Manages Zendesk ticket operations including create, update, delete, assign, search, and fetch.
    """

    def __init__(self):
        """
        Initialize the TicketManager with a TicketValidator instance.
        """
        self.validator = TicketValidator()

    # ---------------- CREATE ----------------
    def create_ticket(
        self, employee_id: str, subject: str, description: str, priority: str = "normal"
    ) -> dict:
        """
        Create a new ticket in Zendesk.
        """
        is_valid, errors = self.validator.validate_create(
            subject, description, priority
        )
        if not is_valid:
            return {
                "success": False,
                "error": "Validation failed for create_ticket",
                "details": errors,
            }

        payload = {
            "ticket": {
                "requester": {"email": employee_id},
                "subject": subject,
                "comment": {"body": description},
                "priority": priority.lower(),
            }
        }

        response = post("/api/v2/tickets.json", payload)
        if response.get("ticket"):
            return {
                "success": True,
                "message": "Ticket created successfully",
                "data": {
                    "id": response["ticket"]["id"],
                    "subject": response["ticket"]["subject"],
                    "status": response["ticket"]["status"],
                    "priority": response["ticket"].get("priority"),
                },
            }
        else:
            return {
                "success": False,
                "error": "Failed to create ticket",
                "details": [str(response)],
            }

    # ---------------- UPDATE ----------------
    def update_ticket(self, ticket_id: int, status: str, comment: str = "") -> dict:
        """
        Update an existing Zendesk ticket's status and optional comment.
        """
        is_valid, errors = self.validator.validate_update(ticket_id, status, comment)
        if not is_valid:
            return {
                "success": False,
                "error": "Validation failed for update_ticket",
                "details": errors,
            }

        payload = {"ticket": {"status": status.lower()}}
        if comment:
            payload["ticket"]["comment"] = {"body": comment}

        response = put(f"/api/v2/tickets/{ticket_id}.json", payload)
        if response.get("ticket"):
            return {
                "success": True,
                "message": "Ticket updated successfully",
                "data": {
                    "id": response["ticket"]["id"],
                    "subject": response["ticket"]["subject"],
                    "status": response["ticket"]["status"],
                    "updated_at": response["ticket"].get("updated_at"),
                },
            }
        else:
            return {
                "success": False,
                "error": "Failed to update ticket",
                "details": [str(response)],
            }

    # ---------------- FETCH ALL ----------------
    def get_ticket(self) -> dict:
        """
        Fetch all tickets from Zendesk.
        """
        return get_all("/api/v2/tickets.json")

    # ---------------- FETCH ONE ----------------
    def get_ticket_by_id(self, ticket_id: int) -> dict:
        """
        Fetch a single ticket by ID.
        """
        response = get(f"/api/v2/tickets/{ticket_id}.json")
        if response.get("ticket"):
            return {"success": True, "ticket": response["ticket"]}
        return {
            "success": False,
            "error": "Ticket not found",
            "details": [str(response)],
        }

    # ---------------- DELETE ----------------
    def delete_ticket(self, ticket_id: int) -> dict:
        """
        Delete a ticket by ID.
        """
        response = delete(f"/api/v2/tickets/{ticket_id}.json")
        if response == {}:
            return {
                "success": True,
                "message": f"Ticket {ticket_id} deleted successfully",
            }
        return {
            "success": False,
            "error": "Failed to delete ticket",
            "details": [str(response)],
        }

    # ---------------- SEARCH ----------------
    def search_ticket(self, query: str) -> dict:
        """
        Search tickets by keyword, requester, or status.
        """
        response = get(f"/api/v2/search.json?query=type:ticket {query}")
        if response.get("results"):
            return {"success": True, "tickets": response["results"]}
        return {
            "success": False,
            "error": "No tickets found",
            "details": [str(response)],
        }

    # ---------------- LIST USERS ----------------
    def list_users(self) -> dict:
        """
        Fetch all users in Zendesk.
        """
        response = get_all("/api/v2/users.json")
        if response.get("users"):
            return {"success": True, "users": response["users"]}
        return {"success": False, "error": "No users found", "details": [str(response)]}

    # ---------------- ADD COMMENT ----------------
    def add_comment(self, ticket_id: int, comment: str, public: bool = True) -> dict:
        """
        Add a comment to a ticket.
        """
        payload = {"ticket": {"comment": {"body": comment, "public": public}}}
        response = put(f"/api/v2/tickets/{ticket_id}.json", payload)
        if response.get("ticket"):
            return {
                "success": True,
                "message": "Comment added successfully",
                "ticket": response["ticket"],
            }
        return {
            "success": False,
            "error": "Failed to add comment",
            "details": [str(response)],
        }
