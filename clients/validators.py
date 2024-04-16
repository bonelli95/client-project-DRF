def valid_tin(tin_number):
    return len(tin_number) <= 13

def valid_name(name):
    return name.isalpha()

def valid_pin(pin_number):
    return len(pin_number) <= 9

def valid_cell(cell_number):
    return len(cell_number) > 14