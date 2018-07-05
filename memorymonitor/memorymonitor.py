#!/usr/bin/env python3
#
# Monitoring Linux-machine memory usage.
#
import os
import sys
import json
import pandas as pd
import matplotlib.pyplot as plt


__all__ = ['Monitor']

# Use configuration
CONFIG = "configuration.json"
MADAY = 1


class Monitor:
    """Shows Memory info

    Arguments:
        None
    Usage:
        >>> Monitor().show()
        return bar graph
    """

    def from_json(self):
        if not CONFIG:
            sys.stderr.write("Configuration file required..")
            sys.exit(MADAY)
        data = open(CONFIG)
        data = json.load(data)
        return data

    def open_file(self):
        data = self.from_json()
        path = data['filename']['path']
        filename = data['filename']['file_']
        filename = path + filename
        if not os.path.isfile(filename):
            sys.stderr.write("File not found!")
            sys.exit(MADAY)
        self.filename = open(filename, 'r')
        if self.filename:
            return self.filename

    def data_to_list(self):

        # Two columns of data
        titles = []
        memory_in_kb = []

        # open the file in the readable format.
        filename = self.open_file()
        for line in filename:

            # Just two columns
            word = line.split()[:2]

            # Set a brake here
            # no need to plot all info
            # reason for a pause, just avoid large unnecessary values
            if 'VmallocTotal:' not in word:

                # Title
                titles.append(word[0].replace(':', ''))

                # Memory data in int.
                memory_in_kb.append(int(word[1]))
            else:
                # Break it before iterate over all items.
                break
        return titles, memory_in_kb

    def show(self):
        """Return bar graph"""

        _titles, _memory_in_kb = self.data_to_list()

        dataframe = {'name': _titles, 'memory(in KB)': _memory_in_kb}

        # Create data frame
        df = pd.DataFrame(data=dataframe)
        df.plot(kind='bar', x='name', y='memory(in KB)')

        # show
        return plt.show()
