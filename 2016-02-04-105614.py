def Spacer(a,b,n):
    return [float(a)+float(x*float(b-a)/n) for x in range(n+1)]

def test_endPoints():
    a = 0
    b = 17
    n = 4
    testList = Spacer(a,b,n)
    assert( testlist[0] == a and testlist[n+1] == b )
    return