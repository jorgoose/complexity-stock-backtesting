import numpy as np

# Creating a list of filenames
filenames = ['s&p_data\\constituents_complexity.txt', 's&p_data\\constituents_performance.txt']
  
complexity_x_axis = []
performance_y_axis = []

with open('s&p_data\\constituents_complexity.txt') as xh:
    with open('s&p_data\\constituents_performance.txt') as yh:
        with open("s&p_data\\plot_data.csv","w") as zh:

            #Read first file
            xlines = xh.readlines()

            #Read second file
            ylines = yh.readlines()

            print(ylines[2])

            #Combine content of both lists
            zlines = []
            for i in range(len(xlines)):

                zlines.append(xlines[i].strip() + "," + ylines[i].split(',')[1])

                if ((ylines[i].split(',')[1] != 'None\n') and ((xlines[i].split(',')[1]) != 'null\n')):
                    print(i)
                    complexity_x_axis.append(float(xlines[i].split(',')[1]))
                    print(ylines[0])
                    print(ylines[1])
                    print(ylines[i].split(',')[1])
                    performance_y_axis.append(float(ylines[i].split(',')[1]))

            #Write to third file
            for i in range(len(zlines)):
                line = zlines[i]
                print(line)
                zh.write(line)


    correlation = np.corrcoef(complexity_x_axis, performance_y_axis)
    print(correlation)

