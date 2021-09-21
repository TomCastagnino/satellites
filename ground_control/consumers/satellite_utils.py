import random

def solve_task(task, error_margin):
    if random.randint(0, 100) <= error_margin:
        return 'Failed to complete task: ' + str(task), False
    else:
        return 'Task completed: ' + str(task), True
