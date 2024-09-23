# Calculate Average Temperature

import array

numDays = int(input("How many day's temperature? "))
sum = 0
temperatures = []
for i in range(numDays):
    temperature = int(input(f"Day {i+1}'s high temperature : "))
    temperatures.append(temperature)
    sum += temperatures[i]
average = round(sum/numDays, 2)
print(f"\nAverage = {average}")

above = 0
for i in temperatures:
    if i > average:
        above += 1
print(f"{above} day(s) above average")
