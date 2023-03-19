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

def runDocker():

    # os.system('cmd /c "C:\Program Files\Docker\Docker\DockerCli.exe -SwitchtoLinuxEngine"')
    # os.system('cmd /c "docker run --rm python-hello-world"')

    """
    To check if the image is present in the local machine and pull the image if not present
    """
    try:
        docker.image.inspect("raghusesha/neuroidv2.x:litedemo_l4l5")
    except:
        docker.pull("raghusesha/neuroidv2.x:litedemo_l4l5")

    # res=docker.run("raghusesha/neuroidv2.x:litedemo_l4l5",publish=[("5910:5900","5911:5901")],tty=True)
    # print(res)

    # Running the conatiner
    if docker.container.inspect("neuroid2.xcont1"):
        print("Container already exists...\nStarting Container...")
        os.system('cmd /c "docker start -i neuroid2.xcont1"')
    else:
        print("Container does not exist...\nRunning Container...")
        os.system('cmd /c "docker run -it -p 5910:5900 -p 5911:5901"' 
                    '" --name neuroid2.xcont1 raghusesha/neuroidv2.x:litedemo_l4l5 /bin/bash"')
    # Do tasks on Docker

    #Stop the container
    # print("Stopping Container...")
    # docker.stop("neuroid2.xcont1")

#Checking if new entries are added to the table
# i=0
# while True:
#     cur=conn.cursor()
#     #Initial Query to get the existing number of rows
#     cur.execute(query)
#     print(cur)
#     #Rolls back to start
#     conn.rollback()
#     time.sleep(refresh_mins*60)
#     if cur.rowcount > 0:
#         print("New entry detected")
#         print_row(cur)
#         runDocker()
#     print("Checking for new entries...",i,"times")
#     i+=1
# conn.close()

runDocker()
