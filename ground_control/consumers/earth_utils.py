
def sort_task_list(task_list):
    """
    :param task_list: each element of the list must include a 'resources' and a 'name' key 
    """
    return sorted(task_list, key=lambda task: (task['pay_off']/len(task['resources'])), reverse=True)

def distribute_tasks(list_of_tasks):
    """
    Takes a list of task and returns a satellite dict and a new list.
    :param list_of_task: each element of the list must include a 'resources' and a 'name' key
    """
    satellite = {'tasks': [], 'resources': set()}
    filtered_list = []
    for task in list_of_tasks:
        resources = set(task['resources'])
        if resources & satellite['resources'] == set():
            satellite['tasks'].append(task['name'])
            satellite['resources'].update(resources)
        else:
            filtered_list.append(task)
    return [satellite, filtered_list]



if __name__ == "__main__":
    
    NUM_OF_SATELLITES = 2
    
    tasks_list = [
    {
        'name': 'fotos',
        'pay_off': 10,
        'resources': [1, 5] 
    },
    {
        'name': 'mantenimiento',
        'pay_off': 1,
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

    my_list = sort_task_list(tasks_list)
    satellites = []
    for stl in range(NUM_OF_SATELLITES):
        s, new_list = distribute_tasks(my_list)
        my_list = new_list
        satellites.append(s)

    print(satellites)
    print('######')
    print(my_list)