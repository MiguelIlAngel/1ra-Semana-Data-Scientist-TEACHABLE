import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D')

# ----- PREGUNTAS SEMILLA -----

# ¿Cuál es el impacto económico del problema?
'''
Según el estudio "Cost of Turnover" del Center for American Progress:

* El coste de la fuga de los empleados que ganan menos de 30000 es del 16,1% de su salario

* El coste de la fuga de los empleados que ganan entre 30000-50000 es del 19,7% de su salario

* El coste de la fuga de los empleados que ganan entre 50000-75000 es del 20,4% de su salario

* El coste de la fuga de los empleados que ganan más de 75000 es del 21% de su salario
'''

# Creamos una nueva variable salario_ano del empleado
df['salario_ano'] = df.salario_mes.transform(lambda x: x*12)
#print(df[['salario_mes','salario_ano']])

'''
      salario_mes  salario_ano  # Mostrar salario_mes y salario_ano
id                              # Se muestra lo que gana un empleado al mes y al año
1            5993        71916  
2            5130        61560
4            2090        25080
5            2909        34908
7            3468        41616
...           ...          ...
2061         2571        30852
2062         9991       119892
2064         6142        73704
2065         5390        64680
2068         4404        52848
'''

# Calculamos el impacto económico de cada empleado si deja la empresa

#Lista de condiciones
condiciones = [(df['salario_ano'] <= 30000),                               # 16.1% de su salario = 0.161
               (df['salario_ano'] > 30000) & (df['salario_ano'] <= 50000), # 19.7% de su salario = 0.197
               (df['salario_ano'] > 50000) & (df['salario_ano'] <= 75000), # 20.4% de su salario = 0.204
               (df['salario_ano'] > 75000)]                                # 21% de su salario = 0.21

#Lista de resultados
resultados = [df.salario_ano * 0.161, df.salario_ano * 0.197, df.salario_ano * 0.204, df.salario_ano * 0.21]

#Aplicamos select
df['impacto_abandono'] = np.select(condiciones,resultados, default = -999)

print(df)

# LO IMPORTANTE
'''
            salario_ano     impacto_abandono
id                                              
1             71916         14670.864  
2             61560         12558.240  
4             25080          4037.880  
5             34908          6876.876  
7             41616          8198.352  
...           ...                 ...      
2061          30852          6077.844  
2062          119892        25177.320  
2064          73704         15035.616  
2065          64680         13194.720  
2068          52848         10780.992
'''