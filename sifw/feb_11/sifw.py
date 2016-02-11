from numpy import linspace, zeros
import matplotlib.pyplot as plt
import math
import time
import datetime
import sys

def get_parameters():
    f = open('sifw_parameters.csv', 'rho')
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

def sifw(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D, _W=1):
    # Computational constants
    dt = 1./(24)        # intervals of 1 hour (float)
    # days = 365             # Simulation lasts 365 days
    N_t = int(days/dt)     # no of intervals in simulation
    t = linspace(0, days, N_t + 1)
    S = zeros(N_t + 1)
    I = zeros(N_t + 1)
    F = zeros(N_t + 1)
    W = zeros(N_t + 1)

    # Initial Condition# NOTE: RETURN HERE TO SET THE INITIAL CONDITIONS
    S[0] = H - 1
    I[0] = 1
    F[0] = 0
    W[0] = _W

    # def D(t):
    #     return _D + _D*math.sin(2*math.pi*t/365)/2

    # print H
    # print S[0], I[0], F[0], W[0]
    # Approximations
    for i in range(N_t):
        S[i+1] = S[i] + dt*((b - d)*(H - S[i] - I[i]) + rho*I[i] - beta*S[i]*F[i]/(k*W[i] + F[i]))
        I[i+1] = I[i] + dt*(beta*S[i]*F[i]/(k*W[i] + F[i]) - (d + rho + alpha)*I[i])
        F[i+1] = F[i] + dt*((r - mu)*F[i] + _lambda*I[i])
        W[i+1] = W[i] + dt*(p + s - D*W[i])

        # if (i % 100 == 0):
        #     print S[i+1], I[i+1], F[i+1], W[i+1]

    return S, I, F, W, t

def display_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D):
    fig = plt.figure()
    l1, l2, l3, l4 = plt.plot(t, S, t, I, t, F, t, W)
    fig.legend((l1, l2, l3, l4), ('S', 'I', 'F', 'W'), 'upper left')

    ax = fig.add_subplot(111)
    ax.set_title('SIFW Model')
    text = 'days = {0}\nH = {1}\nb = {2}\nd = {3}\nbeta = {4}\nrho = {5}\nk = {6}\nalpha = {7}\nr = {8}\nmu = {9}\nlambda = {10}\np = {11}\ns = {12}\nD = {13}\n'.format(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
    ax.text(317, 8000, text, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

    plt.xlabel('days')
    plt.show()

def save_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D):
    fig = plt.figure()
    l1, l2, l3, l4 = plt.plot(t, S, t, I, t, F, t, W)
    fig.legend((l1, l2, l3, l4), ('S', 'I', 'F', 'W'), 'upper left')

    ax = fig.add_subplot(111)
    ax.set_title('SIFW Model')
    text = 'days = {0}\nH = {1}\nb = {2}\nd = {3}\nbeta = {4}\nrho = {5}\nk = {6}\nalpha = {7}\nr = {8}\nmu = {9}\nlambda = {10}\np = {11}\ns = {12}\nD = {13}\n'.format(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
    ax.text(317, 8000, text, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    # text_fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
    plt.xlabel('days')

    print '\ndays = {0}\nH = {1}\nb = {2}\nd = {3}\nbeta = {4}\nrho = {5}\nk = {6}\nalpha = {7}\nr = {8}\nmu = {9}\nlambda = {10}\np = {11}\ns = {12}\nD = {13}'.format(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
    print ''
    title = raw_input('Name your pdf: ')
    title = title.split(' ')[0].split('.')[0]
    if title == '':
        ts = time.time()
        title = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    plt.savefig(title + '.pdf'); # plt.savefig('tmp.png')

def main():
    # get data from parameter csv
    data = get_parameters()

    # get shortest row's length
    m = len(data['H'])
    for k in data:
        m = min(m, len(data[k]))

    for i in range(m):
        days = data['days'][i]
        H = data['H'][i]
        b = data['b'][i]
        d = data['d'][i]
        beta = data['beta'][i]
        rho = data['rho'][i]
        k = data['k'][i]
        alpha = data['alpha'][i]
        r = data['r'][i]
        mu = data['mu'][i]
        _lambda = data['_lambda'][i]
        p = data['p'][i]
        s = data['s'][i]
        D = data['D'][i]

        S, I, F, W, t = sifw(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
        if len(sys.argv) == 1:
            display_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
        elif sys.argv[1] == 'show':
            display_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
        elif sys.argv[1] == 'save':
            save_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)
        else:
            display_sir(S, I, F, W, t, days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D)

if __name__ == "__main__":
    main()
