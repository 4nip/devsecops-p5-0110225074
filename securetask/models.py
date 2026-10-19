"""Data model for a task."""
from dataclasses import dataclass


@dataclass
class Task:
    """A task with a title and completion state."""

    title: str
    completed: bool = False
