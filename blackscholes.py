from scipy import stats
from math import log, pow, sqrt, exp

def black_scholes(s, k, t, v, rf, div, cp):
    """ Pricing options using the Black-Scholes model

    s : initial stock price
    k : strike price
    t : time till expiration
    v : volatility
    rf : risk-free rate
    div : dividend
    cp : Flag +1/-1 for call/put respectively
    
    """
    d1 = (log(s/k)+(rf-div+0.5*pow(v,2))*t)/(v*sqrt(t))
    d2 = d1 - v*sqrt(t)

    optprice = cp*s*exp(-1*div*t)*stats.norm.cdf(cp*d1) - cp*k*exp(-1*rf*t)*stats.norm.cdf(cp*d2)

    return optprice