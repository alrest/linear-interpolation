from math import *
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andres Gonzalez
# Name:         Patrick Shen
# Name:         Nick Almeter
# Name:         Jacob Williams
# Section:      509
# Assignment:   LAB: Linear Interpolation
# Date:         09-09-2022


x1 = 10
y1 = 2026
x2 = 55
y2 = 23026

m = (y2-y1)/(x2-x1)

t = 25
dist = m * (t-x1) + y1
print("Part 1:")
print("For t =", t, "minutes, the position p =", dist, "kilometers")

# PART 2
print()

t = 300
r = 6745
c = 2 * pi * r
dist = (m * (t-x1) + y1) % c
print("Part 2:")
print("For t =", t, "minutes, the position p =", dist, "kilometers")