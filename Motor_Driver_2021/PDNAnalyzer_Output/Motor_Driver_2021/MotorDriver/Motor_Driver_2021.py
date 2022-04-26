designFile = "C:/Users/Gabriel/OneDrive/Documentos/Trabalhos IME/Extras/RoboIME/SSL/SSL-Hardware/Motor_Driver_2021/PDNAnalyzer_Output/Motor_Driver_2021/odb.tgz"

powerNets = ["VCC"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("CON-MOTOR", "3") ],
"ground_pins": [ ("CON-MOTOR", "4") ],
"voltage": 12.6,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("Q2_MAHB", "1"), ("Q2_MAHB", "2"), ("Q2_MAHB", "3") ],
"ground_pins": [ ("CON-MOTOR", "4") ],
"current": 8,
"Rpin": 0.01875,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("Q2_MBHB", "3"), ("Q2_MBHB", "2"), ("Q2_MBHB", "1") ],
"ground_pins": [ ("CON-MOTOR", "4") ],
"current": 8,
"Rpin": 0.01875,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("CON-MOTOR", "3") ],
"ground_pins": [ ("Q1_MAHB", "1"), ("Q1_MAHB", "2"), ("Q1_MAHB", "3") ],
"current": 8,
"Rpin": 0.01875,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("CON-MOTOR", "3") ],
"ground_pins": [ ("Q1_MBHB", "1"), ("Q1_MBHB", "2"), ("Q1_MBHB", "3") ],
"current": 8,
"Rpin": 0.01875,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
