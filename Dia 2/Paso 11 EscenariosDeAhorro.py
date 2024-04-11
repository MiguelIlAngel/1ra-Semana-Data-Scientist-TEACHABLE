import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D')

# ----- CREACIÓN DE ESCENARIOS DE AHORRO -----
# Preguntas respecto al ahorro de costes

# ¿Cuánto dinero podríamos ahorrar fidelizando mejor a nuestros empleados?

# Reducir el abandono de empleados al 10% 
print(f"Reducir un 10% la fuga de empleados nos ahorraría {int(coste_total * 0.1)}$ cada año.")
# Reducir un 10% la fuga de empleados nos ahorraría 271900$ cada año.


# Reducir el abandono de empleados al 20%
print(f"Reducir un 20% la fuga de empleados nos ahorraría {int(coste_total * 0.2)}$ cada año.")
# Reducir un 20% la fuga de empleados nos ahorraría 543801$ cada año.


# Reducir el abandono de empleados al 30%
print(f"Reducir un 30% la fuga de empleados nos ahorraría {int(coste_total * 0.3)}$ cada año.")
# Reducir un 30% la fuga de empleados nos ahorraría 815701$ cada año.


# SEGUIR TRAZANDO ESTRATEGIAS ASOCIADAS A LOS INSIGHTS DE ABANDONO DE EMPLEADOS

# Habíamos visto que los representantes de ventas son el puesto que más se van. ¿Tendría sentido hacer un plan específico para ellos?
# ¿Cual sería el coste ahorrado si disminuimos la fuga un 30%?
# Primero vamos a calcular el % de representantes de ventas que se han ido el año pasado
total_repre_pasado = len(df.loc[df.puesto == 'Sales Representative']) # len = longitud, df.loc = filtrar, puesto = 'Sales Representative' 
abandonos_repre_pasado = len(df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 1)]) # len = longitud, df.loc = filtrar, puesto = 'Sales Representative', abandono = 1  
porc_pasado = abandonos_repre_pasado / total_repre_pasado # Porcentaje de abandono de representantes de ventas
print(porc_pasado) # 0.39 -> 39% de los representantes de ventas se fueron el año pasado

# Ahora vamos a estimar cuantos se podrían ir este año
total_repre_actual = len(df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 0)]) # len = longitud, df.loc = filtrar, puesto = 'Sales Representative', abandono = 0
se_iran = int(total_repre_actual * porc_pasado) # int = entero, total_repre_actual = total de representantes de ventas actuales, porc_pasado = porcentaje de abandono de representantes de ventas
print(se_iran) # 19 -> 19 representantes de ventas se irán este año 

# Sobre ellos cuantos podemos retener (30%) y cuanto dinero puede ahorrarse 
retenemos = int(se_iran * 0.3) # int = entero, se_iran = representantes de ventas que se irán este año, 0.3 = 30% de los representantes de ventas que se irán este año  
ahorramos = df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 0),'impacto_abandono'].sum() * porc_pasado * 0.3 # df.loc = filtrar, puesto = 'Sales Representative', abandono = 0, impacto_abandono = columna con el impacto económico sumados, porc_pasado = porcentaje de abandono de representantes de ventas, 0.3 = 30% de los representantes de ventas que se irán este año
print(f'Podemos retener {retenemos} representantes de ventas y ello supondría ahorrar {ahorramos}$.') 
# Podemos retener 5 representantes de ventas y ello supondría ahorrar 104000.0$.
#Este dato también es muy interesante porque nos permite determinar el presupuesto para acciones de retención por departamento o perfil.
#Ya que sabemos que podemos gastarnos hasta 37.000$ sólo en acciones específicas para retener a representantes de ventas y se estarían pagando sólas con la pérdida evitada