# Biomechanic Hand Data Visualization

## Version 1.0

This version uses the matploitlib for making and showing the plot

### Dependecies

  * python 3+

  * matploitlib:
    * python -mpip install matplotlib
  
### Usage

python visualize_data.py \<option\> \<file\>

Supported options:
  * vmg30 - for vmg30 data
  * cybh - for cyberhand data
  * imu - for imu's data

Example usage: python visualize_data.py cybh data_example/cyberglobe/Ensayo_2_CGL_Cable.txt

Example usage2: python visualize_data.py vmg30 data_example/vmg30/20171103calib_miguel_1/Ensayo_15_VMR_Cable.txt

Example usage3: python visualize_data.py imu data_example/imu/Ensayo_1_IMU.txt


## Version 3.0

This version uses leather for making the plot as svg file and shows it with the default browser.

### Dependecies

  * python 3+

  * leather:
    *  pip install leather

### Usage

python visualize_data3.py \<option\> \<file\> \<outputfile\> (default output is '/generatedchart/lines.svg')

Supported options:
  * vmg30 - for vmg30 data
  * cybh - for cyberhand data
  * imu - for imu's data

Example usage: python visualize_data3.py cybh data_example/cyberglobe/Ensayo_2_CGL_Cable.txt /charts/chart1.svg

Example usage2: python visualize_data3.py vmg30 data_example/vmg30/20171103calib_miguel_1/Ensayo_15_VMR_Cable.txt

Example usage3: python visualize_data3.py imu data_example/imu/Ensayo_1_IMU.txt /ch/IMU_DATA_GRAPH.svg
