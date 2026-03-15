from __future__ import annotations

import gradio as gr

from src.config import HOST, INBROWSER, PORT
from src.ui import create_ui


def create_app() -> gr.Blocks:
    """Build and return the Gradio application."""
    return create_ui()


def main() -> None:
    """Run the local Gradio server."""
    app = create_app()
    app.launch(
        server_name=HOST,
        server_port=PORT,
        inbrowser=INBROWSER,
    )


if __name__ == "__main__":
    main()
