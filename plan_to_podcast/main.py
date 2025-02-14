import argparse
import logging
import os
import wave
from pathlib import Path

from plan_to_podcast.generate_podcast import Hosts, generate_podcast_script
from plan_to_podcast.tts import tts

logger = logging.getLogger(__name__)
DIRECTORY_PATH = Path(__file__).parent.parent
AUDIO_PATH = DIRECTORY_PATH / "output"
OUTFILE = DIRECTORY_PATH / "audio.wav"


def main(prompt: str, model: str):
    """Call main function."""
    # Cleanup output folders
    for file in AUDIO_PATH.glob("*.wav"):
        os.remove(file)

    # Generate a podcast script about a topic
    podcast_script = generate_podcast_script(prompt=prompt, model=model)

    # Convert the podcast script text to speech
    # TODO: There might be a better way to concatenate all the audio
    i = 0
    for turn in podcast_script.script:
        speaker = turn.speaker
        text = turn.content
        voice = "af_heart" if speaker == Hosts.lily else "am_michael"
        outpath = AUDIO_PATH / f"{i}.wav"
        tts(text=text, outpath=outpath, voice=voice, speed=1)
        i += 1

    # Concatenate all the speech files and save to an outfile
    # From https://stackoverflow.com/questions/2890703/how-to-join-two-wav-files-using-python
    audio = []
    files = [(int(f.stem), f) for f in AUDIO_PATH.glob("*.wav")]
    sorted_files = [f for _, f in sorted(files, key=lambda x: x[0])]
    for file in sorted_files:
        w = wave.open(str(file), "rb")
        audio.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    output = wave.open(str(OUTFILE), "wb")
    output.setparams(audio[0][0])
    for i in range(len(audio)):
        output.writeframes(audio[i][1])
    output.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prompt", type=str, help="Podcast topic prompt. You may optionally include required points to hit by specifying them."
    )
    parser.add_argument("-m", "--model", type=str, default="qwen2.5:32b", help="Model for podcast script generation.")
    args = parser.parse_args()
    main(args.prompt, args.model)
