class trackController:
	"""
	trackController description:
	controls one voice in ableton

	in[0] - dance amount
	in[1] - isPresent
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		#create a custom menu for controlling this TrackController,
		#will error if parameters already exist
		# try:
		# 	self.MakeMenu()
		# except:
		# 	print("already have params")
		
		#does this launch clips?
		self.ClipLauncher = self.ownerComp.par.Clipcontroller
		#does this control racks?
		self.RackController = self.ownerComp.par.Rackcontroller

		#td ableton track object for volume and clips
		self.Track = op('abletonTrack1')
		
		#clip launcher, initalize it as off
		self.clipControl = op('abletonClipSelector')
		self.clipControl.allowCooking = self.ClipLauncher

		#rack component for macro control, initalize it as off
		self.rack = op('abletonRack1')
		self.rack.allowCooking = self.RackController
		#number of macros
		self.MacroCount = 2
		#store the track id that will be controlled
		self.TrackNumber = 0

		#set the default min/max volumes
		self.minVol = .1
		self.maxVol = .85




	def InitRack(self):
		'''
		select the appropriate rack device in ableton
		assumes that its the first device in the chain
		is called every time the TrackID parameter is changed
		'''
		self.rack.par.Device = 1
		self.rack.par.Chain1 = 0
		return
	
	def MakeMenu(self):
		'''
		create custom properties on the comp for controlling the track
		errors if the properties exist already
		is there a better way to define all these?
		'''
		o = self.ownerComp
		
		#add page for custom parameters
		p = o.appendCustomPage("Track Options")

		#make par for which track to control
		m = p.appendMenu("Track",replace=False)[0] 
		#set its menu labels to match the ableton track's labels
		m.menuSource = "op('./abletonTrack1').par.Track"


		#add value for number of macros
		c = p.appendInt("Macrocount",replace=False)[0] #[0] cuz it returns a tuple
		#set the range of the custom par 'macrocount'
		c.normMin = 0
		c.normMax = 8
		
		#add value for presence volumes
		v = p.appendFloat("Maxvol",replace=False)[0];
		v.normVal = self.maxVol
		v = p.appendFloat("Minvol",replace=False)[0];
		v.normVal = self.minVol
		
		#add toggles to enable/disable clip launcher or rack controller
		p.appendToggle("Rackcontroller",replace=False)
		p.appendToggle("Clipcontroller",replace=False)

	def toggleComp(self,comp):
		'''
		turns a component on or off
		returns its latest state
		'''
		c = not (comp.allowCooking)
		comp.allowCooking = c
		print(c)
		return c

	def ToggleRackControl(self):
		'''
		toggles rack component
		'''
		self.RackController  = self.toggleComp(self.rack)

	def ToggleClipControl(self):
		'''
		toggles clip component
		'''
		self.ClipLauncher = self.toggleComp(self.clipControl)

