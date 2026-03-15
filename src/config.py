from __future__ import annotations

import os

MODEL_NAME = "microsoft/resnet-50"
TOP_K = int(os.getenv("TOP_K", "3"))
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "7860"))
INBROWSER = os.getenv("INBROWSER", "true").lower() == "true"

APP_TITLE = "FilmDetector MVP"
APP_DESCRIPTION = (
    "Upload an image, run Hugging Face classification, and review the top-3 predictions."
)
APP_CSS = """
:root {
    --page-bg: linear-gradient(135deg, #f4efe6 0%, #dfe9f3 100%);
    --panel-bg: rgba(255, 252, 246, 0.92);
    --panel-border: rgba(30, 41, 59, 0.12);
    --accent: #b45309;
    --accent-dark: #7c2d12;
    --text-main: #172033;
    --text-muted: #52607a;
}

.gradio-container {
    background: var(--page-bg);
}

#app-shell {
    max-width: 900px;
    margin: 0 auto;
    padding: 24px;
}

#hero {
    padding: 28px;
    border: 1px solid var(--panel-border);
    border-radius: 24px;
    background: var(--panel-bg);
    box-shadow: 0 20px 60px rgba(15, 23, 42, 0.10);
}

#hero h1 {
    margin: 0;
    color: var(--text-main);
    font-size: 2.4rem;
}

#hero p {
    margin: 12px 0 0;
    color: var(--text-muted);
    font-size: 1rem;
}

#workspace {
    margin-top: 18px;
    padding: 24px;
    border: 1px solid var(--panel-border);
    border-radius: 24px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: 0 16px 48px rgba(15, 23, 42, 0.08);
}

#analyze-btn {
    background: linear-gradient(135deg, var(--accent), var(--accent-dark));
    border: none;
    color: white;
}
"""

ERROR_NO_IMAGE = "Error: please upload an image before running analysis."
ERROR_MODEL_LOAD = "Error: failed to load the Hugging Face model."
ERROR_INFERENCE = "Error: failed to analyze the image."
