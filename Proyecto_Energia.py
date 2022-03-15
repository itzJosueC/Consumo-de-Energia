consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_coca_codo_g + tot_sopladora_g
sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
oriente = ('0')

print("""
    ===============================
    ADMINISTRADOR MATRIZ ELECTRICA
    ===============================
    """)
print('<1>. Total de MWh en Planta y Ciudad ')
print('<2>. Total de energia dada ')
print('<3>. Dinero Recaudado ')
print('<4>. Salir del programa')
opcion = input('Elija la opción que desee emplear: ')

if opcion == '4':
    print('Saliendo...')
    exit
    
elif opcion == '1':
    
    print("""
    ===============================
    Total de MWh en Planta y Ciudad
    ===============================
    """)
    print('Plantas:', 'Coca Codo Sinclair,', 'Sopladora.')
    n_planta = input('Ingrese el nombre de la planta: ')

    if n_planta == 'Coca Codo Sinclair':
        print('Ciudades:', 'Quito,', 'Guayaquil.')
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MWh de consumo en Coca Codo Sinclair, Quito: ', tot_coca_codo_q, 'Mwh')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de MWh de consumo en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'Mwh')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
    print()

    if n_planta == 'Sopladora':
        print('Ciudades:', 'Quito,', 'Guayaquil.', 'Loja.')
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MWh de consumo en Sopladora, Quito: ', tot_sopladora_q, 'Mwh')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de MWh de consumo en Sopladora, Guayaquil: ', tot_sopladora_g, 'Mwh')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
        elif n_ciudad == 'Loja':
            print('Total de MWh de consumo en Sopladora, Loja: ', tot_sopladora_l)
            print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
    print()
elif opcion == '2':
    print("""
    ===============================
    Total de energia dada a cada
    ciudad por cada planta
    ===============================
    """),

    print('Ciudades:', 'Guayaquil,', 'Quito,', 'Loja,', 'Nueva Loja,', 'Tena.')
    n_ciudad2 = input('Ingrese el nombre de la ciudad: ')

    if n_ciudad2 == 'Guayaquil':
        print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_g, 'Mwh')
        print('Total de MWh, Sopladora:', tot_sopladora_g, 'Mwh')
    elif n_ciudad2 == 'Quito':
        print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_q, 'Mwh')
        print('Total de MWh, Sopladora:', tot_sopladora_q, 'Mwh')
    elif n_ciudad2 == 'Loja':
        print('Total de MWh, Sopladora:', tot_sopladora_l, 'Mwh')
    else:
        print('Ninguna planta otorga energía la ciudad seleccionada')
    print()
elif opcion == '3':
    print("""
    ===============================
    $Dinero Recaudado$
    ===============================
    """),

    print('Regiones:', 'Costa,', 'Sierra,', 'Oriente.')
    n_region = input('Ingrese nombre de Región: ')
    
    print('Costa',)
    if n_region == 'Costa':
        print('Total Recaudado en la Región Costa: ', costa, '$')
    elif n_region == 'Sierra':
        print('Total Recaudado en la Región Sierra: ', sierra, '$')
    elif n_region == 'Oriente':
        print('Total Recaudado en el Oriente: ', oriente, '$')
