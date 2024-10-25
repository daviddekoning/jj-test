+def r(w: float, l: float):
     return w * l / 2

def M(w: float, l: float):
    return w * l * l / 8

def M_point(p: float, l: float):
    return P * L / 4

if __name__ == "__main__":
    print(f"Span: {6}, Load: {16}, Moment: {M(6,16)}")