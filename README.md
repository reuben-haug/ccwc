# PBOY Python Template

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Template Configuration](#template-configuration)
4. [Setup Instructions](#setup-instructions)
5. [Using & Testing](#using-and-testing)
6. [Documentation](#documentation)

## Overview

This project is a personal template for Python projects.

Features:
- Pre-configured Conda environment
- Sphinx documentation setup
- Example tests and main script

## Prerequisites

Choose your development environment:

### Option 1: GitHub Codespaces (Recommended)
- GitHub account
- Web browser
- VS Code (optional, for local connection to Codespace)

### Option 2: Local Development
- Python 3.12+
- Conda or Miniconda
- VS Code with Python extension
- Git
- Docker (optional, only if using dev containers locally)

## Template Configuration

The setup script (`setup_template.py`) will help you configure the following files:
- `pyproject.toml` - Project metadata and dependencies.  This is your source of truth for project dependencies
- `LICENSE` - Project license information
- `.github/codespace.yaml` - GitHub Codespace settings
- `docs/source/index.rst` - Sphinx documentation index
- `docs/README.md` - Project-specific README for documentation

## Setup Instructions

Clone the repository and follow the setup instructions in the terminal.

## Using and Testing

Refer to [docs/workflow.md](docs\workflow.md) for instructions on how to use and test the project.

## Documentation

Your project-specific README.md can be found in [docs/README.md](docs/README.md).  Feel free to replace or edit this README with your own.

todo: Fix git configuration in remote Codespace