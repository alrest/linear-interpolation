from math import *
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andres Gonzalez
# Name:         Patrick Shen
# Section:      509
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR

# PART 1

# coordinates
x1 = 10
y1 = 2026
x2 = 55
y2 = 23026

# calculates the slope
m = (y2-y1)/(x2-x1)

# equation that will solve for distance from houston given time

t = 25
dist = m * (t-x1) + y1
print("For t =", t, "minutes, the position p =", dist, "kilometers")

# PART 2

t = 300
r = 6745
c = 2 * pi * r
dist = (m * (t-x1) + y1) % c
print("For t =", t, "minutes, the position p =", dist, "kilometers")