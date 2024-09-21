import cv2
import matplotlib.pyplot as plt
from datamodels import Maze
import numpy as np
from plot_utils import show_img_cv2

arr = [[1,1,1,0,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,1],
       [1,0,1,1,1,1,0,1,0,1],
       [1,0,0,0,1,0,0,1,0,1],
       [1,0,1,0,1,0,1,1,0,1],
       [1,0,0,0,0,0,1,0,0,1],
       [1,1,1,1,1,0,1,1,1,1],
       [1,0,1,0,1,0,1,1,0,1],
       [1,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,0,1]
]
maze = Maze(array=np.array(arr,dtype=np.uint8)*255)

























def main():
    show_img_cv2(maze.array)


if __name__ == "__main__":
    main()