from random import randint
k = randint(1,1000)
S = 0
while True:
    S += 1
    inp = int(input("czy to: "))
    if inp == k:
        break
    elif inp < k:
        print("za mala liczba")
    elif inp > k:
        print("za duza liczba") 
    else:
        print("zla liczba")
print(f"Brawo zgadles szukna liczba to {k}")