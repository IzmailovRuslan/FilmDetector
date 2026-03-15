from __future__ import annotations

import gradio as gr

from src.config import APP_CSS, APP_DESCRIPTION, APP_TITLE
from src.service import analyze_image


def create_ui() -> gr.Blocks:
    """Create the Gradio interface for image classification."""
    with gr.Blocks(title=APP_TITLE) as demo:
        with gr.Column(elem_id="app-shell"):
            gr.HTML(f"<style>{APP_CSS}</style>")
            gr.HTML(
                f"""
                <section id="hero">
                    <h1>{APP_TITLE}</h1>
                    <p>{APP_DESCRIPTION}</p>
                </section>
                """
            )

            with gr.Column(elem_id="workspace"):
                image_input = gr.Image(
                    type="pil",
                    label="Upload image",
                    sources=["upload"],
                )
                analyze_button = gr.Button("Analyze image", elem_id="analyze-btn")
                result_output = gr.Textbox(
                    label="Prediction result",
                    lines=6,
                    interactive=False,
                    placeholder="Top-3 predictions will appear here.",
                )

                analyze_button.click(
                    fn=analyze_image,
                    inputs=image_input,
                    outputs=result_output,
                )

    return demo
