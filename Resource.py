##Law of coulumb
import math 

#1
# Dos pequeñas esferas identicamente cargadas, cada una con una masa de 3 × 10−2 kg, cuelgan en
#equilibrio. La longitud de cada cuerda es de 0.15 m y el angulo entre la vertical y la cuerda es de 5◦
#.Encuentre la magnitud de la carga sobre cada esfera.

# Definir las constantes y variables iniciales
k = 9e9    # Constante de Coulomb en N m^2/C^2
m = 3e-2   # Masa de cada esfera en kg
g = 9.81   # Aceleración debido a la gravedad en m/s^2
l = 0.15  # Longitud de cada cuerda en metros
theta = 5*math.pi/180  # Ángulo en radianes entre la cuerda y la vertical

# Calcular la magnitud de la carga en cada esfera
q = math.sqrt((m*g*l**2*math.sin(theta))/(k))

# Imprimir el resultado
print("La magnitud de la carga en cada esfera es:", q, "C")
'''
Un protón se mueve a 4,50 × 105 m/s en direcci´on horizontal, y entra en un campo el´ectrico vertical
uniforme con una magnitud de 9,60 × 103 N/C. Si ignora cualquier efecto gravitacional, determine
(a) el intervalo de tiempo requerido para que el prot´on recorra 5,00 cm horizontalmente, (b) su
desplazamiento vertical durante el intervalo de tiempo que viaja los 5,00 cm horizontalmente y
(c) las componentes horizontal y vertical de su velocidad despu´es de haber recorrido los 5,00 cm
horizontalmente.
'''
#a
velocidad_horizontal = 4.50e5 # m/s
distancia_horizontal = 5e-2 # m

# Cálculo del intervalo de tiempo
tiempo = distancia_horizontal / velocidad_horizontal

print("El intervalo de tiempo requerido para recorrer 5,00 cm horizontalmente es de: {:.2e} s".format(tiempo))
#b
magnitud_campo_electrico = 9.60e3 # N/C
carga_proton = 1.60e-19 # C
masa_proton = 1.67e-27 # kg
intervalo_tiempo = 1.11e-7 # s

# Cálculo de la fuerza eléctrica sobre el protón
fuerza_electrica = carga_proton * magnitud_campo_electrico

# Cálculo de la aceleración vertical del protón
aceleracion_vertical = fuerza_electrica / masa_proton

# Cálculo del desplazamiento vertical
desplazamiento_vertical = 0.5 * aceleracion_vertical * intervalo_tiempo**2

print("El desplazamiento vertical durante el intervalo de tiempo que viaja los 5,00 cm horizontalmente es de: {:.2e} m".format(desplazamiento_vertical))

#c
velocidad_horizontal = 4.50e5 # m/s
aceleracion_vertical = 9.22e11 # m/s^2
intervalo_tiempo = 1.11e-8 # s

# Cálculo de la velocidad vertical del protón
velocidad_vertical = aceleracion_vertical * intervalo_tiempo

print("La velocidad horizontal después de haber recorrido los 5,00 cm horizontalmente es de: {:.2e} m/s".format(velocidad_horizontal))
print("La velocidad vertical después de haber recorrido los 5,00 cm horizontalmente es de: {:.2e} m/s".format(velocidad_vertical))


#3 
'''
Encuentre el campo el´ectrico que genera un disco de radio R con densidad de carga superficial
positiva y uniforme, σ, en un punto a lo largo del eje del disco a una distancia d de su centro. Realice
la gr´afica de la magnitud del campo en funci´on de la distancia sobre el eje del disco (el eje es una
linea perpendicular al disco que pasa por su centro).

'''
import math

def electric_field(sigma, R, d):
    k = 1 / (4 * math.pi * 8.85e-12)
    E = k * (sigma * R**2) / (R**2 + d**2)**(3/2)
    return E


# Definimos las constantes
sigma = 2e-6    # C/m^2
R = 0.1         # m
d = 0.05        # m

# Calculamos el campo eléctrico en el punto deseado
E = electric_field(sigma, R, d)

# Mostramos el resultado
print("El campo eléctrico en el punto deseado es: ", E, " N/C")

#4
'''
 Una varilla uniformemente cargada de longitud L y carga total Q se encuentra a lo largo del eje x y el
centro de la varilla pasa por el eje y. Halle las componentes del campo el´ectrico en un punto P sobre
el eje y a una distancia d del origen. (b) ¿Cuales son los valores aproximados de las componentes
del campo cuando d  L?

'''



print("---------------------------")
import math

# Definimos las constantes
k = 9e9
q1 = 500e-9
q2 = -200e-9
q3 = 600e-9
x2 = 4e-2
y3 = 2e-2

# Calculamos la distancia entre las cargas
r13 = math.sqrt(x2**2 + y3**2)
r23 = math.sqrt((x2-4e-2)**2 + y3**2)

# Calculamos la fuerza eléctrica ejercida por cada carga sobre la carga q3
f13 = k * q1 * q3 / r13**2
f23 = k * q2 * q3 / r23**2

# Calculamos la fuerza resultante en términos de sus componentes x e y
fx = f13 + f23
fy = f13 * math.sin(math.atan(y3/x2)) - f23 * math.sin(math.atan(y3/(4e-2-x2)))

# Calculamos la magnitud y dirección de la fuerza resultante
f_res = math.sqrt(fx**2 + fy**2)
theta = math.degrees(math.atan(abs(fy/fx)))
if fx < 0 and fy > 0:
    theta = 180 - theta
elif fx < 0 and fy < 0:
    theta += 180
elif fx > 0 and fy < 0:
    theta = 360 - theta

# Imprimimos los resultados
print("Magnitud de la fuerza resultante: {:.2e} N".format(f_res))
print("Dirección de la fuerza resultante: {:.2f} grados".format(theta))
