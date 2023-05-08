#!/usr/bin/env python3

import os

class QuickFind:
    def __init__(self, data_path=None, init_flag=False, N=None):
        """Initialize QuickFind class.
        Args:
            data (list): user-defined data
            init_flag (bool): flag to create default set [0, 1, 2, ..]
            N (int): the length of the default set
        """
        if init_flag:
            # Set id of each object to itself.
            self.dis_set = [i for i in range(N)] 
        else:
            self.dis_set = []
            self.load_data(data_path)

    def get_data(self):
        return self.dis_set

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.dis_set = [i for i in range(int(data[0]))]
            for line_id in range(len(data))[1:]:
                num1, num2 = data[line_id].split()
                self.union(int(num1), int(num2))

    def is_connected(self: list, p_ind: int, q_ind: int) -> bool:
        """Check whether p_ind and q_ind are in the samle component."""
        return self.dis_set[p_ind] ==  self.dis_set[q_ind]

    def union(self: list, p: int, q: int):
        """Change all entries with p_ind to q_ind."""
        if self.is_connected(p, q):
            print("The elements are already connected")
        else:
            p_ind = self.dis_set[p]
            q_ind = self.dis_set[q]

            for i, elem in enumerate(self.dis_set):
                if elem == p_ind:
                    self.dis_set[i] = q_ind


class QuickUnion:
    def __init__(self, data_path=None, init_flag=False, N=None, improvement=False):
        """Initialize QuickUnion class.
        Args:
            data (list): user-defined data
            init_flag (bool): flag to create default set [0, 1, 2, ..]
            N (int): the length of the default set
            improvement (False, "weighting", "compressing", "all")
        """
        self.improvement = improvement

        if init_flag:
            # Set id of each object to itself.
            self.dis_set = [i for i in range(N)]
            if self.improvement == "weighting" or self.improvement == "all":
                self.trees_size = [1] * N
        else:
            self.dis_set = []
            self.load_data(data_path)

    def get_data(self):
        return self.dis_set

    def load_data(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
            # Set id of each object to itself.
            self.dis_set = [i for i in range(int(data[0]))]
            if self.improvement == "weighting" or self.improvement == "all":
                self.trees_size = [1] * int(data[0])
            for line_id in range(1, len(data)):
                num1, num2 = data[line_id].split()
                self.union(int(num1), int(num2))

    def root(self: list, i: int):
        """Chase parent pointers until reach root."""
        while i != self.dis_set[i]:
            if self.improvement == "compressing" or self.improvement == "all": 
                self.dis_set[i] = self.dis_set[self.dis_set[i]]
            i = self.dis_set[i]
        return i

    def is_connected(self: list, p: int, q: int) -> bool:
        """Check whether p and q have the same root."""
        return self.root(p) ==  self.root(q)

    def __weighted_union(self: list, p_root: int, q_root: int):
        "Apply weighting."
        if self.trees_size[p_root] < self.trees_size[q_root]:
            self.dis_set[p_root] = q_root
            self.trees_size[q_root] += self.trees_size[p_root]
        else:
            self.dis_set[q_root] = p_root
            self.trees_size[p_root] += self.trees_size[q_root]

    def union(self: list, p: int, q: int):
        """Change root of p to root of q."""
        if self.is_connected(p, q):
            print("The elements are already connected")
        else:
            p_root = self.root(p)
            q_root = self.root(q)
            
            if self.improvement == "weighting" or self.improvement == "all":
                self.__weighted_union(p_root, q_root)
            else:
                self.dis_set[p_root] = q_root
        print("set:", self.dis_set)
        if self.improvement == "weighting" or self.improvement == "all":
            print("size:", self.trees_size)

                
if __name__ == '__main__':
    pth = os.getcwd() + '/../data/data.txt'
    data_QF = QuickFind(data_path=pth)
    print("Quick Find:", data_QF.get_data())
    data_QU = QuickUnion(data_path=pth)
    print("Quick Union:", data_QU.get_data())
    data_WQU = QuickUnion(data_path=pth, improvement="weighting")
    print("Weighted Quick Union:", data_WQU.get_data())
    print("Weighted Quick Union Sizes:", data_WQU.trees_size)
    data_PCQU = QuickUnion(data_path=pth, improvement="compressing")
    print("Path compressed Quick Union:", data_PCQU.get_data())

    print("TEST")
    print("-" * 10)
    data_QU.union(0, 9)
    print(data_QU.dis_set)
    data_QU.union(5, 2)
    print("-" * 10)

    pth = os.getcwd() + '/../data/data2.txt'
    data_QU = QuickUnion(data_path=pth)
    print("Quick Union:", data_QU.get_data())
    data_PCQU = QuickUnion(data_path=pth, improvement="compressing")
    print("Path compressed Quick Union:", data_PCQU.get_data())

    data_WQUPC = QuickUnion(data_path=pth, improvement="all")
    print("Weighted path compressed Quick Union:", data_WQUPC.get_data())

    
