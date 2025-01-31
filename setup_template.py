# setup_template.py

import argparse
import os
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
TEMPLATE_FILES = [
    "pyproject.toml",
    "LICENSE",
    ".github/codespace.yaml",
    "docs/source/index.rst",
    "docs/README.md"
]

DEFAULT_PLACEHOLDERS = {
    'PROJECT_NAME_PLACEHOLDER': 'PROJECT_NAME_PLACEHOLDER',
    'AUTHOR_NAME_PLACEHOLDER': 'AUTHOR_NAME_PLACEHOLDER',
    'YEAR_PLACEHOLDER': 'YEAR_PLACEHOLDER',
    'PROJECT_DESCRIPTION_PLACEHOLDER': 'PROJECT_DESCRIPTION_PLACEHOLDER'
}


def update_file(file_path: str, replacements: Dict[str, str], reverse: bool = False) -> None:
    """Update file contents with replacements."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        for placeholder, value in replacements.items():
            old, new = (value, placeholder) if reverse else (placeholder, value)
            content = content.replace(old, new)

        with open(file_path, 'w') as file:
            file.write(content)
        logger.info(f"Updated {file_path}")

    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")
        raise


def validate_files() -> None:
    """Validate all required files exist."""
    missing = [f for f in TEMPLATE_FILES if not os.path.exists(f)]
    if missing:
        raise FileNotFoundError(f"Missing required files: {', '.join(missing)}")


def sanitize_project_name(name: str) -> str:
    """Convert project name to Python package name."""
    return name.lower().replace(" ", "_")


def main() -> None:
    parser = argparse.ArgumentParser(description="Setup or revert project template")
    parser.add_argument("--revert", action="store_true", help="Revert to template defaults")
    args = parser.parse_args()

    try:
        validate_files()

        if args.revert:
            for file_path in TEMPLATE_FILES:
                update_file(file_path, DEFAULT_PLACEHOLDERS, reverse=False)
            logger.info("Successfully reverted to template defaults")
            return

        # Get user input
        replacements = {
            'PROJECT_NAME_PLACEHOLDER': sanitize_project_name(
                input('Enter project name: ').strip() or "PROJECT_NAME_PLACEHOLDER"
            ),
            'AUTHOR_NAME_PLACEHOLDER': 
                input('Enter author name: ').strip() or "AUTHOR_NAME_PLACEHOLDER",
            'YEAR_PLACEHOLDER':
                input('Enter year: ').strip() or "YEAR_PLACEHOLDER",
            'PROJECT_DESCRIPTION_PLACEHOLDER':
                input('Enter project description: ').strip() or "PROJECT_DESCRIPTION_PLACEHOLDER"
        }

        # Update files
        for file_path in TEMPLATE_FILES:
            update_file(file_path, replacements)

        logger.info("Template setup completed successfully")

    except Exception as e:
        logger.error(f"Setup failed: {str(e)}")
        raise


if __name__ == '__main__':
    main()
