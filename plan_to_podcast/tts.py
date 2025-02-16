import re

import numpy as np
from kokoro import KModel, KPipeline

from plan_to_podcast.constants import DEVICE, VOICES

pipelines = {lang_code: KPipeline(lang_code=lang_code, model=False, device=DEVICE) for lang_code in "ab"}
pipelines["a"].g2p.lexicon.golds["kokoro"] = "kˈOkəɹO"
pipelines["b"].g2p.lexicon.golds["kokoro"] = "kˈQkəɹQ"
model = KModel().to(DEVICE).eval()
# Download all voices
for voice in VOICES.values():
    pipelines[voice[0]].load_voice(voice)


# From: https://huggingface.co/hexgrad/Kokoro-82M
def tts(text: str, voice: str = "af_heart", speed: int = 1):
    """Convert text to speech."""
    pipeline = pipelines[voice[0]]
    pack = pipeline.load_voice(voice)
    for _, ps, _ in pipeline(text, voice, speed):
        ref_s = pack[len(ps) - 1]
        audio = model(ps, ref_s, speed)
        return (24000, audio.numpy()), ps


def podcast_tts(text: str, host_voices: dict[str, str]):
    """Convert podcast script text to speech."""
    pattern = r"<\|(.*?)\|>: (.*?)\n\n"
    turns = re.findall(pattern=pattern, string=text)
    if not all(speaker in host_voices for speaker, _ in turns):
        non_matching_hosts = [speaker for speaker, _ in turns if speaker not in host_voices]
        raise ValueError(f"Invalid speaker(s): {set(non_matching_hosts)}")
    audio = []
    tokens = []
    for speaker, content in turns:
        voice = host_voices[speaker]
        turn_audio, turn_tokens = tts(text=content, voice=voice, speed=1)
        audio.append(turn_audio[1])
        tokens.append(f"{content}\n{turn_tokens}")
    audio = np.concatenate(audio, axis=0)
    audio_tokens = "\n\n".join(tokens)
    return (24000, audio), audio_tokens
