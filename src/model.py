from __future__ import annotations

from functools import lru_cache
from typing import Any

from PIL.Image import Image
from transformers import Pipeline, pipeline

from src.config import MODEL_NAME, TOP_K


class ModelLoadError(RuntimeError):
    """Raised when the Hugging Face pipeline cannot be initialized."""


@lru_cache(maxsize=1)
def get_model() -> Pipeline:
    """Load the image classification pipeline once and reuse it."""
    try:
        return pipeline(
            task="image-classification",
            model=MODEL_NAME,
            device=-1,
        )
    except Exception as exc:
        raise ModelLoadError(
            f"Failed to load image classification model '{MODEL_NAME}'."
        ) from exc


def predict(image: Image, top_k: int = TOP_K) -> list[dict[str, Any]]:
    """Run image inference and return raw top-k predictions."""
    classifier = get_model()

    try:
        result = classifier(image, top_k=top_k)
    except Exception as exc:
        raise RuntimeError("Failed to run image inference.") from exc

    return list(result)
