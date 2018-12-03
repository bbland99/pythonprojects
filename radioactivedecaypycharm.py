# Ben Bland 
# Mini Project Radioactive Decay


# Compute the total decay time, safe level of activity in
# material containing a percentage of a given radioactive isotope
import math
import time
import matplotlib.pyplot as plt
#declaring global variables
DisposalConstant = 37.00
DecayConstant = 0.693
HalfLifePhosp32 = 14.262
HalfLifeChrom51 = 27.7025


#create a function that calculates how many days until the safe activity level is reached
def DaysSafeLevel(halflife, DecayConstant, DisposalConstant, A_init, mass):
    daystodecay = -(halflife / DecayConstant) * (math.log(DisposalConstant / (A_init / mass)))
    return daystodecay


# create a function that calculates the safe activity level
def SafeActivityLevel(Ainit, DecayConstant, daytodecay, halflife):
    safeactivitylevel = Ainit * math.exp(-DecayConstant * daytodecay / halflife)
    return safeactivitylevel

#create a delay in the daily activity log
def wait(time_in_seconds):
    time.sleep(time_in_seconds)

#create phosphorus-32 function
def phosphorus32():
        try:
            isotopehalflife = HalfLifePhosp32
            materialmass = float(input("Please enter the mass of Phosphorus-32 in kilograms: "))
            A_initial = float(input("Please enter the initial activity of Phosphorus-32 in kBq: "))
            percent = float(input("Please enter the percent of Phosphorus-32 present in the mass: "))
            isotopemass = materialmass * (percent / 100)
            daycount = 0
            activitylist=[]
            daylist=[]

            print("")
            dayssafe = DaysSafeLevel(isotopehalflife, DecayConstant, DisposalConstant, A_initial, isotopemass)
            print("The time to safe disposal for the isotope is ", format(dayssafe,'.2f'), "days.")
            safeactivity = SafeActivityLevel(A_initial, DecayConstant, dayssafe, isotopehalflife)
            print("")
            print("The safe activity level for this isotope is ", format(safeactivity,'.2f'), "kBq.")
            print("")
            #creating loop that updates the values of the isotope over time
            while A_initial > safeactivity:
                daylist.append(daycount)
                activitylist.append(A_initial)
                print("Activity of Phosphorus-32 on Day", daycount, ": ", format(A_initial,'.2f'), "kBq.")
                A_initial = A_initial * math.exp(-DecayConstant / isotopehalflife)
                daycount += 1
                wait(.3)
            daylist.append(daycount)
            activitylist.append(A_initial)
            print("Activity of Phosphorus-32 on Day", daycount, ": ", format(A_initial,'.2f'), "kBq.")
            #creating graph
            plt.plot(daylist,activitylist,'b-')
            plt.xlabel("Day")
            plt.ylabel("Isotope Activity (kBq)")
            plt.title("Phosphorus-32 Activity by Day")
            plt.show()
        except ValueError:
            print("A value entered does not match the program format. Please restart the program and try again.")
        except IOError:
            print("There was an error with an input. Please restart the program and try again.")
        except:
            print("An unknown error has occurred. Please restart the program and try again.")
    
#create chromium51 function
def chromium51():
        try:
            isotopehalflife = HalfLifeChrom51
            materialmass = float(input("Please enter the mass in kilograms: "))
            A_initial = float(input("Please enter the initial activity of Chromium-51 in kBq: "))
            percent = float(input("Please enter the percent of Chromium-51 present in the mass: "))
            isotopemass = materialmass * (percent / 100)
            daycount=0
            daylist=[]
            activitylist=[]
            print("")
            dayssafe = DaysSafeLevel(isotopehalflife, DecayConstant, DisposalConstant, A_initial, isotopemass)
            print("The time to safe disposal for Chromium-51 is ", format(dayssafe,'.2f'), "days.")
            safeactivity = SafeActivityLevel(A_initial, DecayConstant, dayssafe, isotopehalflife)
            print("")
            print("The safe activity level for Chromium-51 is ", format(safeactivity,'.2f'), "kBq.")
            print("")

            while A_initial > safeactivity:
                daylist.append(daycount)
                activitylist.append(A_initial)
                print("Activity of the isotope on Day", daycount, ": ", format(A_initial, '.2f'), "kBq.")
                A_initial = A_initial * math.exp(-DecayConstant / isotopehalflife)
                daycount += 1
                wait(.3)
            daylist.append(daycount)
            activitylist.append(A_initial)
            print("Activity of the isotope on Day", daycount, ": ", format(A_initial, '.2f'), "kBq.")
            plt.plot(daylist,activitylist,'b-')
            plt.xlabel("Day")
            plt.ylabel("Isotope Activity (kBq)")
            plt.title("Chromium-51 Activity by Day")
            plt.show()
        except ValueError:
            print("A value entered does not match the program format. Please restart the program and try again.")
        except IOError:
            print("There was an error with an input. Please restart the program and try again.")
        except:
            print("An unknown error has occurred. Please restart the program and try again.")
    



    

def main():
    print("If you would like to investigate the Phosphorus-32 isotope, enter 1.")
    print("If you would like to investigate the Chromium-51 isotope, enter 2.")
    print("If you would like to exit the program, enter 0.")
    user_isotope = int(input())

    if user_isotope == 1:
        phosphorus32()

    elif user_isotope == 2:
        chromium51()
        
    elif user_isotope == 0:
        exit()

    else:
        print("Input not recognized. Please restart the program and try again.")


main()
