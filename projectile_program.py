#Ben Bland


from math import pi, sin, cos, radians
import matplotlib.pyplot as plt
import proj


def main():
    #gaining user input values
    angle=float(input("Enter the launch angle (in degrees): "))
    vel=float(input("Enter the initial velocity (in meters/sec): "))
    h0=float(input("Enter the initial height (in meters): "))
    time=float(input("Enter the time interval between position calculations: "))
    #converting degrees to radians for later calculations
    theta=radians(angle)
    #instantiating the class
    proj1=proj.Projectile(angle,vel,h0,time,theta)
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    xlist=[]
    ylist=[]
    maxheight=((yvel**2)*(sin(2*theta)))/(2*9.8)
    print("The max height that the projectile will reach will be ",format(maxheight,'.2f'),"meters.")
    #creating a loop that updates projectile position over time
    while ypos>=0:
        xpos,ypos,yvel=proj1.update(time,xpos,xvel,yvel,ypos)
        ylist.append(ypos)
        xlist.append(xpos)
        print(ypos,yvel)
    print("\nDistance traveled: ",format(xpos,'.2f'),"meters.")
    
    #creating a plot using matplotlib.pyplot
    plt.plot(xlist,ylist,"b-")
    plt.xlabel("X-position")
    plt.ylabel("Y-position")
    plt.title("Projectile Movement")
    plt.show()
    
    
#calling the main function
main()
        
    
