a = "Brian"
b = 22
c = "Mexico"
#Esta funcion permite imprimir el valor de las variables dentro de la SALIDA/IMPRESION 
#Pero se debe de poner los valores de acuerdo a como se quiere que aparezcan
print("Me llamo {} y mi edad es {} ".format(a,b))

#Esta permite poner las variables (parametros) desacomodados y se pueden ubicar con los indices de estos:
print("Me llamo {0} y mi edad es {1} ".format(a,b))

#La siguiente permite asignar una clave a cada variable:
print("Me llamo {nombre} y mi edad es {edad} ".format(nombre=a,edad=b))

#La siguiente prmite crear con un formato:
print(f"Me llamo {a} y mi edad es {b} y soy de {c}")