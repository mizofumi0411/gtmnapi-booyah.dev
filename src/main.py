from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Type
import requests
import json
import time

app = FastAPI()

@app.get("/status")
async def get_status():
  maintenance = False
  unixtime = int(time.time())
  if maintenance:
    # raise MaintenanceMode()
    return {"status": "メンテナンス中", "version": "unknown", "checktimestamp": unixtime}
  url = "https://api.bedrockinfo.com/v1/status?server=gtmn.booyah.dev&port=19132"
  response = requests.get(url)
  data = response.json()
  if not 'message' in data:
    return {"status": "稼働中", "version": data["Version"], "checktimestamp": data["CheckTimestamp"]}
  else:
    return {"status": "停止中", "version": "unknown", "checktimestamp": unixtime}
    # raise MaintenanceMode()
  return data

@app.get("/players")
async def get_players():
  f = open("/app/tmp/mine_users.json","r")
  data = f.read()
  f.close()
  return Response(content=data, media_type="application/json")
