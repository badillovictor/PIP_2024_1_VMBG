
if __name__ == '__main__':
    alumnos = [
        ['Clemente', 1],
        ['Cristobal', 17],
        ['Ana', 5],
        ['Aldama', 2],
        ['Alan', 54],
        ['Melo', 92],
        ['Aquino', 21],
        ['Victor', 37],
        ['Segoviano', 75],
        ['Jeremy', 84],
        ['Carlota Man', 43],
        ['Natalia', 72],
        ['Roodrigo', 48],
        ['Miguel', 40],
        ['Amando', 69],
        ['Raul', 39],
        ['Lexiss', 12],
        ['Sofia', 11],
        ['Cervantes', 9],
        ['Emmanuel', 99],
        ['PaniaguaGOD', 42],
        ['ShekoGOD', 13],
        ['Issac', 61]
    ]
    with open('../Unidad 3/Archivos/archivo.csv', 'w') as file:
        for persona in alumnos:
            line = '{},{}\n'.format(persona[0], persona[1])
            file.write(line)