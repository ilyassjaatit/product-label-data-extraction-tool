import pytest
from celery.result import EagerResult

from apps.products.tasks import collatz_conjecture_generator, collatz_conjecture_task

pytestmark = pytest.mark.django_db


def test_collatz_conjecture_generator():
    generator = collatz_conjecture_generator(15)
    assert next(generator) == 46
    assert next(generator) == 23


def test_collatz_conjecture_task(settings):
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = collatz_conjecture_task.delay(10)
    assert isinstance(task_result, EagerResult)
    assert task_result.result["iterations"] == 5
    assert task_result.result["number_start"] == 10
