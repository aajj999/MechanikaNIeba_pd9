MIU = [10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 0.1, 0.2, 0.3, 0.4, 0.5]

#parametr x pierwszej masy
def x1(miu):
    return -miu

#parametr x drugiej masy
def x2(miu):
    return 1-miu

#potencjał efektywny w punkcie Lagrange'a o podanym x
def pot_eff(x, miu):
    return x**2 / 2 + (1 - miu) / (x + miu) + miu / (x - 1 + miu)

def K(x, miu):
    return (1 - miu) / (abs(x - x1(miu)))**3 + miu / (abs(x - x2(miu)))**3

#wyrażenie, które przyrównane do 0 daje wartość lambdy
def naLambde(lam, K):
    return (lam**4 + (2 - K) * lam**2 + 1 + K - 2 * K**2)

#funkcja wyliczająca parametr lambda
def lam(K):
    lam = 0
    epsilon = 0.1

    while((abs(naLambde(lam, K)) > epsilon) & (lam <= 6)):
        lam += epsilon / 100

    if(lam >= 6):
        return '-'

    return lam

#równanie przyrównane do 0 daje wartość x
def naX(x, miu):
    return x - (1-miu) / (x + miu)**2 - miu / (x - 1 + miu)**2

#wypisywanie wartości x, potencjału oraz parametrów K i lambda dla danego punktu
#paranetr n jest napisem ze zbioru {'1', '2', '3'}, który jest informacją, który to punkt Lagrange'a
def wypisz_dla_x(miu, x, n):
    pot = pot_eff(x, miu)
    k = K(x, miu)
    lamb = lam(k)

    print('   x' + n + '= ' + str(x) + '   pot= ' + str(pot) + '   K= ' + str(k) + '   lambda= ' + str(lamb))


'''
Dla każdej z zadanych wartości parametru miu wyliczamy współrzędne x.
Wartości współrzędnej x są liczbami zespolonymi dla punktów L1 oraz L3.
Wartość dla L2 jest rzeczywista'''
for miu in MIU:
    print('miu= ' + str(miu))

    #x1

    x = 0.09
    '''stosowane ograniczenia na x pochodzą ze wcześniejszej wiedzy
     i są wprowadzone dla efektywności rozwiązania'''
    epsilon = 0.01

    while ((abs(naX(x, miu)) > epsilon) & (x < 1)):
        i = -1
        while ((abs(naX(complex(x, i), miu)) > epsilon) & (i < 0)):
            i += epsilon / 10
            #print('miu=' + str(miu) + 'x=' + str(x) + 'i=' + str(i) + 'naX=' + str(abs(naX(complex(x, i), miu))))

        if(abs(naX(complex(x, i), miu)) <= epsilon):
            break
        x += epsilon / 10
        #print(x)

    wypisz_dla_x(miu, x, '1')


    #x2

    x = 1
    epsilon = 0.0001

    while ((abs(naX(x, miu)) > epsilon) & (x < 1.3)):
        x += epsilon / 10

    wypisz_dla_x(miu, x, '2')

    #x3

    x = -0.7
    epsilon = 0.01

    while ((abs(naX(x, miu)) > epsilon) & (x <= -0.5)):
        i = -1
        while ((abs(naX(complex(x, i), miu)) > epsilon) & (i < 0)):
            i += epsilon / 10
            # print('miu=' + str(miu) + 'x=' + str(x) + 'i=' + str(i) + 'naX=' + str(abs(naX(complex(x, i), miu))))

        if (abs(naX(complex(x, i), miu)) <= epsilon):
            break
        x += epsilon / 10

    wypisz_dla_x(miu, x, '3')




