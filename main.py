
from fastapi import FastAPI
from datetime import datetime
import pytz
import ntplib

app = FastAPI()

@app.get("/horario")
def get_horario():
    try:
        cliente = ntplib.NTPClient()
        resposta = cliente.request('a.st1.ntp.br')
        data_hora = datetime.fromtimestamp(resposta.tx_time, pytz.timezone('America/Sao_Paulo'))
    except:
        # fallback para o horário do servidor caso o NTP falhe
        data_hora = datetime.now(pytz.timezone('America/Sao_Paulo'))

    return {
        "data": data_hora.strftime("%Y-%m-%d"),
        "hora": data_hora.strftime("%H:%M:%S"),
        "dia_da_semana": data_hora.strftime("%A").lower(),
        "fuso": "America/Sao_Paulo",
        "origem": "NTP @ a.ntp.br"
    }
