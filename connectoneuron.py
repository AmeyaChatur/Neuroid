import sys
import mariadb
import time
import os
global conn
from python_on_whales import docker

#Connect to the database
conn = mariadb.connect(
user="root",
password="Aven6er$",
host="localhost",
port=3306,
database="Neuron_table"
)

cur = conn.cursor()

def print_row(cur):
    for row in cur:
        print(row)

#Time after which the query will be executed again
refresh_mins=0.05
#Initial Query to get the existing number of rows and keep track of rows before new entry
prev_row_num=0
query="""SELECT model_master.model_master_id,simulation_req_res.model_master_id,model_master.model_json
        FROM simulation_req_res
        INNER JOIN model_master ON model_master.model_master_id=simulation_req_res.model_master_id 
        WHERE status='new'"""         
cur.execute(query)
print_row(cur)

def runDocker():
    # os.system('cmd /c "C:\Program Files\Docker\Docker\Docker Desktop.exe"')
    # os.system('cmd /c "docker run --rm python-hello-world"')
    res=docker.run("python-hello-world", remove=True)
    print(res)

runDocker()