#Example usage: python visualize_data.py cybh data_example/cyberglobe/Ensayo_2_CGL_Cable.txt

import matplotlib.pyplot as plt
import numpy as np
import sys

def getYTicksAxis(array):
    array=[float(x) for x in array]
    return [(min(array) + (min(array) + (min(array) + max(array)) / 2) / 2) / 2, (min(array) + max(array)) / 2, (max(array) + (max(array) + (min(array) + max(array)) / 2) / 2) / 2]

def plotIMU(file):
    w,x,y,z = [],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split('\t')
            w.append(float(line_array[1]))
            x.append(float(line_array[2]))
            y.append(float(line_array[3]))
            z.append(float(line_array[4]))

        line_num += 1

    #max_yticks = 8
    #yloc = plt.MaxNLocator(max_yticks)

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 8.5
    fig_size[1] = 7.7
    plt.rcParams["figure.figsize"] = fig_size


    f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=False)
    f.canvas.set_window_title('Ensayo IMU')

    #ax1.yaxis.set_major_locator(yloc)
    #ax2.yaxis.set_major_locator(yloc)
    #ax3.yaxis.set_major_locator(yloc)
    #ax4.yaxis.set_major_locator(yloc)

    ax1.plot(w, label="w" ,linewidth=1)
    ax1.set_yticks(getYTicksAxis(w))
    ax1.legend(loc=4)

    ax2.plot(x, label="x" ,linewidth=1)
    ax2.set_yticks(getYTicksAxis(x))
    ax2.legend(loc=4)

    ax3.plot(y, label="y" ,linewidth=1)
    ax3.set_yticks(getYTicksAxis(y))
    ax3.legend(loc=4)

    ax4.plot(z, label="z" ,linewidth=1)
    ax4.set_yticks(getYTicksAxis(z))
    ax4.legend(loc=4)

    plt.subplots_adjust(bottom=0.05, left=0.09, top=0.97, hspace=0.00, right=0.96)
    plt.show()


