from data.variables import diccionario_utters

# PRUEBA DE USO DENTRO DE main.py

idioma = 'en'

texto = """Gracias por compartir todo esto conmigo. Si hay algo más que recuerdes y te gustaría añadir, puedes hacerlo ahora. Antes de que continuemos, me gustaría hacerte una pregunta más. ¿Crees que hubo algún motivo detrás de la agresión o el comportamiento de esas personas?"""

utter = diccionario_utters[idioma.upper()][texto]

with open (f"data/audios/{idioma.upper()}/{utter}.txt") as fichero:
    doc = fichero.read()

print(doc)
