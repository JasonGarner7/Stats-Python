if __name__ == '__main__':
    def readFromFile(filename):
        with open(filename, 'r') as file:
            if file.readline() == '':
                print("The file is empty")
            reading = True
            while reading:
                line = file.readline()
                if line == '':
                    reading = False
                print(file.readline())
                # TODO:
                #  parse through each line
                #  either build the charts here or store in variable and build elsewhere


    readFromFile('ps4_xbox_2013-2020.csv')
    readFromFile('2020_ps5.csv')
    readFromFile('2019_steam.csv') # search terms
    readFromFile('Steam_Epic_2017-2020.csv') # services


    # TODO:
    #   build chart comparing these numbers
    # The PS4 has sold 106.99 million units lifetime,
    # the Switch 50.51 million units,
    # and the Xbox One 46.36 million units.
    # Looking at the marketshare, the PlayStation 4 has a 52 percent market share,
    # the Switch sits at 25 percent,
    # and the Xbox One 23 percent.

    # TODO:
    #   build chart comparing these numbers
    # Epic Games had 61 million monthly users, 13 million average concurrent player count
    # Steam had 95 million, between 14 and 20 million concurrent player count
