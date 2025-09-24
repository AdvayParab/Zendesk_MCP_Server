# Zendesk MCP Server

A simple MCP server for creating and updating Zendesk tickets.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```plaintext

### 2. Configure Environment
Create a `.env` file with your Zendesk credentials:

```plaintext
ZENDESK_SUBDOMAIN=your-company-name
ZENDESK_EMAIL=your-email@company.com
ZENDESK_API_TOKEN=your-api-token
```plaintext


### 3. Get Your Zendesk API Token
1. Go to your Zendesk Admin Centre
2. Navigate to Apps and integrations > Zendesk API
3. Enable token access and generate a new API token
4. Copy the token to your `.env` file

### 4. Run the Server
```bash
python main.py
```plaintext


### Testing

Use the MCP Inspector to test your tools:

```bash
 npx @modelcontextprotocol/inspector 
```

### create_ticket

Create a new support ticket.

**Parameters:**

- `subject` (required): Ticket title
- `description` (required): Detailed description
- `priority` (optional): low, normal, high, urgent (default: normal)

**Example:**

```json
{
  "subject": "Printer not working",
  "description": "The office printer is showing error code E001",
  "priority": "high"
}
```

### update_ticket

Update an existing ticket.

**Parameters:**

- `ticket_id` (required): ID of the ticket to update
- `status` (optional): new, open, pending, hold, solved, closed
- `priority` (optional): low, normal, high, urgent
- `comment` (optional): Add a comment to the ticket

**Example:**

```json
{
  "ticket_id": 12345,
  "status": "solved",
  "comment": "Issue resolved by restarting the printer"
}
```

## File Structure

```plaintext
zendesk-mcp-server/
├── main.py                    # MCP server entry point
├── config.py                  # Configuration management
├── utils
|    -client.py                 # API client
|    -__init__.py
├──tools
|    -__init_.py
|    -create_ticket_tool.py      # Create ticket tool
|    -update_ticket_tool.py      # Update ticket tool
|    -get_ticket.py              # get the ticket tool
├── requirements.txt           # Dependencies
├── .env                       # Environment variables
└── README.md                 # This file
```

