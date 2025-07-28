from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/horario")
def obter_horario():
    fuso = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso)
    return {
        "data": agora.strftime("%Y-%m-%d"),
        "hora": agora.strftime("%H:%M:%S"),
        "fuso": "UTC-3"
    }
