from fastapi import FastAPI
from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field
from typing import Annotated    

class DistanceDuration(BaseModel):
    distance: Annotated[float, Field(...,lt=100)] = 0
    hours: Annotated[int, Field(...,lt=24)] = 0
    minutes: Annotated[int, Field(...,lt=60)] = 50
    seconds: Annotated[int, Field(...,lt=60)] = 0


app = FastAPI(title = 'Run toolz')

@app.post('/avg_pace')
def avgPace(data: DistanceDuration ):
    
    duration_minutes = (60 * data.hours) + data.minutes + (data.seconds / 60)
    pace = duration_minutes / data.distance
    
    pace_m = str(pace).split('.')[0]
    pace_s = int(str(pace).split('.')[1]) * 60
    
        
    return {
            "pace": pace_m + ':' + str(pace_s)[0:2]
        }