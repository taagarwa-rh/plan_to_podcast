# Plan To Podcast

## Introduction

Generate a podcast from a given topic, locally.

## Getting Started

### Prerequisites

In order to work on this project, the following tools *must* be installed:

- [`poetry`](https://python-poetry.org/)
- [`just`](https://just.systems/man/en/)
- [`oc`](https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html) (**optional**)
- [Ollama](https://ollama.com/)
- (Optional) Qwen2.5 32b Q4_K_M (`ollama pull qwen2.5:32b`)

### Initial Steps
To begin working on this project:

1. Clone the repository to your local system via `git clone`
1. Change directory to the project `cd plan_to_podcast`
1. Install the project dependencies `poetry install`
1. Run `just` to see available recipes

### Usage

#### Run the Gradio App

```sh
poetry run gradio plan_to_podcast/app.py
```

Once it's running the app will be available at [http://localhost:7860](http://localhost:7860).

#### Run an Example

```sh
poetry run python plan_to_podcast/main.py --help
```
```sh
usage: main.py [-h] [-m MODEL] prompt

positional arguments:
  prompt                Podcast topic prompt. You may optionally include required points to hit by specifying them.

options:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Model for podcast script generation.
```

Sample usage generating a podcast about RHEL using Qwen2.5 32b (default):
```sh
poetry run python plan_to_podcast/main.py "Red Hat Enterprise Linux (RHEL)"
```

The final audio will be output to `audio.wav`. The individual conversation turns are available in `output/`

You can also specify the model for the podcast script generation:
```sh
poetry run python plan_to_podcast/main.py "Red Hat Enterprise Linux (RHEL)" -m "llama3.3"
```