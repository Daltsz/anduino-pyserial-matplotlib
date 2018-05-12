import serial
import matplotlib.pyplot as plt
import numpy as np


def plot_together(count, data_umi, data_temp):


    #this fuction plot the graphs togethers

    # convert the count in array of int and save in the variable x
    x = np.arange(count)

    # figure 1 with 2 datas

    fig1 = plt.figure(1)

    # create a graph with 2 rows but only one column
    # first data
    numtemp = fig1.add_subplot(2, 1, 1)
    numtemp.plot(x, data_umi, 'blue')
    numtemp.set_title('umidity')

    # second data in the second row
    numtemp = fig1.add_subplot(2, 1, 2)
    numtemp.plot(x, data_temp, 'red')
    numtemp.set_title('Temperature')
    plt.savefig('plot-tempumi')



def plot_separate(data_umi, data_temp):

    # this function plot separete the graphs
    # the first is umidity

    plt.plot(data_umi)
    plt.title('Umidity')
    plt.savefig('plot-umi.png')
    plt.gcf().clear()

    # second is temperature
    plt.plot(data_temp)
    plt.title('Temperature')
    plt.savefig('plot-temp.png')
    plt.gcf().clear()


if __name__ == '__main__':

    ser = serial.Serial('COM3', 9600)
    count = 0
    data_umi = []
    data_temp = []


    while count <= 5:

        #convert the data binary to simple character
        out = ser.readline().decode('utf-8', 'strict')

        # breack in the middle the array
        out = out.split(' ')
        # paste datas behind of datas
        data_umi.append(out[2])
        data_temp.append(out[7])

        # make a print side by side
        print('Loading Graph .....', end= ' ',  flush=True)
        count += 1



plot_separate(data_umi, data_temp)
plot_together(count, data_umi, data_temp)





