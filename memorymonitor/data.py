#!/usr/bin/env python3
#
# Monitoring Linux-machine memory usage.
#
import os
import sys
import json


class Data:
    """Data returns dict of memory info

    Arguments:
        >>>Data(config=configuration.json)
    Usage:
        >>>get_tuple()
    """

    def __init__(self, config):
        self.config = config
        self.mayday = 1
        self.failure = 0

    def exit_now(self, command, filename=None):
        """Exit system

        Arguments:
            command >>> Specify type of command
            filename >>> filename. Will inform you about missing file
                         before exit

        """
        if command.upper() == 'F':
            sys.stderr.write("File {} is  not found!".format(filename))
            sys.exit(self.mayday)
        elif command.upper() == 'CF':
            sys.stderr.write("Configuration file required..")
            sys.exit(self.mayday)
        else:
            return False

    def data_from_json(self):
        if not os.path.isfile(self.config):
            self.exit_now('CF', self.config)
        data = open(self.config)
        data = json.load(data)
        return data

    def read_file(self):
        data = self.data_from_json()
        path = data['filename']['path']
        filename = data['filename']['file_']
        filename = path + filename
        if not os.path.isfile(filename):
            self.exit_now('f', filename)
        self.filename = open(filename, 'r')
        if not self.filename:
            return False
        return self.filename

    def get_tuple(self):

        # Two columns of data
        titles = []
        memory_in_kb = []
        trash = []
        # open the file in the readable format.
        filename = self.read_file()
        for line in filename:

            # Just two columns
            word = line.split()[:2]

            # Set a brake here
            # no need to plot all info
            # reason for a pause, just avoid large unnecessary values
            if word[1] == '0':
                trash.append(word)
            elif 'VmallocTotal:' in word:
                trash.append(word)
            else:
                titles.append(word[0].replace(':', ''))
                # Memory data in int.
                memory_in_kb.append(int(word[1]))
        to_dict = dict(zip(titles, memory_in_kb))
        return to_dict
