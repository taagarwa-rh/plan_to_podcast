from typing import Literal

from openai import Client
from pydantic import BaseModel, create_model

SYSTEM_PROMPT = """
You are a helpful assistant. The user will provide you with a topic to write a podcast about. You should write an informative podcast (a la NPR) based on the topic. The podcast should cover all the topics and key points the user requests.

The podcast has two hosts, {host_a} and {host_b}. {host_a} is a intelligent, informative host who is always excited to talk about the topic. {host_b} is a more skeptical host, asking questions to {host_a} about the topic for her to answer and adding his own thoughts to her response. Together the hosts do an excellent job of breaking down the topic and hit all the key points the user requests.

Please use the provided structure and output your response in JSON.
"""


def script_to_string(script: BaseModel) -> str:
    """Convert podcast script to string."""
    turns = [f"<|{turn.speaker}|>: {turn.content}" for turn in script.script]
    return "\n\n".join(turns)


def generate_podcast_script(prompt: str, model: str, host_a: str, host_b: str) -> str | BaseModel:
    """Generate a podcast script from a given prompt."""
    # Construct the pydantic model dynamically
    conversation_turn = create_model("ConversationTurn", speaker=(Literal[host_a, host_b], ...), content=(str, ...))
    podcast_script = create_model("PodcastScript", script=(list[conversation_turn], ...))
    # Create the OpenAI client
    client = Client(base_url="http://localhost:11434/v1", api_key="NONE")
    # Construct the messages
    system_prompt = SYSTEM_PROMPT.format(host_a=host_a.title(), host_b=host_b.title())
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
    response = client.beta.chat.completions.parse(messages=messages, model=model, temperature=0.5, response_format=podcast_script)
    # Extract the parsed pydantic object
    podcast_script = response.choices[0].message.parsed
    return script_to_string(podcast_script)


if __name__ == "__main__":
    prompt = "Red Hat Enterprise Linux (RHEL)"
    model = "qwen2.5:32b"
    response = generate_podcast_script(prompt=prompt, model=model, host_a="Hank", host_b="John")
    print(response)
