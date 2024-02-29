A = [2, 5, 9, 12, 15, 18, 20] 
N = len(A)  
k = 0  
sum = 0  
while k <= 0:
    k = int(input("Введіть натуральне число k: "))
    if k <= 0:
        print("Число k має бути натуральним.")
for num in A:
    if num <= 0:
        print("Елементи масиву повинні бути натуральними.")
        exit()  
for num in A:
    if num % k == 0:
        sum += num
print(f"Сума елементів, кратних {k}: {sum}")
