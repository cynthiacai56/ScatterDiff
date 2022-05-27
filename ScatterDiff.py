import math
import numpy as np
import matplotlib.pyplot as plt
import json

def scatter_diff(name, filepath1, filepath2):
    """
    Print the mean and variance of the Euclidean distance between two datasets.
    :param name: name of the image
    :param filepath1: filepath of the first dataset (original)
    :param filepath2: filepath of the second dataset (projected)
    :return:
    """
    # read files
    pts1,pts2 = read_file(filepath1), read_file(filepath2)
    if len(pts1) != len(pts2):
        print("Error: len(Points1) != len(Points2)")

    # compute mean and variance of Eucliean distances
    mean, var = stat_eucliean_distance(pts1, pts2)

    # print results
    print("{}       : mean  {}, variance  {}".format(name, mean, var))

    # scatter plot
    scatter_plot(name, pts1, pts2)

    return 0

def read_file(filepath):
    """
    Read xyz or txt file and load the 2D coordinates. Not homogenous.
    :param filepath:
    :return: list of 2D coordinates [x,y].
    """
    point_list = []
    with open(filepath) as f:
        for line in f:
            list = line.split()
            list = [float(list[0]), float(list[1])] # [x,y], take out the '1'
            point_list.append(list)

    return point_list

def stat_eucliean_distance(pts0, pts1):
    """
    Calcultate the mean and variance of the distances for two dataset.
    :param pts0: list of 2D coordinates of original points
    :param pts1: list of 2D coordinates of projected points
    :return: mean, variance of all points
    """
    if len(pts0) == len(pts1):
        # calculate the distance of each pair
        dist = []
        for i in range(0,len(pts0)):
            dist.append(math.dist(pts0[i],pts1[i]))

        # calculate average and variance value
        mean = np.mean(dist)
        variance = np.var(dist)

        return mean, variance
    else:
        return -10, -10

def scatter_plot(name, pts1, pts2):
    """
    Show the comparision between pts1 and pts2.
    :param name: name of the image
    :param pts1: list of 2D coordinates of original points
    :param pts2: list of 2D coordinates of projected points
    :return: none
    """
    # 1. read data
    x1, y1, x2, y2 = [], [], [], []
    for i in range(0,len(pts1)):
        x1.append(pts1[i][0])
        y1.append(pts1[i][1])
        x2.append(pts2[i][0])
        y2.append(pts2[i][1])

    # 2. set figure
    fig = plt.figure(1) # create a figure

    # 3. set set color, area, width
    area = 10 # size of points
    '''
    colors = np.random.rand(len(pts1) # Randomly generate 10 color values ​​between 0 and 1, or
    colors = ['r', 'g', 'y', 'b', 'r', 'c', 'g', 'b', 'k', 'm']  # color schema
    widths = np.arange(n)  # the width of the boundary, optional parameter
    '''

    # 4. scatter
    plt.scatter(x1, y1, s=area)
    plt.scatter(x2, y2, s=area)
    #plt.scatter(x1, y1, s=area, c=colors, linewidths=widths, alpha=0.5, marker='o')
    #plt.scatter(x2, y2, s=area, c=colors, linewidths=widths, alpha=0.5, marker='o')

    # 5. Set label of the axis, title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(name)

    # 6.show
    plt.show()

def main():
    """
    Read json file and perform scatter comparison.
    :return: none
    """
    #-- explain
    print("======================Explanation======================")
    print("Name         : ScatterDiff")
    print("Developer    : Cynthia Cai")
    print("Organization : geo1016, TU Delft")
    print("Function     : This tool is used to compare two scatters, using Eucliean distance and scatter plots.")
    print("Usage        : Include the image name and relevant file paths in params.json.")
    print("               The input files are expected in txt format.\n")


    #-- read the needed parameters from the file 'params.json'
    jparams = json.load(open("params.json"))

    #-- perform scatter
    print("========================Result========================")
    for i in jparams.keys():
        scatter_diff(jparams[i]["name"], jparams[i]["pts1"], jparams[i]["pts2"])

if __name__ == '__main__':
    main()
