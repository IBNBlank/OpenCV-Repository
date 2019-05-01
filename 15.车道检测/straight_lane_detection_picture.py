# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2019-05-01 10:54:43
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-05-01 13:32:02

import cv2 as cv
import numpy as np


### mask ###
def get_masked(img, pt_1, pt_2):
    rows, cols = img.shape
    corner_list = np.array([[(0,rows), pt_1, pt_2, (cols,rows)]])

    # mask the image
    mask = np.zeros_like(img)
    cv.fillPoly(mask, corner_list, 255)
    img_masked = cv.bitwise_and(img, mask)

    # return
    return img_masked


### lane ###
# clean lines
def clean_lines(lines, threshold):
    # detect lines
    if len(lines) == 0:
        return

    # get slopes
    slopes = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            slopes.append((y2-y1)/(x2-x1))

    # clean the lines
    mean = np.mean(slopes)
    diffs = [abs(slope-mean) for slope in slopes]
    max_index = np.argmax(diffs)
    while diffs[max_index] > threshold:
        slopes.pop(max_index)
        lines.pop(max_index)
        mean = np.mean(slopes)
        diffs = [abs(slope-mean) for slope in slopes]
        max_index = np.argmax(diffs)

# least squares
def least_squares(pts, ymin, ymax):
    # get x y
    x = []
    y = []
    for pt in pts:
        x.append(pt[0])
        y.append(pt[1])

    # fit
    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)

    xmin = int(fit_fn(ymin))
    xmax = int(fit_fn(ymax))

    return [(xmin, ymin), (xmax, ymax)]

# get lanes
def get_lanes(img, rho, theta, threshold, min_line_len, max_line_gap):
    # hough
    lines = cv.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)

    # detect direction
    left_lines, right_lines = [], []
    for line in lines:
        for x1, y1, x2, y2 in line:
            k = (y2 - y1) / (x2 - x1)
            if k < 0:
                left_lines.append(line)
            else:
                right_lines.append(line)

    # detect lanes
    if (len(left_lines) <= 0 or len(right_lines) <= 0):
        return np.zeros_like(img)

    # clean the wrong lines
    clean_lines(left_lines, 0.1)
    clean_lines(right_lines, 0.1)

    # get the point of left lanes
    left_points = []
    for line in left_lines:
        for x1, y1, x2 ,y2 in line:
            left_points.append((x1,y1))
            left_points.append((x2,y2))
    left_results = least_squares(left_points, 325, img.shape[0])

    # get the point of right lanes
    right_points = []
    for line in right_lines:
        for x1, y1, x2 ,y2 in line:
            right_points.append((x1,y1))
            right_points.append((x2,y2))
    right_results = least_squares(right_points, 325, img.shape[0])

    # draw the lane
    img_lane = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    cv.fillPoly(img_lane, np.array([[left_results[0], left_results[1], right_results[1], right_results[0]]]), (0, 0, 255))

    return img_lane


### process ###
def process(image):
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # gaussian #
    kernal = (5,5)
    img_gaussian = cv.GaussianBlur(img, kernal, 0)

    # canny #
    minVal = 50
    maxVal = 150
    img_canny = cv.Canny(img_gaussian, minVal, maxVal)

    # mask #
    point_1 = (460, 325)
    point_2 = (520, 325)
    img_masked = get_masked(img_canny, point_1, point_2)

    # lanes #
    rho = 1
    theta = np.pi / 180
    threshold = 15
    min_line_len = 40
    max_line_gap = 20
    img_lane = get_lanes(img_masked, rho, theta, threshold, min_line_len, max_line_gap)

    # combine
    img_result = cv.addWeighted(image, 1, img_lane, 0.2, 0)

    # return #
    return img_result


### main ###
if __name__ == '__main__':
    # get image #
    file_path = "image\\lane2.jpg"
    image = cv.imread(file_path, cv.IMREAD_UNCHANGED)

    # process #
    img_result = process(image)

    # show image #
    cv.imshow("origin", image)
    cv.imshow("lane detection", img_result)
    cv.waitKey(0)
    cv.destroyAllWindows()