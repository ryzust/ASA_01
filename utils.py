import numpy as np
import matplotlib.pyplot as plt

# Generate a random set of points in the plane from [0,1]


# Generate a frame 
def generate_frame():
    frame_points = np.random.random(4)
    frame_points = np.sort(frame_points)
    top_frame = [frame_points[0],frame_points[3]]
    bottom_frame = [frame_points[1],frame_points[2]]

    
    