def plotVMG30(file):
    f11,f12,f21,f22,f31,f32,f41,f42,f51,f52,abd1,abd2,abd3,abd4,pa,tco,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,hroll,hpitch,hyaw,wroll,wpitch,wyaw = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split('\t')

            f11.append(line_array[1])
            f12.append(line_array[2])
            f21.append(line_array[3])
            f22.append(line_array[4])

            f31.append(line_array[5])
            f32.append(line_array[6])
            f41.append(line_array[7])
            f42.append(line_array[8])

            f51.append(line_array[9])
            f52.append(line_array[10])
            pa.append(line_array[15])
            tco.append(line_array[16])

            abd1.append(line_array[11])
            abd2.append(line_array[12])
            abd3.append(line_array[13])
            abd4.append(line_array[14])

            p1.append(line_array[17])
            p2.append(line_array[18])
            p3.append(line_array[19])
            p4.append(line_array[20])
            p5.append(line_array[21])

            p6.append(line_array[22])
            p7.append(line_array[23])
            p8.append(line_array[24])
            p9.append(line_array[25])
            p10.append(line_array[26])

            hroll.append(line_array[27])
            hpitch.append(line_array[28])
            hyaw.append(line_array[29])

            wroll.append(line_array[30])
            wpitch.append(line_array[31])
            wyaw.append(line_array[32])
        line_num+=1

    max_yticks = 3
    yloc = plt.MaxNLocator(max_yticks)

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 8
    fig_size[1] = 7.7
    plt.rcParams["figure.figsize"] = fig_size

    f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8, sharex=True, sharey=True)
    f.canvas.set_window_title('Ensayo VMG30')
    ax1.yaxis.set_major_locator(yloc)
    ax2.yaxis.set_major_locator(yloc)
    ax3.yaxis.set_major_locator(yloc)
    ax4.yaxis.set_major_locator(yloc)
    ax5.yaxis.set_major_locator(yloc)
    ax6.yaxis.set_major_locator(yloc)
    ax7.yaxis.set_major_locator(yloc)
    ax8.yaxis.set_major_locator(yloc)

    ax1.plot(f11, label="f11" ,linewidth=1)
    ax1.plot(f12, label="f12" ,linewidth=1)
    ax1.plot(f21, label="f21",linewidth=1)
    ax1.plot(f22, label="f22",linewidth=1)
    ax1.legend(loc=4)

    ax2.plot(f31, label="f31",linewidth=1)
    ax2.plot(f32, label="f32",linewidth=1)
    ax2.plot(f41, label="f41",linewidth=1)
    ax2.plot(f42, label="f42",linewidth=1)
    ax2.legend(loc=4)

    ax3.plot(f51, label="f51",linewidth=1)
    ax3.plot(f52, label="f52",linewidth=1)
    ax3.plot(pa, label="pa",linewidth=1)
    ax3.plot(tco, label="tco",linewidth=1)
    ax3.legend(loc=4)

    ax4.plot(abd1, label="abd1",linewidth=1)
    ax4.plot(abd2, label="abd2",linewidth=1)
    ax4.plot(abd3, label="abd3",linewidth=1)
    ax4.plot(abd4, label="abd4",linewidth=1)
    ax4.legend(loc=4)

    ax5.plot(p1, label="p1",linewidth=1)
    ax5.plot(p2, label="p2",linewidth=1)
    ax5.plot(p3, label="p3",linewidth=1)
    ax5.plot(p4, label="p4",linewidth=1)
    ax5.plot(p5, label="p5",linewidth=1)
    ax5.legend(loc=4)

    ax6.plot(p6, label="p6",linewidth=1)
    ax6.plot(p7, label="p7",linewidth=1)
    ax6.plot(p8, label="p8",linewidth=1)
    ax6.plot(p9, label="p9",linewidth=1)
    ax6.plot(p10, label="p10",linewidth=1)
    ax6.legend(loc=4)

    ax7.plot(hroll, label="hroll",linewidth=1)
    ax7.plot(hpitch, label="hpitch",linewidth=1)
    ax7.plot(hyaw, label="hyaw",linewidth=1)
    ax7.legend(loc=4)

    ax8.plot(wroll, label="wroll",linewidth=1)
    ax8.plot(wpitch, label="wpitch",linewidth=1)
    ax8.plot(wyaw, label="wyaw",linewidth=1)
    ax8.legend(loc=4)

    plt.subplots_adjust(bottom=0.05, left=0.09, top=0.97, hspace=0.00, right=0.96)
    plt.show()

