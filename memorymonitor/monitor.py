#!/usr/bin/env python3
#
#
import pandas
import matplotlib.pyplot as plt
from data import Data


class Monitor:
    """Monitor for memory information

    Displays Linux-memory info
    Arguments:
        data ---> Required dictionary
    usage:
        Monitor().show()
    """
    def show(self, data):
        dataframe = pandas.DataFrame(data=list(data.items()),
                                     columns=['Title', 'memory'])
        ax = dataframe.plot(kind='barh', x='Title',
                            y='memory', width=1, fontsize=13)
        total = []

        for i in ax.patches:
            total.append(i.get_width())
        total = sum(total)
        for i in ax.patches:
            ax.text(i.get_width()+.3, i.get_y()+.38,
                    str(round((i.get_width()/total)*100, 2))+'%',
                    fontsize=8, color='black')
        ax.invert_yaxis()
        return plt.show()


if __name__ == '__main__':
    config = "configuration.json"
    data = Data(config)
    data = data.get_tuple()
    monitor = Monitor()
    monitor.show(data)
