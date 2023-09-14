a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
delta = float(pow(pow(b,2)-4*a*c,1/2))
print(delta)
v1 = (-b + delta)/2*a
v2 = (-b - delta)/2*a
print(f"v1 = {v1:.2f} e v2 = {v2:.2f}")
