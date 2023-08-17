# Spectral-Data-Analysis
Analyzing the photoionization spectrum of argon. 

***Introduction***
In electron spectroscopy matter is examined by radiating it with a bright light and measuring the kinetic energy of electrons that come off it. 
When the photonic energy of light and kinetic energy of the electrons are known, they can be used to derive the amount of force that was required to break off the electrons. 
This provides valuable information about the matter's electron structure, and its chemical and physical properties. 
This phenomenon where photons break off electrons is called photoionization, and the broken off electrons are called photoelectrons.

The program is for analyzing the photoionization spectrum of argon. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Data***
The "spektridata" folder contains simulated data where argon atoms have been ionized and the kinetic energy of broken off electrons has been measured.
The measurement has been performed multiple times, and each measurement session has been recorded into a different, numbered file. 
The file names are in the format measurement_i.txt. Each file contains rows of data with two floating point numbers. 
The first number on each line is the binding energy of electrons, derived from the measured kinetic energy (unit: electronvolt); 
the second number is the corresponding intensity (no specific unit; 
this described the amount of electrons measured with this particular binding energy). 
In each measurement file, the first column contains the same uniformly distributed binding energy values. 
The program adds together the intensity values from each file. The purpose is to eliminate noise from the measurements.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Functionality***
Due to the measuring equipment, the spectrum has a linear background. Aside from the obvious peaks it looks like a downward sloping line. 
The background signal that causes the sloping is removed before analyzing the spectrum. 
This is done by choosing two points from the spectrum and fitting a line between these points. 
After this, at each data point, values obtained from this line are subtracted from the measured intensity values.
When analyzing the spectrum our primary interest are the two rather obvious peaks in intensity; in particular, their relative intensity. 
The intensity of each peak is obtained by computing their area by obtaining its integral. 
This is obtained by using the trapezoidal rule to estimate the integral. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

***User Controls***
Load data: loads data from a user-specified location and reads it into program memory.
Plot data: plots the current data (the user is prompted to load the data first if it hasn't been loaded yet). 
Remove linear background: when two points in the plot are clicked, this removes the linear background from the data after drawing a line as described above. If there's no data in the program memory yet, the user is given an error message about it.
Calculate intensities: Once the user selects the interval by clicking on the figure, the intensity of peaks is calculated. The result is printed in the text box below the plot. If there's no data in the program memory yet, the user is given an error message about it.
Save figure: saves an image of the current plot. The user uses a separate dialog for select a filename and destination for saving the figure. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

***Libraries***
guilib developed by university of Oulu has been used to design the Graphical Use Interfaces. Additionally matplotlib and numpy has been used.
