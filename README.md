
# Python Boilerplate Project

This is a boilerplate Python project built to streamline the development of robust and maintainable applications. It uses [Poetry](https://python-poetry.org/) for dependency management and includes a set of tools and libraries to support development, testing, and formatting.

## Features

- Environment-based configurations (`.env` files for dev, staging, and prod).
- Linting, formatting, and type-checking with Pylint, Black, and MyPy.
- CLI support with Click.
- Logging with Loguru.
- Debugging with Rich.
- Data manipulation with Pandas.
- Pre-commit hooks for code quality.
- A robust development and testing workflow.

## Setup

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/) for dependency management.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TranNhanGIS/python-boilerplate.git
cd python-boilerplate
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Set up the environment variables by creating `.env` files for each environment (`.env.dev`, `.env.staging`, `.env.prod`).

## Usage

### Running the Application

Start the application:
```bash
poetry run python -m src.main
```

### Running CLI Commands

Use the CLI commands defined in `src/cli/cli.py`:
```bash
poetry run python -m src.cli.cli --help
```

### Running Tests

Run unit and integration tests:
```bash
poetry run pytest
```

Generate test coverage report:
```bash
poetry run pytest --cov=src
```

## Libraries Used

### Dependencies

| Library            | Version  | Description                                                  |
|--------------------|----------|--------------------------------------------------------------|
| `pydantic-settings`| 2.6.1    | Settings validation using Pydantic.                          |
| `click`            | 8.1.7    | CLI support.                                                 |
| `loguru`           | 0.7.2    | Easy and powerful logging utility.                           |
| `humanize`         | 4.11.0   | Human-readable representations of data.                      |
| `pandas`           | 2.2.3    | Data manipulation and analysis.                              |

### Development Dependencies

| Library         | Version  | Description                                    |
|-----------------|----------|------------------------------------------------|
| `mypy`          | 1.13.0   | Static type checking.                          |
| `rich`          | 13.9.4   | Beautiful terminal output for CLI.             |
| `pytest`        | 8.3.3    | Testing framework for Python.                  |
| `pytest-cov`    | 6.0.0    | Test coverage reporting.                       |
| `pre-commit`    | 4.0.1    | Manage pre-commit hooks for consistent quality.|
| `black`         | 24.10.0  | Auto code formatter.                           |
| `pylint`        | 3.3.1    | Code linting to ensure quality.                |
| `yamllint`      | 1.35.1   | YAML file linting to ensure quality.           |

## Project Structure

```bash
python-boilerplate/
├── .dockerignore              # Docker ignore rules
├── .editorconfig              # Editor configuration for consistent coding 
├── .env.dev                   # Development environment variables
├── .env.prod                  # Production environment variables
├── .env.staging               # Staging environment variables
├── .gitignore                 # Git ignore rules
├── .gitattributes             # Git attributes rules
├── .hadolint.yaml             # Hadolint configuration for Dockerfile linting
├── .mypy.ini                  # MyPy type-checking configuration
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── .pylintrc                  # Pylint configuration
├── .yamllint                  # Yamllint configuration
├── CHANGELOG.md               # Changelog for the project
├── docker-compose.dev.yml     # Docker Compose configuration for development
├── docker-compose.prod.yml    # Docker Compose configuration for production
├── docker-compose.staging.yml # Docker Compose configuration for staging
├── Dockerfile                 # Docker build configuration
├── poetry.lock                # Dependency lock file
├── pyproject.toml             # Project and dependency configuration (Poetry)
├── README.md                  # Project documentation
├── start.sh                   # Startup scriptstyle
├── src/                       # Main source code
│   ├── main.py                # Application entry point
│   ├── __init__.py            # Package initializer
│   ├── app/                   # Core application logic
│   │   ├── utils/             # Utility scripts
│   │   │   └── __init__.py
│   │   ├── config.py          # Application configuration
│   │   └── __init__.py
│   ├── cli/                   # Command Line Interface (CLI) commands
│   │   ├── cli.py
│   │   └── __init__.py
├── tests/                     # Test modules
│   ├── __init__.py
│   ├── intergration/          # Integration tests
│   │   └── __init__.py
│   └── unit/                  # Unit tests
│       └── __init__.py
```

## Development

### Type Checking

Run MyPy for static type checks:
```bash
poetry run mypy src
```

### Formatting and Linting

Format the code:
```bash
poetry run black src
```

Lint the code:
```bash
poetry run pylint src
```

### Dockerfile Checking

Download the latest Linux Hadolint package:
```bash
wsl
wget -O hadolint https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64
sudo mv hadolint /usr/local/bin/hadolint
sudo chmod +x /usr/local/bin/hadolint
```

Lint the Dockerfile:
```bash
hadolint --config .hadolint.yaml Dockerfile
```

### Yaml Checking

Download the latest Linux Yaml package:
```bash
wsl
pip install --user yamllint
```

Lint the Dockerfile:
```bash
yamllint -c .yamllint .
```

### Pre-commit Hooks

Download the latest Linux Pre-commit package:
```bash
wsl
pip install pre-commit
```

Ensure code quality using pre-commit hooks:
```bash
pre-commit install
pre-commit
```

## Contributing

Feel free to open issues or submit pull requests for any feature requests, bugs, or improvements.

## License

This project is licensed under the MIT License.
