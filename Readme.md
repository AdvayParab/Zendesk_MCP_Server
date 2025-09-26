# Zendesk MCP Server

A comprehensive MCP server for managing Zendesk tickets with multiple tools and operations.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file with your Zendesk credentials:
```bash
ZENDESK_SUBDOMAIN=your-company-name
ZENDESK_EMAIL=your-email@company.com
ZENDESK_API_TOKEN=your-api-token
```

### 3. Get Your Zendesk API Token
1. Go to your **Zendesk Admin Centre**
2. Navigate to **Apps and integrations** → **Zendesk API**
3. Enable **token access** and generate a new API token
4. Copy the token to your `.env` file

### 4. Run the Server
```bash
python main.py
```

## 🧪 Testing
Use the MCP Inspector to test your tools:
```bash
npx @modelcontextprotocol/inspector 
```

## 🛠️ Available Tools

### **create_ticket**
Create a new support ticket.

**Parameters:**
- `subject` (required): Ticket title
- `description` (required): Detailed description  
- `priority` (optional): `low`, `normal`, `high`, `urgent` (default: `normal`)

**Example:**
```json
{
  "subject": "Printer not working",
  "description": "The office printer is showing error code E001",
  "priority": "high"
}
```

### **update_ticket**
Update an existing ticket.

**Parameters:**
- `ticket_id` (required): ID of the ticket to update
- `status` (optional): `new`, `open`, `pending`, `hold`, `solved`, `closed`
- `priority` (optional): `low`, `normal`, `high`, `urgent`
- `comment` (optional): Add a comment to the ticket

**Example:**
```json
{
  "ticket_id": 12345,
  "status": "solved",
  "comment": "Issue resolved by restarting the printer"
}
```

### **delete_ticket**
Delete a specific ticket.

### **get_single_ticket**
Retrieve details of a specific ticket.

### **get_all_tickets**
List all tickets with pagination support.

### **search_tickets**
Search tickets by various criteria.

### **list_users**
Get list of Zendesk users.

### **add_comment**
Add comments to existing tickets.

## 📁 File Structure

```
zendesk-mcp-server/
├── main.py                    # MCP server entry point
├── config.py                  # Configuration management
├── utils/
│   ├── __init__.py
│   └── client.py              # Zendesk API client
├── tools/
│   ├── __init__.py
│   ├── create_ticket.py       # Create ticket tool
│   ├── update_ticket.py       # Update ticket tool
│   ├── delete_ticket.py       # Delete ticket tool
│   ├── get_single_ticket.py   # Get single ticket tool
│   ├── get_all_tickets.py     # Get all tickets tool
│   ├── search_tickets.py      # Search tickets tool
│   ├── list_users.py          # List users tool
│   └── add_comment.py         # Add comment tool
├── requirements.txt           # Dependencies
├── .env                       # Environment variables (create this)
└── README.md                  # This file
```

## 📋 Requirements
- Python 3.8+
- Valid Zendesk account with API access
- Zendesk API token
