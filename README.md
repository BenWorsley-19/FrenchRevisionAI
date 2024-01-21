# French Lesson AI

Tool which harnesses Open AI and ElevenLabs AI to provide french lessons

## Prerequisites

- Python 3.11+
- Poetry 1.6.1+
- Poetry should install ffmpeg for you but if you have trouble, install it on your machine. On macs you can isntall with: `brew install ffmpeg`

## Building Locally

The project uses [Poetry](https://python-poetry.org/) for packaging and managing dependencies.
Install it with the command  `curl -sSL https://install.python-poetry.org | python3 -`

### Command Line

Move to the repo deirectory.
`poetry install` will install the required dependencies for you.

## Running Locally

Move to the repo deirectory to execute the commands and run:
`poetry run python -m frenchrevisionai` 

## Running Tests

To run the unit tests you can run the command 'poetry run pytest'
