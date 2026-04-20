# Author: Antonio Loureiro Dunch
# GitHub username: aloureirodunch
# Date: April 16th, 2026
# Description: Calculator of various details about a trip.

############# Part A

DistanceMiles = float(input("Enter the trip distance in miles: "))
DriveSpeed = float(input("Enter the average driving speed on the trip in miles per hour: "))
FuelEfficiency = float(input("Enter the average fuel efficiency on the trip in miles per gallon: "))
GasPrice = float(input("Enter the average gas price on the trip per gallon: "))

############# Part B

DriveTime = DistanceMiles / DriveSpeed
DriveTime = round(DriveTime, 1)

GallonsNeeded = DistanceMiles / FuelEfficiency
GallonsNeeded = round(GallonsNeeded, 1)

FuelCost = GallonsNeeded * GasPrice
FuelCost = round(FuelCost, 1)


############# Part C

print(f"For a trip of {DistanceMiles} miles, at an average speed of {DriveSpeed} mph, the driving time will be {DriveTime} hours.")

print(f"Your car will use {GallonsNeeded} gallons of gas, and the total fuel cost will be ${FuelCost}.")