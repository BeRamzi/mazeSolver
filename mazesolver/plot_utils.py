import cv2
import matplotlib.pyplot as plt
import numpy as np
def show_img_cv2(img:np.ndarray, wait:int=0)->None:
    '''
    wait = 0 means it waits  forrever
    wait = 1 wait 1 milisecond

    '''
    cv2.imshow("image", img)
    cv2.waitKey(wait)
    cv2.destroyAllWindows()