"""Task-management operations, separated from the command-line interface."""
from securetask.models import Task
from securetask.validators import validate_title


class TaskService:
    """Store and manage tasks in memory."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        """Validate and add a new task."""
        task = Task(title=validate_title(title))
        self._tasks.append(task)
        return task

    def list_tasks(self) -> list[Task]:
        """Return a copy of the current task list."""
        return list(self._tasks)

    def complete_task(self, index: int) -> Task:
        """Mark a task complete using a zero-based index."""
        if not isinstance(index, int) or index < 0 or index >= len(self._tasks):
            raise IndexError("Task index does not exist.")
        self._tasks[index].completed = True
        return self._tasks[index]
