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