# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:03:49 2019

@author: Yorlin García
"""
import numpy as np
from scipy import linspace

class Euler:
	
	def ini(self):
		print("inicio")
		
		
	def normal(self,xo,yo,Xmin,Xmax,h,fun):
		N = (Xmax -Xmin)/h
		y = np.zeros(int(N))
		y[0] = yo
		x = linspace(Xmin,Xmax,int(N))
		
		for i in range(int(N)-1):
			a = x[i]
			b = y[i]
			Funcion = float(eval(fun))
			y[i+1] = y[i] +h*Funcion
		return(x,y)
			
	def mejorado(self,xo,yo,Xmin,Xmax,h,fun):
		N = (Xmax -Xmin)/h
		y = np.zeros(int(N))
		u = np.zeros(int(N))
		y[0] = yo
		u[0] = yo
		x = linspace(Xmin,Xmax,int(N))
		for i in range(int(N)-1):
			a = x[i]
			b = y[i]
			Funcion1 = float(eval(fun))
			u[i+1] = y[i]+h*Funcion1
			a = x[i+1]
			b = u[i+1]
			Funcion2 = float(eval(fun))
			y[i+1] = y[i]+h*(0.5)*(Funcion1 + Funcion2)
		return(x,y)