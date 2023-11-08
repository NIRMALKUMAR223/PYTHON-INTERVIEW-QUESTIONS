R, C = map(int, input("Enter R and C: ").split())

for i in range(R):
    for j in range(C):
        if i == 0 or i == R - 1 or j == 0 or j == C - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
