"""
DataScienceSS2020
@Modul      MyFirstModule
@copyright  2020 Yakup Yildirim - YYildir1@stud.hs-offenburg.de

This file is an exercise of the DataScienceSS2020 Course.
It provides the functionality to store any given List with his corresponding name.
"""

class ListKeeper:
    def __init__(self):
        self.data = dict()
        self.data['example']=[1,2,3,4,5]
    def show(self):
        return self.data.keys()
    def add(self, name, list):
        self.data[name]= list
    def delete(self, name):
        self.data.pop(name)
    def sort(self, name):
        return (self.data[name]).sort()
    def append(self, name, list):
        self.data[name].append(list)
