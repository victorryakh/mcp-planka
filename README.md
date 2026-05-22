# MCP Planka Server

An MCP (Model Context Protocol) server that exposes Planka project management functionality as tools and resources.

## Features

- **16 Tools** for board, card, list, and project operations
- **4 Resource templates** for accessing Planka data via `planka://` URIs
- **Streamable HTTP transport** for broad client compatibility
- **Lazy loading** via plankapy's schema cache

## Installation

```bash
uv sync
```

## Configuration

Set environment variables or create a `.env` file:

| Variable | Description | Required |
|----------|-------------|----------|
| `PLANKA_URL` | Planka server URL | Yes |
| `PLANKA_API_KEY` | API key for authentication | Either this or username/password |
| `PLANKA_USERNAME` | Username | If not using API key |
| `PLANKA_PASSWORD` | Password | If not using API key |
| `ACCEPT_TERMS` | Accept ToS on first login (default: true) | No |
| `MCP_HOST` | MCP server host (default: 0.0.0.0) | No |
| `MCP_PORT` | MCP server port (default: 8000) | No |

Example `.env`:
```
PLANKA_URL=https://planka.example.com
PLANKA_API_KEY=your_api_key_here
```

## Usage

```bash
uv run python main.py
```

The server runs on `http://localhost:8000/mcp` by default (streamable-http transport).

## Tools

| Tool | Description |
|------|-------------|
| `get_projects` | List all projects |
| `get_project` | Get project details |
| `get_project_boards` | Get boards in a project |
| `get_board` | Get board details |
| `get_board_lists` | Get lists in a board |
| `create_list` | Create a new list |
| `get_board_cards` | Get cards in a board |
| `get_card` | Get card details |
| `create_card` | Create a new card |
| `update_card` | Update card (name, description, due date) |
| `delete_card` | Delete a card |
| `move_card` | Move card to another list |
| `search_cards` | Search cards by name |
| `get_card_comments` | Get comments on a card |
| `get_board_activity` | Get activity (comments) on all cards in a board |
| `get_project_activity` | Get activity (comments) on all cards in a project |

## Resources

| URI | Description |
|-----|-------------|
| `planka://me` | Current user info |
| `planka://projects` | List all projects |
| `planka://project/{id}` | Project details |
| `planka://board/{id}` | Board details |

## Development

```bash
uv sync
uv run python -c "from mcp_planka.server import mcp; print(mcp.name)"
```