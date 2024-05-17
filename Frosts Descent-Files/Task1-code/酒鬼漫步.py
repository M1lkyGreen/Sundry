import numpy as np
steps = 2000
draws = np.random.randint(0,2,size = steps)
direction_steps = np.where(draws > 0,1,-1)
distance = direction_steps.cumsum()
print(distance.max())
print(distance.min())
steps = 15 / 0.5
print((np.abs(distance >= steps).argmax()))
