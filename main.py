import random
import time

def getRandPI(iters=10**8):
    points_in_circle = 0
    points_in_square = 0

    for i in range(iters):
        x = random.random()
        y = random.random()
        distance = x**2 + y**2

        if distance <= 1:
            points_in_circle += 1
        points_in_square += 1
    
        if i % 10**6 == 0: 
            progress = "{:.3f}%".format(i/iters*100,6)
            PIValue = " (PI ≈ {:.10f})".format(4*points_in_circle/points_in_square)
            print((progress + PIValue).rjust(27,"0"))

        PI = 4 * points_in_circle / points_in_square

    return PI

    # random.random()        3.141651276 in 468.40744709968567 seconds
    # random.uniform(0,1)    3.1415521461538463 in 458.7304801940918 seconds
    # You can use random.uniform(0,1), but theoretically they do the same exept that random.random() doesn't include 1.0

t = time.time()
print( f"\nPI ≈ {getRandPI()}" )
print(f"Finished in {time.time()-t} seconds\n")