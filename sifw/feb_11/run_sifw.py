import time
import datetime
import os
from sifw import sifw
from sifw_parameters import days, H, b, d, _beta, _rho, _k, _alpha, _r, _mu, __lambda, _p, _s, _D, _W

ts = time.time()
subdirectory = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
os.mkdir(subdirectory)

f = open(os.path.join(subdirectory, 'parameters.py'), 'w')
f.write('days = ' + str(days) + '\n')
f.write('H = ' + str(H) + '\n')
f.write('b = ' + str(b) + '\n')
f.write('d = ' + str(d) + '\n')
f.write('_beta = ' + str(_beta) + '\n')
f.write('_rho = ' + str(_rho) + '\n')
f.write('_k = ' + str(_k) + '\n')
f.write('_alpha = ' + str(_alpha) + '\n')
f.write('_r = ' + str(_r) + '\n')
f.write('_mu = ' + str(_mu) + '\n')
f.write('__lambda = ' + str(__lambda) + '\n')
f.write('_p = ' + str(_p) + '\n')
f.write('_s = ' + str(_s) + '\n')
f.write('_D = ' + str(_D) + '\n')
f.write('_W = ' + str(_W))
f.close()

for i1 in range(2):
    beta = _beta[i1]
    for i2 in range(2):
        rho = _rho[i2]
        for i3 in range(2):
            k = _k[i3]
            for i4 in range(2):
                alpha = _alpha[i4]
                for i5 in range(2):
                    r = _r[i5]
                    for i6 in range(2):
                        mu = _mu[i6]
                        for i7 in range(2):
                            _lambda = __lambda[i7]
                            for i8 in range(2):
                                p = _p[i8]
                                for i9 in range(2):
                                    s = _s[i9]
                                    for i10 in range(2):
                                        D = _D[i10]
                                        for i11 in range(2):
                                            W = _W[i11]

                                            S, I, F, W, t = sifw(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D, W)

                                            file_name = 'sifw_simulation_' + str(i1) + '_' + str(i2) + '_' + str(i3) + '_' + str(i4) + '_' + str(i5) + '_' + str(i6) + '_' + str(i7) + '_' + str(i8) + '_' + str(i9) + '_' + str(i10) + '_' + str(i11) + '.csv'
                                            #f = open(file_name, 'w')
                                            f = open(os.path.join(subdirectory, file_name), 'w')
                                            for data in S:
                                                f.write(str(data) + ',')
                                            f.write('\n')
                                            for data in I:
                                                f.write(str(data) + ',')
                                            f.write('\n')
                                            for data in F:
                                                f.write(str(data) + ',')
                                            f.write('\n')
                                            for data in t:
                                                f.write(str(data) + ',')
                                            f.write('\n')
                                            f.close()

# sifw(days, H, b, d, beta, rho, k, alpha, r, mu, _lambda, p, s, D, W)

# days = 730
# H = [10000]
# b = [.02, .05, .1]
# d = [.01, .02, .05]
# beta = [.01, .05, .1, .2, .5, .9]
# rho = [.01, .05, .1, .2, .5, .9]
# k = [.01, .05, .1, .2, .5, .9]
# alpha = [.01, .05, .1, .2, .5, .9]
# r = [.01, .1, 1, 10, 100, 1000, 10000]
# mu = [.01, .1, 1, 10, 100, 1000, 10000]
# _lambda = [.01, .1, 1, 10, 100, 1000, 10000]
# p = [.01, .1, 1, 10, 100, 1000, 10000]
# s = [.01, .1, 1, 10, 100, 1000, 10000]
# _D = [.01, .1, 1, 10, 100, 1000, 10000]

#days = 730
#H = 10000
#b = .06
#d = .02
#_beta = [.05, .5]
#_rho = [.05, .5]
#_k = [.05, .5]
#_alpha = [.01, .1]
#_r = [1, 1000]
#_mu = [.5, 500]
#__lambda = [1, 10]
#_p = [.01, 1]
#_s = [.01, 1]
#_D = [.01, 1]
#_W = [1, 1000]

#print days
#print H
#print b
#print d
#print _beta
#print _rho
#print _k
#print _alpha
#print _r
#print _mu
#print __lambda
#print _p
#print _s
#print _D
#print _W

#days
#H
#b
#d
#_beta
#_rho
#_k
#_alpha
#_r
#_mu
#__lambda
#_p
#_s
#_D
#_W

