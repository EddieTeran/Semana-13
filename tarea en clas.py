# crea una funcion para convertir grados centigrados a grados fahrenheit, a grados kelvin
# fahrenheit = (9/5)*(gradcent)+32
#kelvin 273.15 + grad_cent
def cent_a_fahr(grad_cent):
    fahrenheit = (9 / 5) * (grad_cent) + 32
    return fahrenheit

grad_cent = 30
fahrenheit = cent_a_fahr(grad_cent)
print(f"{grad_cent} °C es igual a {fahrenheit} °F.")

kelvin = 273.15 + grad_cent
print(f"{grad_cent} °C es igual a {kelvin} °K.")

