import argparse
import logging
from pathlib import Path

import soundfile as sf

from plan_to_podcast.generate_podcast import generate_podcast_script
from plan_to_podcast.tts import podcast_tts

logger = logging.getLogger(__name__)
DIRECTORY_PATH = Path(__file__).parent.parent
OUTFILE = DIRECTORY_PATH / "audio.wav"


def main(prompt: str, model: str):
    """Call main function."""
    host_a = "Lily"
    host_b = "Marshall"
    host_voices = {
        "Lily": "af_heart",
        "Marshall": "am_michael",
    }

    # Generate a podcast script about the topic
    podcast_script = generate_podcast_script(prompt=prompt, model=model, host_a=host_a, host_b=host_b)

    # Convert the podcast script text to speech
    audio, _ = podcast_tts(text=podcast_script, host_voices=host_voices)

    # Save the audo file
    sf.write(OUTFILE, audio[1], audio[0])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prompt", type=str, help="Podcast topic prompt. You may optionally include required points to hit by specifying them."
    )
    parser.add_argument("-m", "--model", type=str, default="qwen2.5:32b", help="Model for podcast script generation.")
    parser.add_argument("-o", "--output", type=Path, default=OUTFILE, help="Model for podcast script generation.")
    args = parser.parse_args()
    main(args.prompt, args.model)
