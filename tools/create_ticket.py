"""
Tool to create a new Zendesk ticket via manager.
"""
from mcp.types import TextContent
from ticket_manager import TicketManager

ticket_manager = TicketManager()
async def create_ticket(
    employee_id: str,
    subject: str,
    description: str,
    priority: str
) -> list[TextContent]:
    """
    Create a new Zendesk ticket.
    """
    result = ticket_manager.create_ticket(employee_id, subject, description, priority)

    if result.get("success"):
        ticket = result["data"]
        msg = (
            f"✅ SUCCESS: {result['message']}\n"
            f"Employee ID: {employee_id}\n"
            f"Ticket ID: {ticket['id']}\n"
            f"Subject: {ticket['subject']}\n"
            f"Status: {ticket['status']}\n"
            f"Priority: {ticket.get('priority', 'not set')}"
        )
    else:
        msg = f"❌ ERROR: {result.get('error', 'Unknown error')}"
        if "details" in result:
            msg += "\n" + "\n".join(result["details"])

    return [TextContent(type="text", text=msg)]
