#!/usr/bin/env python3
# -*- coding: utf-8 -*-


' a test module '
__author__ = 'Allen ke'

import math
def quadratic(a,b,c):
	s = math.sqrt(b*b - 4*a*c)
	x1 = (s - b)/(2*a)
	x2 = (-b - s)/(2*a)
	return x1,x2

def helloworld():
	print('helloworld')

import sys
def createModuleFunction():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    createModuleFunction()