def plotCyberH(file):
    roll1, mcf1, ifd1, a1, mcf2, ifp2, ifd2, a2, mcf3, ifp3, ifd3, a3, mcf4, ifp4, ifd4, a4, mcf5, ifp5, ifd5, a5, roll5, c, c_ano, usado = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split(' ')
            roll1.append(line_array[1])
            roll5.append(line_array[21])
            c.append(line_array[22])
            c_ano.append(line_array[23])
            usado.append(line_array[24])

            mcf1.append(line_array[2])
            ifd1.append(line_array[3])
            a1.append(line_array[4])

            mcf2.append(line_array[5])
            ifp2.append(line_array[6])
            ifd2.append(line_array[7])
            a2.append(line_array[8])

            mcf3.append(line_array[9])
            ifp3.append(line_array[10])
            ifd3.append(line_array[11])
            a3.append(line_array[12])

            mcf4.append(line_array[13])
            ifp4.append(line_array[14])
            ifd4.append(line_array[15])
            a4.append(line_array[16])

            mcf5.append(line_array[17])
            ifp5.append(line_array[18])
            ifd5.append(line_array[19])
            a5.append(line_array[20])
        line_num+=1

    fig, ((ax1, ax2, ax3, ax4, ax5, ax6), (ax7,ax8,ax9,ax10,ax11,ax12),(ax13,ax14,ax15,ax16, ax17,ax18),(ax19,ax20,ax21,ax22,ax23,ax24)) = plt.subplots(4, 6)
    fig.canvas.set_window_title('Ensayo CyberGlobe')
    max_yticks = 1
    yloc = plt.MaxNLocator(max_yticks)
    removeXYAxis(ax1)
    removeXYAxis(ax2)
    removeXYAxis(ax3)
    removeXYAxis(ax4)
    removeXYAxis(ax5)
    removeXYAxis(ax6)
    removeXYAxis(ax7)
    removeXYAxis(ax8)
    removeXYAxis(ax9)
    removeXYAxis(ax10)
    removeXYAxis(ax11)
    removeXYAxis(ax12)
    removeXYAxis(ax13)
    removeXYAxis(ax14)
    removeXYAxis(ax15)
    removeXYAxis(ax16)
    removeXYAxis(ax17)
    removeXYAxis(ax18)
    removeXYAxis(ax19)
    removeXYAxis(ax20)
    removeXYAxis(ax21)
    removeXYAxis(ax22)
    removeXYAxis(ax23)
    removeXYAxis(ax24)

    ax1.plot(mcf1,linewidth=0.8)
    ax1.set(title='mcf1')
    ax2.plot(mcf2,linewidth=0.8)
    ax2.set(title='mcf2')
    ax3.plot(mcf3,linewidth=0.8)
    ax3.set(title='mcf3')
    ax4.plot(mcf4,linewidth=0.8)
    ax4.set(title='mcf4')
    ax5.plot(ifd1,linewidth=0.8)
    ax5.set(title='ifd1')
    ax6.plot(ifd2,linewidth=0.8)
    ax6.set(title='ifd2')
    ax7.plot(ifd3,linewidth=0.8)
    ax7.set(title='ifd3')
    ax8.plot(ifd4,linewidth=0.8)
    ax8.set(title='ifd4')
    ax9.plot(ifd5,linewidth=0.8)
    ax9.set(title='ifd5')
    ax10.plot(ifp2,linewidth=0.8)
    ax10.set(title='ifp2')
    ax11.plot(ifp3,linewidth=0.8)
    ax11.set(title='ifp3')
    ax12.plot(ifp4,linewidth=0.8)
    ax12.set(title='ifp4')
    ax13.plot(ifp5,linewidth=0.8)
    ax13.set(title='ifp5')
    ax14.plot(a1,linewidth=0.8)
    ax14.set(title='a1')
    ax15.plot(a2,linewidth=0.8)
    ax15.set(title='a2')
    ax16.plot(a3,linewidth=0.8)
    ax16.set(title='a3')
    ax17.plot(a4,linewidth=0.8)
    ax17.set(title='a4')
    ax18.plot(a5,linewidth=0.8)
    ax18.set(title='a5')
    ax19.plot(roll1,linewidth=0.8)
    ax19.set(title='roll1')
    ax20.plot(roll5,linewidth=0.8)
    ax20.set(title='roll5')
    ax21.plot(c,linewidth=0.8)
    ax21.set(title='c')
    ax22.plot(c_ano,linewidth=0.8)
    ax22.set(title='c_ano')
    ax23.plot(usado,linewidth=0.8)
    ax23.set(title='usado')
    ax24.plot([],linewidth=0.8)
    ax24.set(title='None')
    fig.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    frame1 = plt.gca()

    plt.subplots_adjust(bottom=0.05, left=0.01, top=0.97, hspace=0.26, wspace=0.12,right=0.99)
    plt.show()

def removeXYAxis(ax):
    yloc = plt.MaxNLocator(3)
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_locator(yloc)


def main():
    op = sys.argv[1]
    file = open(sys.argv[2], "r")

    if(op=="cybh"):
        plotCyberH(file)
    elif(op=="vmg30"):
        plotVMG30(file)
    elif(op=="imu"):
        plotIMU(file)
    else:
        print("Unsuported operation: " + op)

if __name__== "__main__":
    main()
