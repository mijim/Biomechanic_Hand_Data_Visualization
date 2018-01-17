#Example usage: python visualize_data.py cybh data_example/cyberglobe/Ensayo_2_CGL_Cable.txt

import matplotlib.pyplot as plt
import numpy as np
import sys


def plotCyberH(file):
    roll1, mcf1, ifd1, a1, mcf2, ifp2, ifd2, a2, mcf3, ifp3, ifd3, a3, mcf4, ifp4, ifd4, a4, mcf5, ifp5, ifd5, a5, roll5, c, c_ano, usado = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split(' ')
            roll1.append(line_array[1])
            roll5.append(line_array[20])
            c.append(line_array[21])
            c_ano.append(line_array[22])
            usado.append(line_array[23])

            mcf1.append(line_array[2])
            ifd1.append(line_array[3])
            a1.append(line_array[4])

            mcf2.append(line_array[5])
            ifp2.append(line_array[6])
            a2.append(line_array[7])

            mcf3.append(line_array[8])
            ifp3.append(line_array[9])
            ifd3.append(line_array[10])
            a3.append(line_array[11])

            mcf4.append(line_array[12])
            ifp4.append(line_array[13])
            ifd4.append(line_array[14])
            a4.append(line_array[15])

            mcf5.append(line_array[16])
            ifp5.append(line_array[17])
            ifd5.append(line_array[18])
            a5.append(line_array[19])
        line_num+=1

    max_yticks = 3
    yloc = plt.MaxNLocator(max_yticks)

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 6
    fig_size[1] = 8
    plt.rcParams["figure.figsize"] = fig_size

    f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, sharex=True, sharey=True)
    f.canvas.set_window_title('Ensayo cyberhand')
    ax1.yaxis.set_major_locator(yloc)
    ax2.yaxis.set_major_locator(yloc)
    ax3.yaxis.set_major_locator(yloc)
    ax4.yaxis.set_major_locator(yloc)
    ax5.yaxis.set_major_locator(yloc)
    ax6.yaxis.set_major_locator(yloc)

    ax1.plot(mcf1, label="mcf1" ,linewidth=1)
    ax1.plot(ifd1, label="ifd1" ,linewidth=1)
    ax1.plot(a1, label="a1",linewidth=1)
    ax1.legend(loc=4)

    ax2.plot(mcf2, label="mcf2",linewidth=1)
    ax2.plot(ifp2, label="ifp2",linewidth=1)
    ax2.plot(a2, label="a2",linewidth=1)
    ax2.legend(loc=4)

    ax3.plot(mcf3, label="mcf3",linewidth=1)
    ax3.plot(ifd3, label="ifd3",linewidth=1)
    ax3.plot(ifp3, label="ifp3",linewidth=1)
    ax3.plot(a3, label="a3",linewidth=1)
    ax3.legend(loc=4)

    ax4.plot(mcf4, label="mcf4",linewidth=1)
    ax4.plot(ifd4, label="ifd4",linewidth=1)
    ax4.plot(ifp4, label="ifp4",linewidth=1)
    ax4.plot(a4, label="a4",linewidth=1)
    ax4.legend(loc=4)

    ax5.plot(mcf5, label="mcf5",linewidth=1)
    ax5.plot(ifd5, label="ifd5",linewidth=1)
    ax5.plot(ifp5, label="ifp5",linewidth=1)
    ax5.plot(a5, label="a5",linewidth=1)
    ax5.legend(loc=4)

    ax6.plot(roll1, label="roll1",linewidth=1)
    ax6.plot(roll5, label="roll5",linewidth=1)
    ax6.plot(c, label="c",linewidth=1)
    ax6.plot(c_ano, label="c_ano",linewidth=1)
    ax6.plot(usado, label="usado",linewidth=1)
    ax6.legend(loc=4)

    plt.subplots_adjust(bottom=0.05, left=0.09, top=0.97, hspace=0.00, right=0.96)
    plt.show()

def main():
    op = sys.argv[1]
    file = open(sys.argv[2], "r")
    if(op=="cybh"):
        plotCyberH(file)

if __name__== "__main__":
    main()
