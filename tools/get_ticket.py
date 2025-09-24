"""Tool to fetch all Zendesk tickets via manager."""

from mcp.types import TextContent
from ticket_manager import TicketManager

ticket_manager = TicketManager()


async def get_ticket() -> list[TextContent]:
    """
    Fetch all tickets from Zendesk.
    """
    result = ticket_manager.get_ticket()

    if "error" in result:
        msg = f"❌ ERROR: Failed to fetch tickets\n{result['error']}"
    else:
        tickets = result.get("data", [])
        if not tickets:
            msg = "ℹ️ No tickets found in Zendesk."
        else:
            msg_lines = ["✅ SUCCESS: Tickets fetched successfully", ""]
            for t in tickets[:100]:
                msg_lines.append(
                    f"ID: {t['id']}, Subject: {t['subject']}, "
                    f"Status: {t['status']}, Priority: {t.get('priority', 'N/A')}"
                )
            msg = "\n".join(msg_lines)

    return [TextContent(type="text", text=msg)]
