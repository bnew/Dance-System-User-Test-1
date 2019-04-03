#duplicator script
merge = op('merge1')
i = op('in1')

def changeAmount(amt):
	ins = len(merge.inputConnectors)
	diff = amt - ins + 1
	
	for n in range(abs(diff)):
		if diff < 0:
		#decreasing connections
			merge.inputConnectors[0].disconnect()
		
		else:
		#increasing connections
			i.outputConnectors[0].connect(merge)
			

def onValueChange(par, prev):
	changeAmount(int(par.val))
	return
		