import os
from random import *

import pygame
import time
import csv

from constants import *
from objects.ball import BallObject
from objects.platform import PlatformObject
from objects.text import TextObject
from scenes.base import BaseScene


class FileUploader:
    def __init__(self, name='-1', score=-1):
        self.data = [
            "name,score".split(","),
            f"{name},{score}".split(",")
        ]
        self.name = name
        self.score = score
        self.fieldnames = self.data[0]
        self.list = []

    def set_score(self, score):
        self.score = score
        self.data[1][1] = score
        print('set_score', self.data[1][1])

    def set_name(self, name):
        self.name = name
        self.data[1][0] = f'{name}'
        print('set_name', self.data[1][0])

    def read_file_data(self):
        self.data = [
            "name,score".split(","),
            f"{self.name},{self.score}".split(",")
        ]
        self.open_file()

    def open_file(self):
        with open("highscores.csv", encoding='utf-8') as data_f:
            reader = csv.DictReader(data_f, delimiter=",")
            for line in reader:
                self.data += [f"{line['name']},{line['score']}".split(',')]
            self.data += reader

    def packing(self):
        self.list = []
        for val in self.data[1:]:
            inner_dict = dict(zip(self.fieldnames, val))
            self.list.append(inner_dict)

    def write_file_data(self):
        self.packing()
        with open("highscores.csv", "tw", newline='', encoding='utf-8') as date_f:
            writer = csv.DictWriter(date_f, delimiter=',', fieldnames=self.fieldnames)
            writer.writeheader()
            for row in self.list:
                writer.writerow(row)

    def checking_for_name(self, name):
        self.read_file_data()
        for val in self.data[1:]:
            if val[0] == name:
                return 1
        return 0
