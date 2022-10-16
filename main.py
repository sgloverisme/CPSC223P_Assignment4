from weather import *  #gets all functions from weather
#import json

file ="weather.dat"

mychoice=0
while(True):
    print("          *** TUFFY TITAN WEATHER LOGGER MAIN MENU           \n")
    print("1. Set data filename")
    print("2. Add weather data ")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")

    mychoice= input("Enter menu choice: ")
    print()
    
    ## menu choice execution
    if mychoice == '1':  # menu choice 1 
        myfile= input("Enter data filename:")
        weather=read_data(myfile)
    elif mychoice == '2': #menu choice 2 
        dt =  input("Enter date (YYYYMMDD): ")
        tm = input("Enter time (hhmmss): ")
        t = int(input("Enter temperature: "))
        h = int(input("Enter humidity: "))
        r = float(input("Enter rainfall: "))
        weather[dt+tm] = {'t':t, 'h':h, 'r':r}
        write_data(weather, myfile) # write_data (new filename, where i am getting the data from)
    elif mychoice == '3': #menu choice 3
        d = input("Enter date: ") #string
        display = report_daily(weather, d)
        print(display)
    elif mychoice=='4': 
        display = report_historical(weather)
        print(display)
    elif mychoice == '9':
        break

