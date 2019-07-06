# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:38:58 2019

@author: Yorlin García
"""
import numpy as np
from scipy import linspace

class EulerSegundo:
	
	def normal(self,Vo,Xo,tmin,tmax,Deltat,fun):
		N = (tmax - tmin)/Deltat
		t = linspace(tmin,tmax,int(N))
		
		v = np.zeros(len(t))
		x = np.zeros(len(t))
		x[0] = Xo
		v[0] = Vo
		for i in range(len(t)-1):
			a = x[i]
			acel = float(eval(fun))
			v[i+1] = v[i] + Deltat*acel
			x[i+1] = x[i] + Deltat*v[i]
		return(t,x)
		
	def mejorado(self,Vo,Xo,tmin,tmax,Deltat,fun):
		N = (tmax - tmin)/Deltat
		t = linspace(tmin,tmax,int(N))
		
		v = np.zeros(len(t))
		x = np.zeros(len(t))
		u = np.zeros(len(t))
		u[0] = Vo
		x[0] = Xo
		v[0] = Vo
		
		for i in range(len(t)-1):
			a = x[i]
			acel1 = float(eval(fun))			
			v[i+1] = v[i] + Deltat*acel1
			u[i+1] = v[i] + Deltat*acel1
			x[i+1] = x[i] + Deltat*(0.5)*(v[i]+u[i+1])
		return(t,x)
		
		
		