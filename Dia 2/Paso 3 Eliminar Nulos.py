# Como vimos en el PASO 2, vamos a eliminar las variables "años en puesto" y "conciliación" porque tienen demasiados nulos

import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'

# df = df.drop(columns = ['anos_en_puesto', 'conciliacion']) # La diferencia con la línea de abajo es que la eliminacion es temporal
df.drop(columns = ['anos_en_puesto', 'conciliacion'], inplace = True) # Eliminar columnas con demasiados nulos, inplace = True para que sea permanente

# Para ver si se eliminaron las columnas
print(df.isna().sum().sort_values(ascending=False)) # df.isna() -> DataFrame con valores faltantes, df.isna().sum() -> Suma de valores faltantes por columna, df.isna().sum().sort_values(ascending=False) -> Ordenar de mayor a menor

'''
sexo                        199
educacion                   101
satisfaccion_trabajo         76
implicacion                  18
edad                          0
mayor_edad                    0
anos_desde_ult_promocion      0
anos_compania                 0
num_formaciones_ult_ano       0
anos_experiencia              0
nivel_acciones                0
horas_quincena                0
satisfaccion_companeros       0
evaluacion                    0
incremento_salario_porc       0
horas_extra                   0
estado_civil                  0
num_empresas_anteriores       0
salario_mes                   0
abandono                      0
puesto                        0
nivel_laboral                 0
satisfaccion_entorno          0
empleados                     0
carrera                       0
distancia_casa                0
departamento                  0
viajes                        0
anos_con_manager_actual       0'''
