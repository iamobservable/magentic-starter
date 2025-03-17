# Magentic One Template

A ready-to-use template for building AI agents with the Magentic One framework on top of AutoGen, leveraging Claude 3.7 Sonnet.

## Overview

This repository provides a streamlined setup for building AI agents using AutoGen's [Magentic One](https://github.com/microsoft/autogen/tree/main/autogen-ext/autogen_ext/teams) interface combined with Anthropic's Claude 3.7 Sonnet model. It includes:

- Docker containerization for consistent development environments
- Environment variable management for API keys
- Ready-to-use examples of both direct agent usage and team-based workflows

## Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose
- Anthropic API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/magentic-template.git
   cd magentic-template
   ```

2. Create the required environment files:
   ```bash
   cp env/one.example env/one.env
   ```

3. Edit `env/one.env` and add your Anthropic API key:
   ```
   ANTHROPIC_MODEL="claude-3-7-sonnet-20250219"
   ANTHROPIC_API_KEY="your-api-key-here"
   ```

4. If you want to use the PostgreSQL database (currently commented out in `compose.yml`), create a database environment file:
   ```bash
   cp env/db.example env/db.env
   ```

## Usage

### Running the Examples

The repository comes with two example scripts:

#### Direct Agent Execution

This example demonstrates how to use a single agent to solve a task:

```bash
docker compose run one python magentic_one.py
```

This runs a default task: "Write a Python script to fetch data from an API."

#### Team-Based Workflow

This example shows how to use a team of agents to solve a task:

```bash
docker compose run one python main.py
```

This runs a default task: "Provide an alternative option to the meaning of life."

### Customizing Tasks

To modify the default tasks or create your own agent workflows:

1. Edit `magentic_one.py` or `main.py` to change the default task
2. Create new Python files based on the provided examples to implement different agent structures

## Project Structure

```
.
├── compose.yml           # Docker Compose configuration
├── env/                  # Environment variable files
│   ├── db.example        # Example database environment vars
│   └── one.example       # Example Anthropic API environment vars
├── one/                  # Main project directory
│   ├── Dockerfile        # Docker container definition
│   ├── magentic_one.py   # Example of direct agent execution
│   ├── main.py           # Example of team-based agent workflow
│   ├── pyproject.toml    # Python project dependencies
│   ├── src/              # Source code
│   │   └── anthropic.py  # Anthropic API client setup
│   └── uv.lock           # Dependency lock file
└── README.md             # This file
```

## Advanced Configuration

### Using a Database

The project includes commented-out configuration for a PostgreSQL database with pgvector. To enable it:

1. Uncomment the `db` service section in `compose.yml`
2. Set up proper database credentials in `env/db.env`
3. Modify your code to use the database connection

### Changing the Model

To use a different Anthropic model:

1. Update the `ANTHROPIC_MODEL` value in `env/one.env`
2. Make sure your Anthropic API key has access to the model you're requesting

## Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/my-new-feature
   ```
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
