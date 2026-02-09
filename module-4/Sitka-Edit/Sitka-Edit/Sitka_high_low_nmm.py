
import csv
from datetime import datetime

from matplotlib import pyplot as plt

def main():
    filename = 'sitka_weather_2018_simple.csv' #File is in same directory as python script
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

     # Get dates and high temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    #Generate matplotlib so keypress can take use from it
    fig, ax = plt.subplots()
    #Decided maybe having the instructions listed in the graph might be useful
    ax.set_title("Press H = Highs | L = Lows | Q = Quit")

    #Add keypress function to main so I can access the variables. Not sure How else I could have done this...
    #Decided to do a keypress since I couldnt get the console and matplotlib to work in unison found how to do it here https://matplotlib.org/stable/gallery/event_handling/keypress_demo.html
    def KeyPress(event):

        #Converted all keys to lower case in the event they had caps lock on. Not sure if that would affect it but decided to be safe
        if event.key.lower() == 'h': #Sets graph Highs
            #clears plots found from https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
            plt.cla()
            ax.plot(dates, highs, c='red')
            ax.set_title("Daily High Temperatures - 2018", fontsize = 24)

            #I repeat these in both so any random key doesnt change the graph
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.autofmt_xdate()
            fig.canvas.draw_idle()
        elif event.key.lower() == 'l': #Sets graph Lows
            #clears plots found from https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
            plt.cla()
            ax.plot(dates, lows, c='blue')
            ax.set_title("Daily Low Temperatures - 2018", fontsize = 24)

            #I repeat these in both so any random key doesnt change the graph
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            fig.autofmt_xdate()
            fig.canvas.draw_idle()
        elif event.key.lower() == 'q': 
            plt.close('all')
     
    #Intro to controls and pauses for an input to allow the user to read before the graph shows        
    print("Hello, This program will allow you to generate a graph with the Lows and a graph with the Highs. The commands will be (h) for Highs, (l) for Lows, or (e) for Exit.\n")
    input('Press enter key to continue to the graph...')
    fig.canvas.mpl_connect('key_press_event', KeyPress) #Calls the keypress function when a key is pressed
    plt.show() 
 
       


#if check to potentially use this function in a future program without triggering main. Took inspiration from the textbook for this
if __name__ == '__main__': 
    main()
