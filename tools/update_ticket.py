"""
Tool to update an existing Zendesk ticket via manager.
"""
from mcp.types import TextContent
from ticket_manager import TicketManager

ticket_manager = TicketManager()

async def update_ticket(ticket_id: int, status: str, comment: str = "") -> list[TextContent]:
    """
    Update an existing Zendesk ticket.
    """
    result = ticket_manager.update_ticket(ticket_id, status, comment)

    if result.get("success"):
        ticket = result["data"]
        msg = (
            f"✅ SUCCESS: {result['message']}\n"
            f"Ticket ID: {ticket['id']}\n"
            f"Subject: {ticket['subject']}\n"
            f"Status: {ticket['status']}\n"
            f"Updated At: {ticket.get('updated_at', 'N/A')}"
        )
    else:
        msg = f"❌ ERROR: {result.get('error', 'Unknown error')}"
        if "details" in result:
            msg += "\n" + "\n".join(result["details"])

    return [TextContent(type="text", text=msg)]
