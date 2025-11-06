def eval_expr(*args):
    op = args[0]
    if len(args) != 3:
        raise ValueError("Format ekspresi tidak valid (jumlah argumen salah)")
    x = args[1]
    y = args[2]
    if op not in "+-*/":
        raise ValueError("Operator tidak valid")
    if isinstance(y, list):
        if len(y) != 3:
            raise ValueError("Format ekspresi tidak valid (jumlah argumen salah)")
        finalY = eval_expr(y[0], y[1], y[2])
    else:
        finalY = y
    if finalY == 0:
        raise ValueError("Pembagian dengan 0")
    
    if isinstance(x, list):
        if len(x) != 3:
            raise ValueError("Format ekspresi tidak valid (jumlah argumen salah)")
        finalX = eval_expr(x[0], x[1], x[2])
    else:
        finalX = x
    
    hasil = finalX + finalY if op == "+" else finalX - finalY if op == "-" else finalX * finalY if op == "*" else finalX/finalY
    return hasil
  
try:  
    print(eval_expr("-", ["+", 10, 5], 4))
except ValueError as e:
    print(e)
