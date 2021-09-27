import os
import click
import requests


@click.command()
@click.option('--host', help='Satellite Host.')
@click.option('--port', help='Satellite Port.')
def setup_satellite(host, port):
    satellite_name = f'satellite_{port}'

    ground = os.environ.get('GROUND_HOST', 'http://127.0.0.1:8000')
    endpoint = f'{ground}/api/register_satellite/'

    payload = {
        'name': satellite_name,
        'host': host,
        'port': int(port)
    }

    r = requests.post(endpoint, data=payload)
    click.echo(r.content)


if __name__ == '__main__':
    setup_satellite()