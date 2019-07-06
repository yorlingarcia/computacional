class Distribucion:
	
	cont = 0
	med = 0
	def ini(self):
		print("hola")
		
		
	def Er(self,x, punt):
		
		aux =punt[0]
		self.contcont = 0
		for i in range(len(punt)):
		    if aux < punt[i]:
		        aux = punt[i]
		        self.cont = i
		Er = aux
		Erx = x[self.cont]
		self.med = Er/2
		return([Er,Erx,self.med])
		
	def gamma(self,x,punt):
		aux1 = 0
		aux2 = 0
		gamma = 0
		for i in range(len(punt)//2):
		    if punt[self.cont-i] < self.med:
		        aux1 = self.cont-i
		        break
		for i in range(len(punt)//2):
		    if punt[self.cont+i] < self.med:
		        aux2 = self.cont+i
		        break
		gamma = x[aux2-1]-x[aux1+1]
		
		gamma_x1 = x[aux1+1]
		gamma_x2 = x[aux2-1]
		gamma_y1 = punt[aux1+1]
		gamma_y2 = punt[aux2-1]
		return([gamma,gamma_x1,gamma_x2,gamma_y1,gamma_y2])