import numpy as np
import matplotlib.pyplot as plt
def quadratic_models(time,a,b,c):
    temp = a* (time ** 2) + b * time + c
    return temp

time_vals = np.linspace(0,10,50)

def hardcoded() :
    a,b,c = 0.1,-1,30
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label ='Hardcoded coeff')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Hardcoded coeff')
    plt.show()
    plt.show()

def keyboard() :
    a = float(input("Enter the value of a : "))
    b = float(input("Enter the value of b : "))
    c = float(input("Enter the value of c : "))
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label ='User Input')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('user input')
    plt.show()

def singleset() :
    try:
        with open('single_set.txt', 'r') as file:
            line = file.readline()
            a, b, c = map(float, line.split())
            temperature_file_single = quadratic_models(time_vals, a, b, c)
            plt.plot(time_vals, temperature_file_single, label='Single File Input Coefficients')
    except FileNotFoundError:
        print("The file 'single_set.txt' was not found. Please make sure it exists.")
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Single Set')
    plt.show()

def multisetfile() :
    try:
        with open('multi_set.txt', 'r') as file:
            lines = file.readlines()
        
        for i, line in enumerate(lines):
            a, b, c = map(float, line.split())
            temperature_file_multiple = quadratic_models(time_vals, a, b, c)
            plt.plot(time_vals, temperature_file_multiple, label=f'File Input Set {i+1} Coefficients')
    except FileNotFoundError:
        print("The file 'multi_set.txt' was not found. Please make sure it exists.")
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multi Set from File')
    plt.show()

def multiset() :
    sets_of_coefficients = [{0.2,1.5,35},{-0.1,2.0,25},{0.3,-2,30}]
    # Plot each set of coefficients
    for i, (a, b, c) in enumerate(sets_of_coefficients):
        temperature = quadratic_models(time_vals, a, b, c)
        plt.plot(time_vals, temperature, label=f'Set {i+1}: a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Multi Set')
    plt.show()

def hardcoded_keyboard() :
    a,b,c = 0.1,-1,30
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label =f'Hardcoded coeff : a={a}, b={b}, c={c}')
    a = float(input("Enter the value of a : "))
    b = float(input("Enter the value of b : "))
    c = float(input("Enter the value of c : "))
    temp_hardcoded = quadratic_models(time_vals,a,b,c)
    plt.plot(time_vals,temp_hardcoded,label =f'User Input : a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title("Hardcoded and Input")
    plt.legend()
    plt.show()

def main() :
    hardcoded() #hardcoded values
    keyboard() #user input values
    singleset() #single set from file single_set.txt
    multisetfile() #multi set from file multi_set.txt
    multiset() #multi set declared
    hardcoded_keyboard() #hardcoded and userinput values together
main()
