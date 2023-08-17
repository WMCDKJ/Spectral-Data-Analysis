# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:59:41 2023

@author: USER
"""

import numpy as np
import matplotlib 
import guilib as gb
import os

data = {
        "column_1": [],
        "column_2": [],
        "points" : [],
        "textbox": None,
}

def load_data(location):

    temp_dict =  {}

    # Loop through each file in the folder
    for file_name in os.listdir(location):
        if file_name.startswith("measurement_") and file_name.endswith(".txt"):
            file_path = os.path.join(location, file_name)
            temp_first_column_list = []
            temp_second_column_list = []

            # Open each file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            #Read each file linewise  
            for line in lines:
                #Split values of each line
                columns = line.strip().split()
                #Storing the split values in a list
                first_column_value = float(columns[0])
                second_column_value = float(columns[1])
                temp_first_column_list.append(first_column_value)
                temp_second_column_list.append(second_column_value)
            
            #Forming the x axis
            data["column_1"] = temp_first_column_list
            #Create a temporary list for each file and store the split values for column2
            temp_dict[file_name] = temp_second_column_list

    #Create a new list to the same length as the temporary list and initialize each value to zero
    second_column = [0.0] * len(temp_dict["measurement_0.txt"])

    #Outer loop through keys(k) and values(v) of the temporary dictionary
    for k, v in temp_dict.items():
        #Inner loop through indices(j)
        for j in range(len(v)):
            #Summing the values of second column in each file row wise
            second_column[j] += v[j]

    #Forming the y axis
    data["column_2"] = second_column
        
    gb.open_msg_window("Info", "Data loaded Successfully!", error=False)

def plot_data():
    
    #Prompting user to load data if there is no data
    if not data["column_1"] and not data["column_2"]:
        gb.open_msg_window("Error", "Please load data first", error=True)

    #Plotting the data
    else:
        subplot.plot(data["column_1"], data["column_2"], 'blue')
        canvas.draw()
    
def select_points(event):

    #Recording two click points   
    global count
 
    if count == 0:
        x = event.xdata
        y = event.ydata
        data["points"].append((x, y))
        subplot.plot(x, y, 'ro')  # Mark the first click on the plot
        canvas.draw()
        count = 1

    else:     
        x = event.xdata
        y = event.ydata
        data["points"].append((x, y))
        subplot.plot(x, y, 'ro')  # Mark the second click on the plot
        canvas.draw()
        count = 0       
            
        # Fit a line to the selected points  
        x_points, y_points = zip(*data["points"])
        coeffs = np.polyfit(x_points, y_points, 1)

        #Prompting user to load data if there is no data
        if not data["column_1"] and not data["column_2"]:
           gb.open_msg_window("Error", "Please load data first", error=True)
            
        else:
            # Calculate the fitted line values for the entire x range
            fitted_line = np.polyval(coeffs, data["column_1"])

            # Subtract the fitted line from column_2 data
            corrected_data = [y - fitted_line[i] for i, y in enumerate(data["column_2"])]

            # Plot the fitted line and the corrected data
            subplot.plot(data["column_1"], fitted_line, 'red', label='Fitted Line')
            subplot.plot(data["column_1"], corrected_data, 'green', label='Corrected Data')
            canvas.draw()

            #Determine the interval for intensity calculation
            interval_start, interval_end = data["points"][-2][0], data["points"][-1][0]
            x_data = np.array(data["column_1"])
            y_data = np.array(data["column_2"])
            
            # Find indices within the selected interval
            indices = np.where((x_data >= interval_start) & (x_data <= interval_end))
            
            # Calculate the intensity using the trapezoidal rule
            intensity = np.trapz(y_data[indices], x_data[indices])
            
            # Print the values into the textbox
            message = f"\nIntensity is ={intensity:.2f}\n"
            gb.write_to_textbox(data["textbox"], message)


def open_folder():
    folder_path = gb.open_folder_dialog("Open")
    load_data(folder_path)

def save_figure():
    save_path = gb.open_save_dialog(title="Save", initial=".")
    #figure.savefig('D:\Year 1 Period 4\Elementary Programming\Project\Myplot.png')
    figure.savefig(save_path)
    gb.open_msg_window("Info", "Saved Successfully", error=False)

def clear_plot():
    figure.clf
    figure.show
 
#______________________________GUI_______________________________________________________________________________________________________
     
# Create the window
window = gb.create_window("Photoionization spectrum of argon")
    
# Create the left frame for buttons
left_frame = gb.create_frame(window, side=gb.LEFT)
    
# Create the first button and connect it to load_data function
Loadbtn = gb.create_button(left_frame, "Load Data", open_folder)

# Create the second button and connect it to the plot_data function
Pltbtn = gb.create_button(left_frame, "Plot Data", plot_data) 

# Create the third button and connect it to the remove background function
#RemBackbtn = gb.create_button(left_frame, "Remove Background", remove_background)

# Create the forth button and connect it to the calculate intensities function 
#CalIntbtn = gb.create_button(left_frame, "Calculate intensities", calculate_intensities)

# Create the save button and connect it to the save function
Savebtn = gb.create_button(left_frame, "Save", save_figure)

# Create the clear button and connect it to the save function
Clrbtn = gb.create_button(left_frame, "Clear", clear_plot)

# Create the quit button and connect it to the quit function from the library
Qbtn = gb.create_button(left_frame, "Quit", gb.quit)

# Create the right frame for the figure
right_frame = gb.create_frame(window, side = gb.TOP)

# Create the figure and add it to the right frame
canvas,figure, subplot = gb.create_figure(right_frame, select_points, 500, 500)
count = 0

# Create the textbox and assign it to the state dictionary
textbox = gb.create_textbox(right_frame)
data["textbox"] = textbox

subplot.set_xlabel('Binding energy (eV)')
subplot.set_ylabel('Intensity (arbitrary units)')
subplot.set_title('Electron Spectrum')

gb.start()
    

