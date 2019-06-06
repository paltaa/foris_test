#Decisiones

##Argparse
En general he hecho muchos scripts de python que se ejecutan mediante cli, por lo que usar argparse para recordar su
correcto funcionamiento siempre es útil.

##Enfoque de los datos:
Primero me gusta estructurar la informacion de una manera util y práctica es por eso de la funcion file_to_dict
que me devuelve un diccionario bien definido que puedo usar para generar otro tipo de reportes.

Una vez tengo los datos bien estructurados para poder trabajar uso la siguiente funcion dict_list_to_presence_minutes_report,
con la que transformo mi diccionario en la lista de strings que conforman el informe pedido.

##Testing:

Existiendo solamente 2 casos, generé 2 tests por función, el caso vacío y el caso conocido, además del caso en el que el
archivo con los inputs no existe, devolviendo un 0
