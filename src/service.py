from __future__ import annotations

from PIL.Image import Image

from src.config import ERROR_INFERENCE, ERROR_MODEL_LOAD, ERROR_NO_IMAGE, TOP_K
from src.model import ModelLoadError, predict
from src.utils import format_predictions


def analyze_image(image: Image | None) -> str:
    """Validate input, run inference, and format the top-k result."""
    if image is None:
        return ERROR_NO_IMAGE

    try:
        predictions = predict(image, top_k=TOP_K)
    except ModelLoadError:
        return ERROR_MODEL_LOAD
    except Exception:
        return ERROR_INFERENCE

    return format_predictions(predictions[:TOP_K])
