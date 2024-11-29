def map_coordinates(husklens_x, husklens_y):
    # Dimens�es da Husklens
    husklens_width = 320
    husklens_height = 240
    
    # Dimens�es do LCD
    lcd_width = 240
    lcd_height = 240
    
    # Mapeia as coordenadas
    lcd_x = int(husklens_x * lcd_width / husklens_width)
    lcd_y = int(husklens_y * lcd_height / husklens_height)
    
    return lcd_x, lcd_y

#test
husklens_x, husklens_y = 160, 120
lcd_x, lcd_y = map_coordinates(husklens_x, husklens_y)
print(f'Coordenadas Husklens: ({husklens_x}, {husklens_y})')
print(f'Coordenadas LCD: ({lcd_x}, {lcd_y})')