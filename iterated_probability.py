#!/usr/bin/python
from decimal import Decimal
from math import log
from math import factorial as fac
from math import log1p
from math import exp

#prob is a really small probability
#This is about the probability that an attacker with 1600 (a crazy number of) masternodes captures a LLMNQ.

prob=2 ** -100

#A large number of trials  (10^20 years of masternode quorums in this case)

M=365*2*(10 ** 20)

print prob

print M

# We want to calculate (1-p)^M but if we use python I expect we'll get an error

fail = (1-prob) ** M

print fail, "<-- Total fail"

#This prints as 1.0 which doesn't really give us ANY information at all.
#If the actual answer was something like .999 I expect this method would not find that value because of rounding errors.

#Instead we use log1p(x) which will compute ln(1+x) and this function is intended to be very accurate when x is near zero.

#(note)  ln is the natural logarithim or the log base e

#A property of logarithims is that log(x^n) = n*log(x)
# So we compute

lnofanswer = M * log1p(-prob)

#notice the negative
#to write it out log1p(-prob) = ln(1-prob)

print lnofanswer

#That gives us an answer we can work with but remember this is the natural logarithim of the answer

#We calculate

ans = exp(lnofanswer)

#and conclude that

print "(1-p)^M =", ans


#That works out to be a measurable probability.
#The probability that the hacker is sucessful at least once in 10^20 (a crazy number of) years is

print 1-ans

#when the scrypt is run this evaluates to 5.75868444042e-08
#this actualy gives us some information and avoids that rounding error.

