"""
Module for validating Zendesk tickets.
Contains functions to check ticket data and enforce rules.
"""


class TicketValidator:
    """
    This module contains functions to validate tickets from Zendesk.
    """

    VALID_PRIORITIES = ["low", "normal", "high", "urgent"]
    VALID_STATUSES = ["new", "open", "pending", "hold", "solved", "closed"]

    @staticmethod
    def validate_employee_id(employee_id: str) -> tuple[bool, str]:
        """
        Validate the employee ID.
        """
        if not employee_id or len(employee_id.strip()) < 6:
            return False, "✗ Invalid employee ID. It must be 6 characters long."
        return True, "✓ Valid"

    @staticmethod
    def validate_subject(subject: str) -> tuple[bool, str]:
        """
        Validate the subject of a ticket.
        """
        if not subject or len(subject.strip()) < 5:
            return False, "✗ dont be too specific, explain more!"
        if len(subject.strip()) > 150:
            return False, "✗ Whoa, stop complaining, make it shorter!"
        return True, "✓ Valid"

    @staticmethod
    def validate_description(description: str) -> tuple[bool, str]:
        """
        Validate the description of a ticket.
        """
        if not description or len(description.strip()) < 10:
            return False, "✗ Explain more, what am I god ?"
        return True, "✓ Valid"

    @staticmethod
    def validate_priority(priority: str) -> tuple[bool, str]:
        """
        Validate the priority of a ticket.
        """
        if priority.lower() not in TicketValidator.VALID_PRIORITIES:
            return (
                False,
                f"✗Invalid priority. What’s next — ‘super-ultra-mega-urgent’? Stick to "
                f"{TicketValidator.VALID_PRIORITIES}",
            )
        return True, "✓ Valid"

    @staticmethod
    def validate_ticket_id(ticket_id: int) -> tuple[bool, str]:
        """
        Validate the ticket ID.
        """
        if not isinstance(ticket_id, int) or ticket_id <= 0:
            return False, "✗ stop being negative, provide a valid ticket ID!"
        return True, "✓ Valid"

    @staticmethod
    def validate_status(status: str) -> tuple[bool, str]:
        """
        Validate the status of a ticket.
        """
        if status.lower() not in TicketValidator.VALID_STATUSES:
            return (
                False,
                f"✗ Nice try, but that status does not exist in Zendesk’s universe. "
                f"Stick to the real ones: {TicketValidator.VALID_STATUSES}.",
            )
        return True, "✓ Valid"

    @staticmethod
    def validate_create(
        subject: str, description: str, priority: str
    ) -> tuple[bool, list[str]]:
        """
        Validate inputs for creating a ticket.
        """
        errors = []
        for valid, msg in [
            TicketValidator.validate_subject(subject),
            TicketValidator.validate_description(description),
            TicketValidator.validate_priority(priority),
        ]:
            if not valid:
                errors.append(msg)

        return (len(errors) == 0, errors)

    @staticmethod
    def validate_update(
        ticket_id: int, status: str, comment: str
    ) -> tuple[bool, list[str]]:
        """
        Validate inputs for updating a ticket.
        """
        errors = []
        for valid, msg in [
            TicketValidator.validate_ticket_id(ticket_id),
            TicketValidator.validate_status(status),
        ]:
            if not valid:
                errors.append(msg)

        if comment and len(comment.strip()) < 3:
            errors.append(
                "✗ That is not a comment, that is a sneeze. "
                "Give me something with actual details!"
            )
        return (len(errors) == 0, errors)
