import openai


def get_models() -> list[str]:
    """Get a list of available models."""
    client = openai.Client(base_url="http://localhost:11434/v1", api_key="NONE")
    models = sorted([model.id for model in client.models.list()])
    return models
