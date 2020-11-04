

def clearing_input(string):
    x = string.split(" ")

    a = 0
    clear_x = list()
    for i in x:
        try:
            clear_x.append(float(i))
            a += 1
        except:
            pass
        if a == 4:
            break
    return clear_x
	