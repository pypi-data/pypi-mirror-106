'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-04-21 16:24:36
LastEditors: TianyuYuan
LastEditTime: 2021-04-21 23:18:16
'''
import cv2
import math
import numpy as np
from tykit.aibeekit.facex_client import FacexClient

facex = FacexClient("gpu204", 16143)

class DrawBox:

    @staticmethod
    def r_matrix(radius):
        """返回旋转矩阵"""
        r = np.array([[math.cos(radius),(-1)*math.sin(radius)],[math.sin(radius),math.cos(radius)]])
        return r

    @staticmethod
    def create_box(left:int, top:int, width, height, degree) -> dict:
        """Create box dict
        @param left: the x coordinate of the left-top point of the box
        @param top: the y coordinate of the left-top point of the box
        @param width: the width of the box
        @param height: the height of the box
        @param degree: the degree(not radius) of the box
        @return box: the box dict
        """
        box = {
            'left':left,
            'top':top,
            'width':width,
            'height':height,
            'degree':degree,
        }
        return box

    @staticmethod
    def rotate_box(box:dict):
        """输入box信息，输出实际的box端点坐标"""
        left_point_x = int(box['left'])
        top_point_y = int(box['top'])
        angle = box['degree']
        width = box['width']
        height = box['height']
        radius = angle * math.pi / 180
        center_x = width/2
        center_y = height/2
        vector_cxy = np.array([[center_x, center_y]]).T
        vector_trans = np.array([[left_point_x,top_point_y]]).T
        # * p' = T + R*p
        rotated_cxy = vector_trans+np.dot(DrawBox.r_matrix(radius),vector_cxy)

        rbox = ((rotated_cxy[0][0],rotated_cxy[1][0]), (width, height), angle)
        r_box = cv2.boxPoints(rbox)
        r_box = np.int0(r_box)
        return r_box

    @staticmethod
    def draw_box(img, points):
        # TODO use cv2 to draw line and save image.
        return 0


    @staticmethod
    def dbi(img_address:str, box:dict={}, save:str="", show:bool=True):
        """'dbi' is the abbr of 'Draw Box on the Image'
        @param img_address: the address of the image
        @param box: the box dict. Its default to null dict, and it will request the box info from facex automatically
        @param save: the processed image save path. Its default to null str, and won't save anything.
        @param show: whether imshow the processed image
        """
        img = cv2.imread(img_address)
        if box:
            points = DrawBox.rotate_box(box)
        else:
            box = facex.get_box(img_address, check=False)
            if box:
                points = DrawBox.rotate_box(box)
            else:
                print("ERROR: Can't detect face in this image.")
        # TODO use cv2 to draw line and save image.
        img_and_box = DrawBox.draw_box(img, points)
        if show:
            cv2.imshow("Image and box", img_and_box)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if save:
            cv2.imwrite(save, img_and_box)