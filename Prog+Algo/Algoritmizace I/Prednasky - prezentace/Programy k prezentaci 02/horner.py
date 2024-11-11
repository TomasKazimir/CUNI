def horner(a,x):
    """
    výpočet hodnoty polynomu Hornerovým schématem
    a: seznam s koeficienty polynomu od nejvyššího řádu
    x: bod z definičního oboru
    vrátí: hodnotu polynomu v bodě x
    """
    h = 0
    for i in range(len(a)):
        h = h * x + a[i]
    return h
