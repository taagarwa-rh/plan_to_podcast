from enum import Enum

from openai import Client
from pydantic import BaseModel

SYSTEM_PROMPT = """
You are a helpful assistant. The user will provide you with a topic to write a podcast about. You should write an informative podcast (a la NPR) based on the topic. The podcast should cover all the topics and key points the user requests.

The podcast has two hosts, Lily and Marshall. Lily is a intelligent, informative host who is always excited to talk about the topic. Marshall is a more skeptical host, asking questions to Lily about the topic for her to answer and adding his own thoughts to her response. Together the hosts do an excellent job of breaking down the topic and hit all the key points the user requests.

Please use the provided structure and output your response in JSON.
"""


class Hosts(Enum):
    """Host names."""

    lily = "Lily"
    marshall = "Marshall"


class ConversationTurn(BaseModel):
    """Podcast conversation turn model."""

    speaker: Hosts
    content: str


class PodcastScript(BaseModel):
    """Podcast script model."""

    script: list[ConversationTurn]


def generate_podcast_script(prompt: str, model: str) -> PodcastScript:
    """Generate a podcast script from a given prompt."""
    client = Client(base_url="http://localhost:11434/v1", api_key="NONE")
    messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}]
    response = client.beta.chat.completions.parse(messages=messages, model=model, temperature=0.5, response_format=PodcastScript)
    return response.choices[0].message.parsed


if __name__ == "__main__":
    prompt = "Red Hat Enterprise Linux (RHEL)"
    model = "qwen2.5:32b"
    response = generate_podcast_script(prompt=prompt, model=model)
    print(response)
