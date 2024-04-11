import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'

df.info() # Información del DataFrame

# Nos muestra la cantidad de filas y columnas, el tipo de datos de cada columna y la cantidad de valores no nulos

 #    Column                    Non-Null Count  Dtype  
#--   ------                    --------------  -----  
 #0   edad                      1470 non-null   int64  
 #1   abandono                  1470 non-null   object 
 #2   viajes                    1470 non-null   object 
 #3   departamento              1470 non-null   object 
 #4   distancia_casa            1470 non-null   int64  
 #5   educacion                 1369 non-null   object
 #6   carrera                   1470 non-null   object
 #7   empleados                 1470 non-null   int64
 #8   satisfaccion_entorno      1470 non-null   object
 #9   sexo                      1271 non-null   float64
 #10  implicacion               1452 non-null   object
 #11  nivel_laboral             1470 non-null   int64
 #12  puesto                    1470 non-null   object
 #13  satisfaccion_trabajo      1394 non-null   object
 #14  estado_civil              1470 non-null   object
 #15  salario_mes               1470 non-null   int64
 #16  num_empresas_anteriores   1470 non-null   int64
 #17  mayor_edad                1470 non-null   object
 #18  horas_extra               1470 non-null   object
 #19  incremento_salario_porc   1470 non-null   int64
 #20  evaluacion                1470 non-null   object
 #21  satisfaccion_companeros   1470 non-null   object
 #22  horas_quincena            1470 non-null   int64
 #23  nivel_acciones            1470 non-null   int64
 #24  anos_experiencia          1470 non-null   int64
 #25  num_formaciones_ult_ano   1470 non-null   int64
 #26  conciliacion              459 non-null    object
 #27  anos_compania             1470 non-null   int64
 #28  anos_en_puesto            232 non-null    float64
 #29  anos_desde_ult_promocion  1470 non-null   int64
 #30  anos_con_manager_actual   1470 non-null   int64
