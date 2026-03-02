# Name: Saranya Mohanamoorthi
# Roll Number: iitp_aimltn_2602093 
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
high_temp = temperatures[0]
low_temp = temperatures[0]
for t in temperatures:
    if t > high_temp:
        high_temp = t
    if t < low_temp:
        low_temp = t
print('Highest Temperature:', high_temp)
print('Lowest Temperature:', low_temp)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
count = 0
for t in temperatures:
    if t <= 30:
        continue
    count = count+1
print('Hot Days (>30°C):', count)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
count = 0
for t, temp in enumerate(temperatures):
    if temp>30:
        if temp>=40:
            break
        count = count+1
    
print('Hot Days before alert:', count)
print(f'Alert! Extreme temperature {temp}°C detected on Day {t+1}')
