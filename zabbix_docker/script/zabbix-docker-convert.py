#!/usr/bin/python

#################################################################
#
# zabbix-docker-convert-py
#
#   A program that converts between K,M,G,T.
#
# Version: 1.0
#
# Author: Richard Sedlak
#
#################################################################

import sys

def B(b):
    return int(float(b))
	
def KB(b):
    return int(float(b) * 1024)
	
def MB(b):
    return int(float(b) * 1024 * 1024)

def GB(b):
    return int(float(b) * 1024 * 1024 * 1024)
	
def TB(b):
    return int(float(b) * 1024 * 1024 * 1024 * 1024)

options = {
	'k':KB,
	'K':KB,
	'm':MB,
	'M':MB,
	'g':GB,
	'G':GB,
	't':TB,
	'T':TB,
	'b':B,
	'B':B
}	

#
# First read from stdin
#
lines = sys.stdin.readlines(81)

tokens = lines[0].split(" ");

c = tokens[1][0]

print options[c](tokens[0])
