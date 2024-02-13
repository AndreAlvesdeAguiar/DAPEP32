API ESP 32 - https://github.com/AndreAlvesdeAguiar/PROJETO_ESP32/blob/main/02_2024

Local - http://192.168.15.25/data
Resposta - {"temperature":[28.60000038,"°C"],"humidity":[60.40000153,"%"],"moisture":[4095,"%"],"moisture2":[191,"%"]}

------------Inicio
Abra um terminal

#docker compose up --build

Em outro terminal - vamos acessar o postgres para ver os dados gravados.
Descobrindo qual CONTAINER ID O docker está rodando

#docker ps

andre@andre-Inspiron-5557:~/Documentos/py_lab$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                    NAMES
a16ae65b6134   py_lab-python_script   "python script.py"       20 minutes ago   Up 20 minutes                            py_lab-python_script-1
968595119d13   postgres:latest        "docker-entrypoint.s…"   20 minutes ago   Up 20 minutes   0.0.0.0:5432->5432/tcp   py_lab-db-1

#docker exec -it 968595119d13 bash

Indicativo de acesso 'root@968595119d13:/#'

Com isso acessamos o container.
Agora precisamos acessar o postgres

#psql -U postgres -d my_database

Indicativo de acesso 'my_database=#' 

Buscar TODOS na TABELA CRIADA
# SELECT * FROM sensor_data;

retorno

    id  |                                                  data                                                           
---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
    1 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [0, "%"], "temperature": [28, "°C"]}
    2 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [4095, "%"], "temperature": [28, "°C"]}
    3 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [755, "%"], "temperature": [28, "°C"]}
    4 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [1177, "%"], "temperature": [28, "°C"]}
    5 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [4095, "%"], "temperature": [28, "°C"]}
    6 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [4095, "%"], "temperature": [28, "°C"]}
    7 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [4095, "%"], "temperature": [28, "°C"]}
    8 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [4095, "%"], "temperature": [28, "°C"]}
    9 | {"humidity": [62.59999847, "%"], "moisture": [4095, "%"], "moisture2": [213, "%"], "temperature": [28, "°C"]}
