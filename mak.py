from opcua import Server

from random import randint

import time

server=Server()

url="opc.tcp://localhost:4840"

server.set_endpoint(url)

name="MAKZPRO"

addspace=server.register_namespace(name)

node=server.get_objects_node()

Param=node.add_object_type(addspace, "Parameters")

Machine1Temp=Param.add_variable(addspace, "Temperature1", 0)

Machine2Temp=Param.add_variable(addspace, "Temperature2", 0)

Machine1Press=Param.add_variable(addspace, "Pressure1", 0)

Machine2Press=Param.add_variable(addspace, "Pressure2", 0)

Machine1Temp.set_writable()

Machine2Temp.set_writable()

Machine1Press.set_writable()

Machine2Press.set_writable()



server.start()



print("Server started at {}".format(url))

while True:

    Temperature1 = int(10   )

    Temperature2 = randint(10,50)

    Pressure1 = randint(10,50)

    Pressure2 = randint(100,999)

    print(Temperature1,Temperature2,Pressure1,Pressure2)

    

    Machine1Temp.set_value(Temperature1)

    Machine2Temp.set_value(Temperature2)

    Machine1Press.set_value(Pressure1)

    Machine2Press.set_value(Pressure2)



    

    time.sleep(2)