# Напишите программу для 
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

print('W X Y Z')
for W in range(2):
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                if not (Z and W) or not Y or (X == W):
                    print(W, X, Y, Z)
