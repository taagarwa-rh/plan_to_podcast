import soundfile as sf
import torch
from kokoro import KPipeline

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
pipeline = KPipeline(lang_code="a", device=DEVICE)


# From: https://huggingface.co/hexgrad/Kokoro-82M
def tts(text: str, outpath: str, voice: str = "af_heart", speed: int = 1):
    """Convert text to speech."""
    generator = pipeline(text, voice=voice, speed=speed, split_pattern=r"\n+")
    for i, (gs, ps, audio) in enumerate(generator):
        print(gs)  # gs => graphemes/text
        print(ps)  # ps => phonemes
        sf.write(outpath, audio, 24000)  # save each audio file


if __name__ == "__main__":
    tts("Hello world!", outpath="output.wav")
