from django.test import TestCase
from .consumers import earth_utils, satellite_utils
from unittest.mock import patch

tasks_list = [
{
    'name': 'fotos',
    'pay_off': 10,
    'resources': [1, 5] 
},
{
    'name': 'mantenimiento',
    'pay_off': 5,
    'resources': [1, 2] 
},
{
    'name': 'pruebas',
    'pay_off': 1,
    'resources': [5, 6] 
},
{
    'name': 'fsck',
    'pay_off': 0.1,
    'resources': [1, 6] 
},
]

def mocked_random(start, end):
    return 0

class UtilsTest(TestCase):
    
    def test_sort_task_list(self):
        result = earth_utils.sort_task_list(tasks_list)
        most_important_task = result[0]['name']
        self.assertEqual(most_important_task, 'fotos')
    
    def test_distribute_tasks(self):
        sorted_list = earth_utils.sort_task_list(tasks_list)
        satellite, new_tasks_list = earth_utils.distribute_tasks(sorted_list)
        most_important_task = satellite['tasks'][0]
        second_important_task = new_tasks_list[0]['name']
        self.assertEqual(most_important_task, 'fotos')
        self.assertEqual(second_important_task, 'mantenimiento')

    @patch('ground_control.consumers.satellite_utils.random.randint', mocked_random)
    def test_solve_taks_pass(self):
        result, tr = satellite_utils.solve_task('test_task', -1)
        target = 'Task completed: test_task'
        self.assertEqual(result, target)
        self.assertTrue(tr)

    @patch('ground_control.consumers.satellite_utils.random.randint', mocked_random)
    def test_solve_tasks_fail(self):
        result, fls = satellite_utils.solve_task('test_task', 1)
        target = 'Failed to complete task: test_task'
        self.assertEqual(result, target)
        self.assertFalse(fls)
