

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
