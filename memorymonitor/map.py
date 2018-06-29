#!/usr/bin/env python3
import os
import matplotlib.pyplot as plt
import numpy as np


class MemoryMonitor:
    """MemoryMonitor displays memory status of the linux

    Note down all memory data and visulazing with matplotlib
    Arguments:
        None
    Usage:
        >> Call MemoryMonitor
    Runs on Linux
    """

    def __init__(self):
        self.data = os.popen("free")
        self.header = self.data.readline()
        self.title = self.header.split()
        self.memory = self.data.readline()

    def plot_data(self):
        """Plot data plots memory information

        Plot data does the two main operation
        First one:
             Parse the data to required format
        Second part:
            plot the data
        """

        memory = self.memory.split()
        memory = memory[1:]
        memory = [int(i) for i in memory]

        swap = self.data.readline()
        swap = swap.split()
        if len(swap) < len(memory):
            reminder = len(memory)-len(swap)
            for _ in range(reminder+1):
                swap.append(0)
        swap = swap[1:]
        swap = [int(i) for i in swap]

        # set bar chart measurements
        N = len(memory)
        ind = np.arange(N)
        width = 0.40

        # Initialize graph
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # set two column
        memory_column = ax.bar(ind, memory, width, color='c')
        swap_column = ax.bar(ind+width, swap, width, color='m')

        ax.set_xticks(ind+width)
        ax.set_xticklabels((tuple(self.title)))
        ax.legend((memory_column[0], swap_column[0]), ('MEM', 'swap'))

        # Add title
        plt.title("Linux memory map")

        # Display the graph
        plt.show()
