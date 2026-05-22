FROM python:3.11-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY pyproject.toml ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Copy source code
COPY . .


# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1

# Expose MCP port
EXPOSE 8000

# Run the MCP server
CMD ["uv", "run", "python", "main.py"]
