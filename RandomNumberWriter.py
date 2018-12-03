# Ben Bland
# this program will write a series of random numbers to a file
# the application will let the user specify how many numbers the file will hold

import random

def main():

    try:
        randomNumber = random.randint(1, 500)
        outfile = open('numberfile.txt', 'w')
        x = int(input("How many random numbers are required? "))
        while x!=0:
            outfile.write(str(randomNumber)+'\n')
            x-=1
            randomNumber = random.randint(1, 500)
        outfile.close()
        print("The numbers have been written to 'numberfile.txt'")
    except IOError:
        print('An error occured writing the file.')
    except ValueError:
        print('Cannot write non numeric data to the file.')
    except:
        print('An error occured involving the file.')

main()
