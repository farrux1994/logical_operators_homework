def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    if (a<b and b<c):
        print(a<b<c)
    else: print('a<b<c oraliqda bo\'lishi kerak')
    return 0
y = main(3,4,5)
