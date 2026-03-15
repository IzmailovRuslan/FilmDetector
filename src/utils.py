from __future__ import annotations

from typing import Any


def format_score(score: float) -> str:
    """Convert a raw score to a readable percentage string."""
    return f"{score * 100:.2f}%"


def format_predictions(predictions: list[dict[str, Any]]) -> str:
    """Convert model output into a numbered list for the UI."""
    lines = []

    for index, item in enumerate(predictions, start=1):
        label = item.get("label", "unknown")
        score = float(item.get("score", 0.0))
        lines.append(f"{index}. {label} - {format_score(score)}")

    return "\n".join(lines)
