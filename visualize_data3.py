#Example usage: python visualize_data3.py cybh data_example/cyberglobe/Ensayo_2_CGL_Cable.txt

import leather
import sys
import webbrowser
import os

def getYTicksAxis(array):
    array=[float(x) for x in array]
    return [(min(array) + (min(array) + (min(array) + max(array)) / 2) / 2) / 2, (min(array) + max(array)) / 2, (max(array) + (max(array) + (min(array) + max(array)) / 2) / 2) / 2]

def plotIMU(file,genereted_chart_file):
    w,x,y,z = [],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split('\t')
            w.append((line_num,float(line_array[1])))
            x.append((line_num,float(line_array[2])))
            y.append((line_num,float(line_array[3])))
            z.append((line_num,float(line_array[4])))

        line_num += 1

    lattice = leather.Lattice(leather.Line(stroke_color=None, width=2))
    lattice.add_many([w,x,y,z], titles=['w','x','y','z'])
    lattice.to_svg(genereted_chart_file,1700,950)
    webbrowser.open('file://' + os.path.realpath(genereted_chart_file))


def plotVMG30(file,genereted_chart_file):
    f11,f12,f21,f22,f31,f32,f41,f42,f51,f52,abd1,abd2,abd3,abd4,pa,tco,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,hroll,hpitch,hyaw,wroll,wpitch,wyaw = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    line_num = 0

    for line in file:
        if(line_num > 1):
            line_array = line.split('\t')

            f11.append((line_num,float(line_array[1])))
            f12.append((line_num,float(line_array[2])))
            f21.append((line_num,float(line_array[3])))
            f22.append((line_num,float(line_array[4])))

            f31.append((line_num,float(line_array[5])))
            f32.append((line_num,float(line_array[6])))
            f41.append((line_num,float(line_array[7])))
            f42.append((line_num,float(line_array[8])))

            f51.append((line_num,float(line_array[9])))
            f52.append((line_num,float(line_array[10])))
            pa.append((line_num,float(line_array[15])))
            tco.append((line_num,float(line_array[16])))

            abd1.append((line_num,float(line_array[11])))
            abd2.append((line_num,float(line_array[12])))
            abd3.append((line_num,float(line_array[13])))
            abd4.append((line_num,float(line_array[14])))

            p1.append((line_num,float(line_array[17])))
            p2.append((line_num,float(line_array[18])))
            p3.append((line_num,float(line_array[19])))
            p4.append((line_num,float(line_array[20])))
            p5.append((line_num,float(line_array[21])))

            p6.append((line_num,float(line_array[22])))
            p7.append((line_num,float(line_array[23])))
            p8.append((line_num,float(line_array[24])))
            p9.append((line_num,float(line_array[25])))
            p10.append((line_num,float(line_array[26])))

            hroll.append((line_num,float(line_array[27])))
            hpitch.append((line_num,float(line_array[28])))
            hyaw.append((line_num,float(line_array[29])))

            wroll.append((line_num,float(line_array[30])))
            wpitch.append((line_num,float(line_array[31])))
            wyaw.append((line_num,float(line_array[32])))
        line_num+=1

    lattice = leather.Lattice(leather.Line(stroke_color=None, width=0.5))
    lattice.add_many([f11,f12,f21,f22,f31,f32,f41,f42,f51,f52,abd1,abd2,abd3,abd4,pa,tco,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,hroll,hpitch,hyaw,wroll,wpitch,wyaw], titles=['f11','f12','f21','f22','f31','f32','f41','f42','f51','f52','abd1','abd2','abd3','abd4','pa','tco','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','hroll','hpitch','hyaw','wroll','wpitch','wyaw'])
    lattice.to_svg(genereted_chart_file,1700,950)
    webbrowser.open('file://' + os.path.realpath(genereted_chart_file))

def plotCyberH(file,genereted_chart_file):
    roll1, mcf1, ifd1, a1, mcf2, ifp2, ifd2, a2, mcf3, ifp3, ifd3, a3, mcf4, ifp4, ifd4, a4, mcf5, ifp5, ifd5, a5, roll5, c, c_ano, usado = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    line_num = 0
    
    for line in file:
        if(line_num > 1):
            line_array = line.split(' ')
            roll1.append((line_num,float(line_array[1])))
            roll5.append((line_num,float(line_array[21])))
            c.append((line_num,float(line_array[22])))
            c_ano.append((line_num,float(line_array[23])))
            usado.append((line_num,float(line_array[24])))

            mcf1.append((line_num,float(line_array[2])))
            ifd1.append((line_num,float(line_array[3])))
            a1.append((line_num,float(line_array[4])))

            mcf2.append((line_num,float(line_array[5])))
            ifp2.append((line_num,float(line_array[6])))
            ifd2.append((line_num,float(line_array[7])))
            a2.append((line_num,float(line_array[8])))

            mcf3.append((line_num,float(line_array[9])))
            ifp3.append((line_num,float(line_array[10])))
            ifd3.append((line_num,float(line_array[11])))
            a3.append((line_num,float(line_array[12])))

            mcf4.append((line_num,float(line_array[13])))
            ifp4.append((line_num,float(line_array[14])))
            ifd4.append((line_num,float(line_array[15])))
            a4.append((line_num,float(line_array[16])))

            mcf5.append((line_num,float(line_array[17])))
            ifp5.append((line_num,float(line_array[18])))
            ifd5.append((line_num,float(line_array[19])))
            a5.append((line_num,float(line_array[20])))
        line_num+=1

    lattice = leather.Lattice(leather.Line(stroke_color=None, width=0.5))
    lattice.add_many([roll1, mcf1, ifd1, a1, mcf2, ifp2, ifd2, a2, mcf3, ifp3, ifd3, a3, mcf4, ifp4, ifd4, a4, mcf5, ifp5, ifd5, a5, roll5, c, c_ano, usado], titles=['roll1', 'mcf1', 'ifd1', 'a1', 'mcf2', 'ifp2', 'ifd2', 'a2', 'mcf3', 'ifp3', 'ifd3', 'a3', 'mcf4', 'ifp4', 'ifd4', 'a4', 'mcf5', 'ifp5', 'ifd5', 'a5', 'roll5', 'c', 'c_ano', 'usado'])
    lattice.add_x_scale(0,line_num-30)
    lattice.add_y_scale(0,250),
    lattice.to_svg(genereted_chart_file,1700,950)
    webbrowser.open('file://' + os.path.realpath(genereted_chart_file))
    

def removeXYAxis(ax):
    yloc = plt.MaxNLocator(3)
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_locator(yloc)


def main():
    genereted_chart_file = 'generatedchart/lines.svg'
    op = sys.argv[1]
    file = open(sys.argv[2], "r")
    if(len(sys.argv) > 3):
        genereted_chart_file = sys.argv[3]
    
    if(op=="cybh"):
        plotCyberH(file,genereted_chart_file)
    elif(op=="vmg30"):
        plotVMG30(file,genereted_chart_file)
    elif(op=="imu"):
        plotIMU(file,genereted_chart_file)
    else:
        print("Unsuported operation: " + op)

    file.close()

if __name__== "__main__":
    main()
