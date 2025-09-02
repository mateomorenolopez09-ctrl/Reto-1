# Programa para clasificar niveles de hemoglobina




N=int(input("ingrese el nuemro de personas a consultar"))
# inicializamos contadoras
h_bajos=0 # Cuantos hombres tienen hemoglobina baja
h_normal=0
h_alta=0
m_bajos=0
m_normal=0
m_alta=0
hemoglobinaH=0
hemoglobinaM=0
NH=0
NM=0
promedioH=0
promedioM=0

for i in range(N):
   genero = int(input("ingrese su genero (1. Masculno, 2. Femenino)"))
   hemoglobina=float(input("ingrese su nivel de hemoglobina"))
   
   if genero == 1:
       if hemoglobina <= 12.2:
           m_bajas+=1
       elif hemoglobina >=12.2 and hemoglobina <=16.2 :
           m_normal+=1
       else:
           m_alta+=1
if genero ==2: # si es mujer
           if hemoglobina < 12.2:
               h_bajos+=1
           elif hemoglobina >=12.6 and hemoglobina <=16.2:
               h_normal+=1
           else:
               h_alta+=1
hemoglobinaH=hemoglobinaH+hemoglobina # suma de hemoglobina en hombres
hemoglobinaM=hemoglobinaM+hemoglobina # suma de hemoglobina en mujeres
promedioH=hemoglobinaH/NH # promedio de hemoglobona en hombres
promedioM=promedioM/NM # promedio de hemoglobina en mujeres
print("El promedio de hemoglobina en hombres es:", promedioH)   # Mostrara el promedio de hempoglobina en hombre

print("El promedio de hemoglobina en mujeres es:", promedioM) # MOstrar el promedio de hemoglobina en mujeres 

  
  