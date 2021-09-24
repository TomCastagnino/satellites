import requests
from earth_api.models import Satellite
from earth_api.utils import sort_task_list, distribute_tasks


def start_distribution(list_of_tasks):
    sorted_list = sort_task_list(list_of_tasks) 
    online_satellites = get_online_satellites()
    response = []
    for port in online_satellites:
        endpoint = 'http://127.0.0.1:' + port + '/api/tasks/'
        task, sorted_list = distribute_tasks(sorted_list)
        try:
            if len(task['tasks']):
                r = requests.post(endpoint, data=task)
                response.append(r.json()['results'])
        except requests.exceptions.ConnectionError as e:
            print(e)
    return response

def get_online_satellites():
    online_satellites = []
    satellites = Satellite.objects.all()
    for satellite in satellites:
        port = str(satellite.port)
        if is_online(port):
            online_satellites.append(port)
    return online_satellites
        
def is_online(port):
    endpoint = 'http://127.0.0.1:' + port + '/api/health/'
    try:
        r = requests.get(endpoint)
        if r.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False
    return False
    
