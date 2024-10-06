import os, sys


def get_translations(language):
    translations = {
    "es": {
        "gender": "¿Cual es tu género? \n1.Hombre\n2.Mujer\n3.Hombre afeminado\n4.Dama con Rama",
        "weight": "¿Cuanto pesas?",
        "tam": "¿Tasa máxima de alcoholemia permitida? \n1. 0,5 g/L\n2. 0,3 g/L (Nóveles y profesionales)",
        "drink": "¿Que quieres beber hoy? \n1.Cervecilla \n2.Vino \n3.Destilados \n4.Absenta"
    },
    "en": {
        "gender": "¿What's your gender? \n1.Man\n2.Woman\n3.Tomboy\n4.Surprise girl",
        "weight": "¿What's your weight?",
        "tam": "¿Maximum alcohol tax allowed? \n1.0,5 g/L\n2.0,3 g/L (New driver and professionals)",
        "drink": "¿What are you gonna drink? \n1.Beer \n2.Wine \n3.Spirits \n4.Absinthe"
    },
    "ca": {
        "gender": "¿Quin es el teu génere? \n1.Home\n2.Dona\n3.Home afeminat\n4.Dona amb pirola",
        "weight": "¿Cuanto pesas?",
        "tam": "¿Tasa máxima de alcoholemia permessa? \n1.0,5 g/L\n2.0,3 g/L (Novel i professionals)",
        "drink": "¿Que vols beure? \n1.Birreta \n2.Vinet \n3.Destilat \n4.Absenta"
    },
   }
    return translations.get(language, translations["es"])


def data(gender, weight, tam, drink):
    if gender == 1 or gender == 4:
        k = 0.7
    elif gender == 2 or gender == 3:
        k = 0.6
    
    if tam == 1:
        tma = 0.5
    elif tam == 2:
        tma = 0.3

    wh = weight

    if drink == 1:
        grad = 4.5
    elif drink == 2:
        grad = 11
    elif drink == 3:
        grad = 35
    elif drink == 4:
        grad = 90

    return k, tma, wh, grad

def calc(k, tma, wh, hundred, density, grad):

    cai  = (tma*k*wh*hundred)/(density * grad)
    return cai



