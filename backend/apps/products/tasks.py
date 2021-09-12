import random

from app.celery import app as celery_app


def collatz_conjecture_generator(number):
    """
    # conjecture 3n+1

    If the number is even, divide it by two.
    If the number is odd, triple it and add one.
    """
    while True:
        if (number % 2) == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        yield number


@celery_app.task()
def collatz_conjecture_task(number=None):
    """
    Task example
    """
    if number is None:
        number = random.randint(0, 1000)
    collatz_sequences = collatz_conjecture_generator(number)
    next_collatz = next(collatz_sequences)
    index = 0
    while next_collatz != 1:
        next_collatz = next(collatz_sequences)
        index += 1
    return {"iterations": index, "number_start": number}
