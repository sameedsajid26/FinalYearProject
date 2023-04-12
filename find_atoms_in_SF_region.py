# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:52:47 2023

@author: ZHANG Jun
@editor: Sameed SAJID
"""

import numpy as np
number_of_atomic_planes = 18 # along z direction
scaled_positions_of_SF = 0.5
spacing = 1 / (number_of_atomic_planes - 1)

for i in range(1,501):
    #print (i)

    # variables
    file_name = f'/Users/sameedsajid/opt/anaconda3/pkgs/lammps-2022.06.23-py310h33d413e_mpich_0/bin/25JAN/testing/dump.{i}relax.1.0'
    # read file
    with open(file_name, 'r') as f:
        # data1 = np.loadtxt(f, dtype=str)
        
        item1 = f.readline() # reads the first line
        time_step = float(f.readline())
        #print(time_step)
        item2 = f.readline()
        number_of_atoms = int(f.readline())
        #print(number_of_atoms)
        item3 = f.readline()
        cell_vector1 = [float(x) for x in f.readline().split()]
        cell_vector2 = [float(x) for x in f.readline().split()]
        cell_vector3 = [float(x) for x in f.readline().split()]

        #print(cell_vector1, cell_vector2, cell_vector3)
        item4 = f.readline()
        data = np.loadtxt(f, dtype=str)
        # print(data)

    # get coordinates
    positions = np.array(data[:,2:5], dtype=float)

    # calculate the layer spacing, in the scaled unit.
    #spacing = 1 / (number_of_atomic_planes - 1)

    # find atoms in the SF region
    atom_index = np.where((positions[:,2] > scaled_positions_of_SF - spacing) & (positions[:,2] < scaled_positions_of_SF + spacing))[0]
    #print(atom_index)

    # export the information of atoms in the SF region.
    results = data[atom_index]
    # print(results.shape)

    #keep only the atom_type column
    result2 = results[:,1]
    #print(result2.shape)
    result2 = result2.reshape((-1, 1)) # 
    result2 = result2.T
    # print(result2)

    if (i==1):
        global_results = result2
    else:
        global_results = np.vstack((global_results, result2))
    # save the results to a file
print(global_results.shape)    
np.savetxt('/Users/sameedsajid/opt/anaconda3/pkgs/lammps-2022.06.23-py310h33d413e_mpich_0/bin/25JAN/testing/new_x_data.txt', global_results, fmt='%s')
