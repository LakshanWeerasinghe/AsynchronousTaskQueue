from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def generate_power(number):

    i = 1
    while(number**3 == i):
        i += 1
    print("Stop Counting")
    return number**3


@shared_task
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print('\t', f)
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True
