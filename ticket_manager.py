"""Ticket Manager: Handles create and update logic for Zendesk tickets."""

from ticket_validator import TicketValidator
from utils.client import post, put


class TicketManager:
    """
    Manages ticket operations with validation and API calls.
    """

    def __init__(self):
        self.validator = TicketValidator()

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
                "requester": {"ID": employee_id},
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

    def update_ticket(self, ticket_id: int, status: str, comment: str = "") -> dict:
        """
        Update an existing ticket in Zendesk.
        """
        is_valid, errors = self.validator.validate_update(ticket_id, status, comment)
        if not is_valid:
            return {
                "success": False,
                "error": "Validation failed for update_ticket",
                "details": errors,
            }

        payload = {
            "ticket": {
                "status": status.lower(),
            }
        }
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
