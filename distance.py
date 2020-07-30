import numpy as np
import argparse
import sys
import os

def read_file_list(filename):
    """
    Reads a trajectory from a text file.

    File format:
    The file format is "stamp d1 d2 d3 ...", where stamp denotes the time stamp (to be matched)
    and "d1 d2 d3.." is arbitary data (e.g., a 3D position and 3D orientation) associated to this timestamp.

    Input:
    filename -- File name

    Output:
    dict -- dictionary of (stamp,data) tuples

    """
    file = open(filename)
    data = file.read()
    lines = data.replace(",", " ").replace("\t", " ").split("\n")
    list = [[v.strip() for v in line.split(" ") if v.strip() != ""] for line in lines if
            len(line) > 0 and line[0] != "#"]
    list = [(float(l[0]), l[1:]) for l in list if len(l) > 1]
    #print(list)
    return list #dict(list)


def compute_distance(file_list):
    sum = 0
    for a in range(len(file_list)):
        a_t = file_list[a][1]
        b = a+1
        if b<len(file_list):
            b_t = file_list[b][1]
            dis=np.linalg.norm([float(b_t[0])-float(a_t[0]),float(b_t[1])-float(a_t[1]),float(b_t[2])-float(a_t[2])], ord=2)
            #print(dis)
        sum +=dis
    return sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''input with tum rgb-d pose file''')
    parser.add_argument('file', help='temp tx ty tz ..... ')
    args = parser.parse_args()
    list = read_file_list(args.file)
    distance = compute_distance(list)
    print("distance of the trajectory is %f"%distance)



