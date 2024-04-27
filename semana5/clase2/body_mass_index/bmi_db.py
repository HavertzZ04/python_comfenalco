#range = el rango de bmi en el que el usuario esta para ser catalogado
#status = segun el rango se asigna el estado del usuario

bmi_diccionary = {
    "malnutrition" : {
        "range": [0, 18],
        "status": "Malnutrition"
    },
    "normal": {
        "range": [18.5, 24.9],
        "status": "Normal"
    },
    "overweight": {
        "range": [25, 29.9],
        "status": "Overweight"
    }, 
    "obesity_1": {
        "range": [30, 34.9],
        "status": "Obesity Type 1"
    }, 
    "obesity_2": {
        "range": [35, 39.9],
        "status": "Obesity Type 2"
    }, 
    "extreme": {
        "range": [40, 200], #BMI world record 185.5 - Jon Brower Minnoch.
        "status": "Extreme Obesity"
    }  
}

