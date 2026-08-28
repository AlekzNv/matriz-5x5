Cine=[  
    ["libre ", "libre ", "libre" ],
    ["libre ", "libre ", "libre" ],
    ["libre ", "libre ", "libre" ],
]

personas= int (input("Ingrese el numero de personas que van a asistir al cine."))
contador=0

while contador<personas:
    fila= int (input("Ingrese la fila."))
    columna= int (input("Ingrese columna."))
    Cine[fila][columna]="ocupado"
    contador = contador +1

print ("Estado de los acientos")
for fila in Cine:
    print(fila)