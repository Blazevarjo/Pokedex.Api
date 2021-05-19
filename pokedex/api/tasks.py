from pokedex.celery import app


@app.task(name='test')
def test():
    print('test')


app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'pokedex.test',
        'schedule': 10.0
    }
}
