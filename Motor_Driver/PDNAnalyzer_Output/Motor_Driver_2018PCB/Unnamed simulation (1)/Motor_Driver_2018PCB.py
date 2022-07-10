designFile = "C:/Users/Gabriel/OneDrive/Documentos/Trabalhos IME/Extras/RoboIME/SSL_Electronic_Boards/Motor_Driver_2018/PDNAnalyzer_Output/Motor_Driver_2018PCB/odb.tgz"

powerNets = ["VCC"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("CON-MC2", "3") ],
"ground_pins": [ ("CON-MC2", "4") ],
"voltage": 12.6,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("IC?", "9"), ("IC?", "4"), ("IC?", "3"), ("IC?", "17"), ("IC?", "18"), ("IC?", "23") ],
"ground_pins": [ ("IC?", "12"), ("IC?", "7"), ("IC?", "10"), ("IC?", "11"), ("IC?", "25"), ("IC?", "24"), ("IC?", "20"), ("IC?", "26") ],
"current": 6,
"Rpin": 0.114285714285714,
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
