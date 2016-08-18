#!/usr/bin/env python

#########################################################################
#
#	This Program has definitions to calculate the fourier transform and noise floor
#	of a set of data from a given file.

#	Copyright (C) 2016 Aman Abhishek Tiwari, Indian Institute of Technology, Kanpur
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################## 

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.signal import argrelextrema

#########################################################################

def greater (arr, comp):
	result = []
	for idx in range (len (arr)):
		if arr[idx] > comp:
			result [idx] = arr[idx]
	return result

#########################################################################
#########################################################################

def noise_floor_distribution (data_points) :
	y_range = 1000
	x_range = 100
	interval = len (data_points) / x_range
	result = np.zeros ((x_range,y_range))
	for i in range (x_range):
		data = np.array (\
			data_points [int (i * interval) : int ((i + 1) * interval)])
		ymin = min (data)
		ymax = max (data)
		y_interval = (ymax - ymin) / y_range
		for j in range (y_range) :
			total_p = len (data)
			result [i][j] = (data > (j * y_interval)).sum() * 100 / total_p
	
	#for row in result:
		#for elt in row:
			#print (elt)
	
	plt.figure (2)
	#x = np.array (range(len (result[400])))
	plt.grid()
	for i in range (x_range):
		plt.plot (result[i])
	return

#########################################################################
#########################################################################

def noise_floor (data_points) :
	plt.figure (1)
	y_range = 1000
	x_range = 1000
	interval = len (data_points) / x_range
	#result = np.zeros ((x_range,y_range))
	results = []
	for i in range (x_range):
		data = data_points [int (i * interval) : int ((i + 1) * interval)]
		#print (type (data))
		ymin = min (data)[0]
		ymax = max (data)[0]
		y_interval = (ymax - ymin) / y_range
		total_points = len (data)
		print (i)
		for j in range (y_range) :
			#result [i][j] = (data > (j * y_interval)).sum() * 100 / total_points
			tmp = ()
			total = 0
			for elt in data:
				total += elt[0] >= (j * y_interval)
				
			
			y_tmp = j * y_interval
			if total * 100 / total_points <20:
				for elt in data:
					if elt[0] >= y_tmp:
						results.append (elt)
				break
				#print ("within if ", results)
	
	
	#for row in result:
		#for elt in row:
			#print (elt)
	
	#x = np.array (range(len (result[400])))
	
	x = []
	y = []
	#outfile = open (sys.argv[3], 'w')
	for elt in results:
		x.append (elt[1])
		y.append (elt[0])
		#outfile.write (str (elt[1]) + "," + str (elt[0]) + "\n")

	#print (results)
	plt.grid()
	plt.subplot (312)
	plt.plot (x, y, ".")
	return

#########################################################################

def fourier_transform (datafile, freq):
	infile = open (datafile, 'r')
	freq = float (freq)

	y = []
	for line in infile:
		y.append (float (line))

	y = np.array (y)

	y_out = np.fft.fft (y)
	y_out_log = 20 * np.log10 (np.absolute (y_out) / 8191)
	#y_out_log = np.absolute (y_out)
	#y_out_log = 20 * np.absolute (y_out) / 8191
	plt.figure (1)
	x = np.array (range(len (y))) / float (freq)
	final = []
	
	###############################
	plt.subplot (311)
	plt.grid()
	plt.plot (x, y)
	###############################
	plt.subplot (312)
	#plt.grid()
	x_out = np.fft.fftfreq (len (x), d = 1 / freq)
	
	for idx in range (int (len (x) / 2)):
		final.append (([y_out_log[idx], x_out[idx]]))
	plt.plot (x_out[1:len (x_out)/2], y_out_log[1:len (x_out)/2], ".")
	#print (min (final)[0])
	#print (type (final))
	###############################

	n = 1.0
	fc = 5e6
	H = 1 / (1 + (x_out/ fc)**(2 * n))

	yflt = np.real (np.fft.ifft (H * y_out))
	plt.subplot (313)
	plt.plot (x, y)
	plt.plot (x, yflt)
	print (max (yflt));
	print (min (yflt));
	noise_floor_distribution (y_out_log[:len (x_out)/2])
	noise_floor (final)
	plt.grid()
	plt.show()
	return

if __name__ == '__main__':
    fourier_transform()
#########################################################################
