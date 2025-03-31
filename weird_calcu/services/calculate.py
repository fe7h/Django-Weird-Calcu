
def calculate(a: int | float, b: int | float) -> str:
    res = a + b
    return str(int(res)) if res.is_integer() else str(res)
