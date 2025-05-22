# Proyecto 01 Generar el PDF de un presupuesto

from datetime import datetime
from fpdf import FPDF
import time

# Capturar la información del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")
fecha_actual = datetime.now().strftime("%d/%m/%Y")
proyecto = input("Digita la descripción del proyecto: ")
horas_estimadas =input("Digita la cantidad de horas estimadas: ")
valor_hora = input("Digita el valor de la hora trabajada: ")
tiempo_estimado = input("Digita el plazo estimado:  ")

# Imprimir la información
print(nombre_cliente)
print(fecha_actual)
print(proyecto)
print(horas_estimadas)
print(valor_hora)
print(tiempo_estimado)

# Calculando el valor total del proyecto

valor_total = int(horas_estimadas) * int(valor_hora)
valor_total


# Separando la parte entera y centavos

valor_formateado = "{:,.2f}".format(valor_total)


# Generando el archivo PDF del presupuesto

pdf = FPDF(format='letter')
pdf.add_page()
pdf.image("template.png",0,0,216,279)
pdf.set_font("Helvetica", size=15)

pdf.text(55,  110, nombre_cliente)
pdf.text(55,  100, fecha_actual)
pdf.text(120, 142, proyecto)
pdf.text(120, 156, horas_estimadas)
pdf.text(120, 170, valor_hora)
pdf.text(120, 184, tiempo_estimado)
pdf.text(148, 200, str(valor_formateado))

pdf.output("presupuesto.pdf")


