designFile = "C:/Users/Gabriel/OneDrive/Documentos/Trabalhos IME/Extras/RoboIME/SSL/SSL-Hardware/SSL-Motherboard/PDNAnalyzer_Output/SSL-Motherboard/odb.tgz"

powerNets = ["VBAT"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("Q1", "5"), ("Q1", "6"), ("Q1", "7"), ("Q1", "8"), ("Q1", "9") ],
"ground_pins": [ ("BAT", "1") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R11_M0", "2") ],
"ground_pins": [ ("C1_M0", "3") ],
"current": 8,
"Rpin": 0.0125,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("R11_M1", "2") ],
"ground_pins": [ ("C1_M1", "3") ],
"current": 8,
"Rpin": 0.0125,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R11_M2", "2") ],
"ground_pins": [ ("C1_M2", "3") ],
"current": 8,
"Rpin": 0.0125,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("R11_M3", "2") ],
"ground_pins": [ ("C1_M3", "3") ],
"current": 8,
"Rpin": 0.0125,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("RD1", "2") ],
"ground_pins": [ ("CON_DM1", "0") ],
"current": 4,
"Rpin": 0.025,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("P1", "6"), ("P1", "5"), ("P1", "4"), ("P1", "3"), ("P1", "2"), ("P1", "1") ],
"ground_pins": [ ("P1", "12"), ("P1", "11"), ("P1", "10"), ("P1", "9"), ("P1", "8"), ("P1", "7") ],
"current": 4,
"Rpin": 0.15,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.0015},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
