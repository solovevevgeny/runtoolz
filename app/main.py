from fastapi import FastAPI
from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field
from typing import Annotated    

class duration(BaseModel):
    hours: Annotated[int, Field(...,lt=24)] = 0
    minutes: Annotated[int, Field(...,lt=60)] = 25
    seconds: Annotated[int, Field(...,lt=60)] = 0


app = FastAPI(title = 'Run toolz')

@app.post('/avg_pace')
def avgPace(distance: float, duration: duration ):
    
    duration_minutes = (60 * duration.hours) + duration.minutes + (duration.seconds / 60)
    pace = duration_minutes / distance
    
    pace_m = str(pace).split('.')[0]
    pace_s = int(str(pace).split('.')[1]) * 60
    
        
    return {
            "distance": distance,
            "minutes": duration_minutes,
            "pace": pace_m + ':' + str(pace_s)[0:2]
        }