import os, sys

def get_translations(language):
    translations = {
        "es": {
            "title": "Calculadora Bebidas a Tomar Antes de la Multa",  
            "select_language": "Selecciona Idioma:",
            "gender": "¿Cual es tu género? ",
            "weight": "¿Cuanto pesas?",
            "tam": "¿Tasa máxima de alcoholemia permitida?",
            "drink": "¿Que quieres beber hoy?",
            "result": "Puedes consumir:",
            "alcohol_pure": "ml de alcohol puro", 
            "gender_options": ["Hombre", "Mujer", "Hombre afeminado", "Dama con Rama"],
            "tam_options": ["0,5 g/L", "0,3 g/L (Nóveles y profesionales)"],
            "drink_options": ["Cervecilla", "Vino", "Destilados", "Absenta"],
        },
        "en": {
            "title": "Drink Calculator Before a Penalty",  
            "select_language": "Select Language:",
            "gender": "What's your gender? ",
            "weight": "What's your weight?",
            "tam": "Maximum alcohol tax allowed?",
            "drink": "What are you gonna drink?",
            "result": "You can consume:",
            "alcohol_pure": "ml of pure alcohol",  
            "gender_options": ["Man", "Woman", "Effeminate Man", "Lady with Branch"],
            "tam_options": ["0.5 g/L", "0.3 g/L (Novice and Professionals)"],
            "drink_options": ["Beer", "Wine", "Spirits", "Absinthe"],
        },
        "ca": {
            "title": "Calculadora Begudes a Beure Abans de la Multa",  
            "select_language": "Selecciona Idioma:",
            "gender": "Quin es el teu gènere? ",
            "weight": "Quin és el teu pes?",
            "tam": "Tasa màxima d'alcoholemia permesa?",
            "drink": "Què vols beure?",
            "result": "Pots consumir:",
            "alcohol_pure": "ml d'alcohol pur", 
            "gender_options": ["Home", "Dona", "Home afeminat", "Dama amb Rama"],
            "tam_options": ["0,5 g/L", "0,3 g/L (Nové i professionals)"],
            "drink_options": ["Cervesa", "Vi", "Destil·lats", "Absenta"],
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

def calcSelectedDrinks(cai, grad):
    if grad == 4.5:
        return calculate_beer(cai, grad)
    elif grad == 11:
        return calculate_wine(cai, grad)
    elif grad == 35:
        return calculate_spirits(cai, grad)
    elif grad == 90:
        return calculate_absinthe(cai, grad)

def calculate_beer(cai, grad):
    volumQuinto = 200
    volumMediana = 330
    volumCana = 210

    numberOfQuintos = cai / volumQuinto
    numberOfMediana = cai / volumMediana
    numberOfCanas = cai / volumCana

    return numberOfQuintos, numberOfMediana, numberOfCanas

def calculate_wine(cai, grad):
    wineCapacity = 150
    numberOfWine = cai / wineCapacity
    return numberOfWine

def calculate_spirits(cai, grad):
    shotCapacity = 30
    cubataCapacity = 480

    numberOfShots = cai /  shotCapacity
    numberOfCubatas = cai / cubataCapacity

    return numberOfShots, numberOfCubatas

def calculate_absinthe(cai, grad):
    absinthCapacity = 30
    numberOfAbsinths = cai / absinthCapacity
    return numberOfAbsinths
