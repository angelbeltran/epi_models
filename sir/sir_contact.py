from numpy import linspace, zeros
import matplotlib.pyplot as plt
import math
import time
import datetime
import sys

def get_parameters():
    f = open('sir_contact_parameters.csv', 'r')
    mapping = dict()
    for line in f:
        data = line.split(',')
        for i in range(len(data)):
            data[i] = data[i].strip(' ')
            data[i] = data[i].strip('\n')
        for i in range(1, len(data)):
            if '.' not in data[i]:
                data[i] = int(data[i])
            else:
                data[i] = float(data[i])
        mapping[data[0]] = data[1:]
    f.close()
    return mapping

def sir(D, H, n, _a, K, r, nb_mb, e):
    # Computational constants
    dt = 1./(24)        # intervals of 1 hour
    # D = 365             # Simulation lasts 365 days
    N_t = int(D/dt)     # no of intervals in simulation
    t = linspace(0, N_t*dt, N_t + 1)
    S = zeros(N_t + 1)
    I = zeros(N_t + 1)
    B = zeros(N_t + 1)

    # Initial Condition
    S[0] = H - 1
    I[0] = 1
    B[0] = 0

    def a(t):
        return _a + _a*math.sin(2*math.pi*t*dt/365)

    # Approximations
    for i in range(N_t):
        S[i+1] = S[i] + dt*(n*(H - S[i]) - a(i)*S[i]*B[i]/(K + B[i]) + 0.0*r*I[i])
        I[i+1] = I[i] + dt*(a(i)*B[i]*S[i]/(K + B[i]) - r*I[i])
        B[i+1] = B[i] + dt*(B[i]*(nb_mb) + e*I[i])

    return S, I, B, t


def display_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e):
    fig = plt.figure()
    l1, l2, l3 = plt.plot(t, S, t, I, t, B)
    fig.legend((l1, l2, l3), ('S', 'I', 'B'), 'upper left')

    ax = fig.add_subplot(111)
    ax.set_title('SIR Contact Model')
    text = 'D = {0}\nH = {1}\nn = {2}\na = {3}\nK = {4}\nr = {5}\nnb_mb = {6}\ne = {7}\n'.format(D, H, n, a, K, r, nb_mb, e)
    ax.text(317, 8000, text, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    plt.xlabel('days')
    plt.show()

def save_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e):
    fig = plt.figure()
    l1, l2, l3 = plt.plot(t, S, t, I, t, B)
    fig.legend((l1, l2, l3), ('S', 'I', 'B'), 'upper left')
    # text_fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('SIR Contact Model')
    text = 'D = {0}\nH = {1}\nn = {2}\na = {3}\nK = {4}\nr = {5}\nnb_mb = {6}\ne = {7}\n'.format(D, H, n, a, K, r, nb_mb, e)
    ax.text(317, 8000, text, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    # text_fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
    plt.xlabel('days')


    # display_string = 'Name your pdf:\nH = {0}\nn = {1}\na = {2}\nK = {3}\nr = {4}\nnb_mb = {5}\ne = {6}.\ntitle: '.format(H, n, a, K, r, nb_mb, e)
    display_string = 'Name your pdf:\nD = {0}\nH = {1}\nn = {2}\na = {3}\nK = {4}\nr = {5}\nnb_mb = {6}\ne = {7}\n'.format(D, H, n, a, K, r, nb_mb, e)
    title = raw_input(display_string)
    print ''
    title = title.split(' ')[0].split('.')[0]
    if title == '':
        ts = time.time()
        title = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    plt.savefig(title + '.pdf'); # plt.savefig('tmp.png')

def main():
    # get data from parameter csv
    data = get_parameters()

    # get longest row's length
    m = len(data['a'])
    for k in data:
        m = min(m, len(data[k]))

    for i in range(m):
        D = data['D'][i]
        H = data['H'][i]
        n = data['n'][i]
        a = data['a'][i]
        K = data['K'][i]
        r = data['r'][i]
        nb_mb = data['nb_mb'][i]
        e = data['e'][i]

        S, I, B, t = sir(D, H, n, a, K, r, nb_mb, e)
        if len(sys.argv) == 1:
            display_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e)
        elif sys.argv[1] == 'show':
            display_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e)
        elif sys.argv[1] == 'save':
            save_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e)
        else:
            display_sir(S, I, B, t, D, H, n, a, K, r, nb_mb, e)

if __name__ == "__main__":
    main()
