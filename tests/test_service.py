"""Unit tests for SecureTask business logic."""
import pytest

from securetask.service import TaskService
from securetask.validators import validate_title


def test_add_task_strips_surrounding_whitespace():
    service = TaskService()
    task = service.add_task("  Finish assignment  ")
    assert task.title == "Finish assignment"
    assert task.completed is False


def test_empty_title_is_rejected():
    service = TaskService()
    with pytest.raises(ValueError):
        service.add_task("   ")


def test_title_over_120_characters_is_rejected():
    with pytest.raises(ValueError):
        validate_title("x" * 121)


def test_list_tasks_returns_added_tasks():
    service = TaskService()
    service.add_task("Read module")
    assert [task.title for task in service.list_tasks()] == ["Read module"]


def test_complete_task_changes_status():
    service = TaskService()
    service.add_task("Run tests")
    task = service.complete_task(0)
    assert task.completed is True


def test_invalid_task_index_is_rejected():
    service = TaskService()
    with pytest.raises(IndexError):
        service.complete_task(0)
