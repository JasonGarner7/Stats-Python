import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    def readFromFile(filename):
        with open(filename, 'r') as file:
            reading = True
            category = []
            date = []
            data = []
            data_size = 0
            i = 0
            while reading:
                line = file.readline()
                # stop at end of file
                if line == '':
                    reading = False
                # skip the first line
                elif line[:8] == 'Category' or line == '\n':
                    continue
                # set the categories for particular data set
                elif line[:5] == 'Month' or line[:4] == 'Week':
                    if line.find('Switch') != -1:
                        category.append('Nintendo Switch')
                    if line.find('Xbox One') != -1:
                        category.append('Xbox One')
                    if line.find('PlayStation 4') != -1:
                        category.append('PlayStation 4')
                    if line.find('Xbox Series X') != -1:
                        category.append('Xbox Series X')
                    if line.find('PlayStation 5') != -1:
                        category.append('PlayStation 5')
                    if line.find('Steam') != -1:
                        category.append('Steam')
                    if line.find('Epic') != -1:
                        category.append('Epic Games')
                    for item in category:
                        data_size += 1
                        data.append([])
                # add data into arrays
                else:
                    split = line.split(',')
                    count = 0
                    for item in split:
                        if count == 0:
                            date.append(item)
                        else:
                            if count <= data_size:
                                item = int(item)
                                data[count-1].append(item)
                        count += 1
                    i += 1
            # build line charts from data
            fig, ax = plt.subplots(figsize=(8, 8))
            count = 0
            for item in data:
                if count == 0:
                    df = pd.DataFrame({'x': date, category[count]: item})
                    plt.plot(date, category[count], data=df, marker='', markersize=4, color='skyblue', linewidth=2)
                elif count == 1:
                    df = pd.DataFrame({'x': range(0, len(item)), category[count]: item})
                    plt.plot('x', category[count], data=df, marker='', markersize=4, color='lightcoral', linewidth=2)
                elif count == 2:
                    df = pd.DataFrame({'x': range(0, len(item)), category[count]: item})
                    plt.plot('x', category[count], data=df, marker='', markersize=4, color='limegreen', linewidth=2)
                count += 1
            # implement appropriate labels
            plt.legend()
            plt.ylabel('Level of Interest')
            for n, label in enumerate(ax.xaxis.get_ticklabels()):
                if n % 10 != 0:
                    label.set_visible(False)
            plt.xticks(rotation=25)
            plt.xlabel(date[0][:4]+' - '+date[-1][:4])
            chart_title = ''
            for item in category:
                if item == category[-1]:
                    chart_title += item
                else:
                    chart_title += item+' vs. '
            plt.title(chart_title)
            plt.savefig(chart_title+'.png')


    readFromFile('xbox_ps4_2013-2020.csv') # video game console
    readFromFile('switch_xbox_ps4_2017-2020.csv') # video game console
    readFromFile('seriesx_ps5.csv') # search terms, last 12 months
    readFromFile('steam_epic_2017-2020.csv') # services

    # The PS4 has sold 106.99 million units lifetime,
    # the Switch 50.51 million units,
    # and the Xbox One 46.36 million units.
    # Looking at the marketshare, the PlayStation 4 has a 52 percent market share,
    # the Switch sits at 25 percent,
    # and the Xbox One 23 percent.
    plt.figure(figsize=(8, 8))
    labels = ['Playstation 4', 'Xbox One', 'Switch']
    data = [106.99, 46.36, 50.51]
    plt.bar(np.arange(len(labels)), data, align='center', alpha=0.5, label=labels)
    plt.xticks(np.arange(len(labels)), labels, rotation=25)
    plt.ylabel('Units Sold in Millions')
    plt.title('Video Game Console Lifetime Sales')
    plt.savefig('Console-Lifetime-Sales.png')


    # Epic Games had 61 million monthly users, 13 million average concurrent player count
    # Steam had 95 million, between 14 and 20 million concurrent player count
    plt.figure(figsize=(8, 8))
    labels = ['Epic Monthly Users', 'Steam Monthly Users', 'Epic Concurrent', 'Steam Concurrent']
    data = [61, 95, 13, 17]
    plt.bar(np.arange(len(labels)), data, align='center', alpha=0.5, label=labels)
    plt.xticks(np.arange(len(labels)), labels, rotation=25)
    plt.ylabel('in Millions')
    plt.title('PC Gaming Platform Users 2019')
    plt.savefig('PC-Monthly-And-Concurrent-Users.png')
