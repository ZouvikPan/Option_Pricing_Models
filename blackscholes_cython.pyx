#!python
#cython: language_level=3
cdef extern from "math.h" nogil:
    double exp(double)
    double sqrt(double)
    double pow(double, double)
    double log(double)
    double erf(double)

cdef double std_norm_cdf(double x):
    return 0.5*(1+erf(x/sqrt(2.0)))

def black_scholes(double s, double k, double t, double v, double rf, double div, double cp):
    """ Pricing options using the Black-Scholes model

    s : initial stock price
    k : strike price
    t : time till expiration
    v : volatility
    rf : risk-free rate
    div : dividend
    cp : Flag +1/-1 for call/put respectively

    """
    cdef double d1, d2, optprice
    d1 = (log(s/k)+(rf-div+0.5*pow(v,2))*t)/(v*sqrt(t))
    d2 = d1 - v*sqrt(t)
    optprice = cp*s*exp(-1*div*t)*std_norm_cdf(cp*d1) - cp*k*exp(-rf*t)*std_norm_cdf(cp*d2)

    return optprice