def fixing_float(size, n_float):
    fmt = ".{n}f"
    fix = [None]
    
    for i in range(size):
        fix.append(fmt.format(n=n_float))

    return fix
