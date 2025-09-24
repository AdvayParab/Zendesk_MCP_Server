"""Ticket Manager: Handles create, update, and fetch logic for Zendesk tickets."""

from ticket_validator import TicketValidator
from utils.client import post, put, get_all


class TicketManager:
    """
    Manages Zendesk ticket operations including create, update, and fetch.
    """

    def __init__(self):
        """
        Initialize the TicketManager with a TicketValidator instance.
        """
        self.validator = TicketValidator()

    def create_ticket(
        self, employee_id: str, subject: str, description: str, priority: str = "normal"
    ) -> dict:
        """
        Create a new ticket in Zendesk.

        Args:
            employee_id (str): Requester's ID.
            subject (str): Ticket subject.
            description (str): Ticket description.
            priority (str, optional): Ticket priority (default "normal").

        Returns:
            dict: Contains success status, message, and ticket data if successful,
                  otherwise error details.
        """
        is_valid, errors = self.validator.validate_create(subject, description, priority)
        if not is_valid:
            return {
                "success": False, 
                "error": "Validation failed for create_ticket", 
                "details": errors
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
                "details": [str(response)]
                }

    def update_ticket(self, ticket_id: int, status: str, comment: str = "") -> dict:
        """
        Update an existing Zendesk ticket's status and optional comment.

        Args:
            ticket_id (int): ID of the ticket to update.
            status (str): New status for the ticket.
            comment (str, optional): Optional comment to add.

        Returns:
            dict: Contains success status, message, and updated ticket data if successful,
                  otherwise error details.
        """
        is_valid, errors = self.validator.validate_update(ticket_id, status, comment)
        if not is_valid:
            return {
                "success": False, 
                "error": "Validation failed for update_ticket", 
                "details": errors
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
                "details": [str(response)]
                }

    def get_ticket(self) -> dict:
        """
        Fetch all tickets from Zendesk using the paginated client helper.

        Returns:
            dict: Contains 'success' and 'data' keys.
                  'data' is a list of ticket dicts with id, subject, status, and priority.
        """
        return get_all("/api/v2/tickets.json")
