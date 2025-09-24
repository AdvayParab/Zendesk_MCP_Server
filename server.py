"""
This module runs the server.
It handles API requests and serves responses.
"""
from fastmcp import FastMCP
from tools.create_ticket import create_ticket
from tools.update_ticket import update_ticket
from tools.get_ticket import get_ticket

app = FastMCP("zendesk-server")

app.tool(description="Create a new Zendesk ticket")(create_ticket)
app.tool(description="Update an existing Zendesk ticket")(update_ticket)
app.tool(description="Get all ticket")(get_ticket)

if __name__ == "__main__":
    print("🚀 FastMCP Zendesk Server started at http://127.1.0.1:8000/mcp")
    app.run(
        transport="http",
        host="127.1.0.1",
        port=8000,
        path="/mcp"
    )
