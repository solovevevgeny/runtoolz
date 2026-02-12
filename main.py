from fastapi import FastAPI
from datetime import datetime, time


app = FastAPI(title = 'Run toolz')



@app.get('/avg_pace')
def avgPace(distance: float, time: time):
    return {'time': time}