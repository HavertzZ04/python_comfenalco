# ejercicio 
'''
- definir una variable que se llame sentencia_1 con valor True, 
- definir otra variable que se llame sentencia_2 con valor False

-- not sentencia_1 que salio? T/F
-- not sentencia_1 and sentencia_2 que salio? T/F
-- not sentencia_2 or sentencia_1 que salio? T/F
-- not (sentencia_2 or not sentencia_1) que salio? T/F
'''

# Definir las variables sentencia_1 y sentencia_2
sentencia_1 = True
sentencia_2 = False

# Evaluar las expresiones y mostrar los resultados
resultado_1 = not sentencia_1
resultado_2 = not sentencia_1 and sentencia_2
resultado_3 = not sentencia_2 or sentencia_1
resultado_4 = not sentencia_2 or not sentencia_1

# Mostrar los resultados
print("not sentencia_1:", resultado_1)  
print("not sentencia_1 and sentencia_2:", resultado_2)  
print("not sentencia_2 or sentencia_1:", resultado_3)  
print("not sentencia_2 or not sentencia_1:", resultado_4) 