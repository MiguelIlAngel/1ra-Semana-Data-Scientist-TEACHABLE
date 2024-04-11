# ANALISIS EXPLORATORIO DE DATOS (EDA) - PASO 6 "NUMERICAS"

import pandas as pd # Pandas, librería para manipulación de datos
import numpy as np # Numpy, librería para cálculos matemáticos
import matplotlib.pyplot as plt # Matplotlib, librería para gráficos
#%matplotlib inline # Comando para mostrar gráficos en el notebook (SOLO SE USA EN Jupyter Notebook)

df = pd.read_csv('C:/Users/Miguel/Desktop/Analista de Datos/Externo/1ra Semana Data Scientist TEACHABLE/Dia 1/AbandonoEmpleados.csv', sep = ';', index_col = 'id', na_values = '#N/D') #"df" -> DataFrame, cargar datos, SEParador = ';', INDICE = 'id', valores faltantes = '#N/D'

# Definimos gráficos para variables numéricas
def estadisticos_cont(num):
    #Calculamos describe
    estadisticos = num.describe().T
    #Añadimos la mediana
    estadisticos['median'] = num.median()
    #Reordenamos para que la mediana esté al lado de la media
    estadisticos = estadisticos.iloc[:,[0,1,8,2,3,4,5,6,7]]
    #Lo devolvemos
    return(estadisticos)

# Llamamos y mostramos a la función para calcular estadísticos de las variables numéricas
print(estadisticos_cont(df.select_dtypes(np.number)))

'''
                           count         mean  median          std     min     25%     50%     75%      max
edad                      1470.0    36.923810    36.0     9.135373    18.0    30.0    36.0    43.0     60.0
distancia_casa            1470.0     9.192517     7.0     8.106864     1.0     2.0     7.0    14.0     29.0
empleados                 1470.0     1.000000     1.0     0.000000     1.0     1.0     1.0     1.0      1.0   # 1 valor no tiene sentido
sexo                      1271.0     2.727773     3.0     0.720788     1.0     2.0     3.0     3.0      4.0   # 4 valores no tienen sentido
nivel_laboral             1470.0     2.063946     2.0     1.106940     1.0     1.0     2.0     3.0      5.0
salario_mes               1470.0  6502.931293  4919.0  4707.956783  1009.0  2911.0  4919.0  8379.0  19999.0
num_empresas_anteriores   1470.0     2.693197     2.0     2.498009     0.0     1.0     2.0     4.0      9.0
incremento_salario_porc   1470.0    15.209524    14.0     3.659938    11.0    12.0    14.0    18.0     25.0
horas_quincena            1470.0    80.000000    80.0     0.000000    80.0    80.0    80.0    80.0     80.0   # 0 desvío estándar
nivel_acciones            1470.0     0.793878     1.0     0.852077     0.0     0.0     1.0     1.0      3.0
anos_experiencia          1470.0    11.279592    10.0     7.780782     0.0     6.0    10.0    15.0     40.0
num_formaciones_ult_ano   1470.0     2.799320     3.0     1.289271     0.0     2.0     3.0     3.0      6.0
anos_compania             1470.0     7.008163     5.0     6.126525     0.0     3.0     5.0     9.0     40.0
anos_en_puesto             232.0     2.771552     3.0     0.705244     1.0     2.0     3.0     3.0      4.0
anos_desde_ult_promocion  1470.0     2.187755     1.0     3.222430     0.0     0.0     1.0     3.0     15.0
anos_con_manager_actual   1470.0     4.123129     3.0     3.568136     0.0     2.0     3.0     7.0     17.0
'''

# CONCLUSIONES:

# empleados solo tiene un valor, por lo que no aporta información --> eliminarla
# horas_quincena tiene un desvío estándar de 0, por lo que no aporta información --> eliminarla
# sexo tiene valores (4) que no tienen sentido, por lo que no aporta información --> eliminarla
# Los valores a imputar era el sexo, pero como lo vamos a eliminar, no hay nada que reemplazar

df.drop(columns = ['empleados','sexo','horas_quincena'], inplace = True) # Eliminar columnas con un solo valor, con valores que no tienen sentido y con desvío estándar de 0, inplace = True para que sea permanente

