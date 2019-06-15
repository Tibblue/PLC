weather = [{
    'date':'2 Dom',
    'prev_txt': 'Ceu nublado por nuvens altas',
    'temp_min': 13,
    'temp_max':28,
    'uv':8
},{
    'date':'3 Seg',
    'prev_txt': 'Ceu pouco nublado',
    'temp_min': 11,
    'temp_max': 27,
    'uv':9
},{
    'date':'4 Ter',
    'prev_txt': 'Ceu limpo',
    'temp_min': 9,
    'temp_max': 31,
    'uv':9
}]


def conselhos_da_avo(weather):
    dia = '2'
    for previsao in weather:
        date = previsao['date'].split()[0]
        if date == dia:
            if previsao['temp_min'] < 15:
                print('leva um casaco')
            if previsao['uv'] > 7:
                print("sai do sol")

conselhos_da_avo(weather)