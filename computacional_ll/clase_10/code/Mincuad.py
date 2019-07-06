# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:15:09 2019

@author: Yorlin García
"""

#import numpy
class Minimoscuadrados:
	
	def min(self,D):
		
		#D = numpy.array(D)
		#print(type(D))
		sigma = (abs(D[:,1]))**0.5
		d = 0.
		dx = 0.
		dxx = 0.
		dxy = 0.
		dy =0.
		delta = 0.
		for i in range(len(D[:,0])):
		    d += 1/sigma[i]**2
		    dx += D[i,0]/sigma[i]**2
		    dxx += (D[i,0]/sigma[i])**2
		    dxy += D[i,0]*D[i,1]/sigma[i]**2
		    dy += D[i,1]/sigma[i]**2
		
		delta = d*dxx - dx**2
		
		a1 = (dxx*dy - dx*dxy)/delta
		a2 = (d*dxy -dx*dy)/delta
		return([a1,a2,sigma])