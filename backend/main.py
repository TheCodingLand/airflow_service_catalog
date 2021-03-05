from fastapi import FastAPI
import requests
from requests.auth import HTTPBasicAuth
app = FastAPI()
import base64
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



usrPass = "airflow:airflow"
    #b64Val = base64.b64encode(usrPass)
username="airflow"
password="airflow"
b64Val =base64.b64encode(usrPass.encode()).decode()
headers = { "Authorization": f"Basic {b64Val}" }
headers.update({"accept": "application/json"})

@app.get("/")
async def root():
    
 
    
    res = requests.get("http://localhost:8080/api/v1/dags?limit=100",auth=(username,password))
    #headers=headers)
    print (res)
    print (res.text)

    return res.json()["dags"][0]
 

@app.get("/dags")
async def get_dags():
    
    
   
    res = requests.get("http://localhost:8080/api/v1/dags?limit=100",auth=(username,password))
    #headers=headers)
    print (res)
    print (res.text)

    return res.json()["dags"][0]

@app.get("/emails")
def list_dag_runs_today():
    data= {
    "dag_ids": [
        "create_ticket_from_email"
    ],
    
    
    "execution_date_gte": "2021-01-04T00:00:00.577Z",
    "execution_date_lte": "2021-04-04T23:49:25.577Z",
    "page_limit": 1,
    "page_offset": 0
    
    }
    
    
    res = requests.post("http://localhost:8080/api/v1/dags/~/dagRuns/list",json = data, auth=(username,password))
    return res.json()