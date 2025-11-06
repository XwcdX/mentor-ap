class UnderZeroError(Exception):
    pass

def underZero(h):
    if h < 0:
        raise UnderZeroError("Day cannot be negative")
    return h
    
try:
    h = underZero(int(input()))
    h /= 0
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Harus berupa angka")
except UnderZeroError as e:
    print(e)
except Exception as e:
    print(e)
    
    
def ran(*param):
    if len(param) == 1:
        start = 0
        end = param[0]
        move = 1
    elif len(param) == 2:
        start, end = param
        move = 1
    elif len(param) == 3:
        start, end, move = param
    else:
        raise ValueError("Jumlah Argumen Salah")
    
    output = []
    if start > end:
        while start > end:
            output.append(start)  
            start += move
    else:
        while start < end:
            output.append(start)  
            start += move
            
    return output

print(list(range(11, 0, -2)))