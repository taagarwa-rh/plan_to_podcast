import gradio as gr

from plan_to_podcast.constants import BANNER_TEXT, EXAMPLES, VOICES
from plan_to_podcast.generate_podcast import generate_podcast_script
from plan_to_podcast.tts import podcast_tts
from plan_to_podcast.utils import get_models

MODELS = get_models()

# Podcast script generation tab
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(BANNER_TEXT)
    with gr.Row(variant="panel"):
        with gr.Accordion("0. (Optional) Select a preloaded script", open=False):
            example = gr.Dropdown(label="Example", choices=list(EXAMPLES.keys()), interactive=True)
            load_example = gr.Button(value="Load Example", variant="secondary")

    with gr.Row():
        # Script Generation Column
        with gr.Column(variant="panel"):
            gr.Markdown("## 1. Generate a Podcast Script")
            with gr.Row():
                host_a = gr.Textbox(label="Host 1 Name", value="Lily")
                host_b = gr.Textbox(label="Host 2 Name", value="Marshall")
            with gr.Row():
                voice_a = gr.Dropdown(list(VOICES.items()), value="af_heart", label="Host 1 Voice", interactive=True)
                voice_b = gr.Dropdown(list(VOICES.items()), value="am_michael", label="Host 2 Voice", interactive=True)
                host_voices = {host_a.value: voice_a.value, host_b.value: voice_b.value}
                host_voices = gr.JSON(value=host_voices, visible=False)
            with gr.Row():
                topic = gr.Textbox(
                    label="Topic", info="Topic for your podcast. You can also specify key points for the hosts to talk about.", max_lines=5
                )
            with gr.Row():
                default_model = "qwen2.5:32b" if "qwen2.5:32b" in MODELS else MODELS[0]
                model = gr.Dropdown(MODELS, value=default_model, label="Generation Model", info="LLM to use for generating script")
            with gr.Row():
                generate_btn = gr.Button("Generate", variant="primary")
        # TTS column
        with gr.Column(variant="panel"):
            gr.Markdown("## 2. Review Generated Script")
            script = gr.Textbox(
                show_label=False,
                max_lines=5,
                info="Podcast script. Each conversation turn must in the format '<|speaker|>: content', separated by a blank line.",
            )
            gr.Markdown("## 3. Convert Podcast Script to Audio")

            with gr.Row():
                tts_btn = gr.Button("Generate", variant="primary")
            with gr.Row():
                out_audio = gr.Audio(label="Output Audio", interactive=False, streaming=False, autoplay=True)
            with gr.Accordion("Output Tokens", open=False):
                out_ps = gr.Textbox(interactive=False, show_label=False, info="Tokens used to generate the audio.", lines=15)

    load_example.click(lambda x: (EXAMPLES[x]["topic"], EXAMPLES[x]["script"].strip()), inputs=[example], outputs=[topic, script])
    generate_btn.click(fn=generate_podcast_script, inputs=[topic, model, host_a, host_b], outputs=[script])
    tts_btn.click(fn=podcast_tts, inputs=[script, host_voices], outputs=[out_audio, out_ps])

demo.launch()
