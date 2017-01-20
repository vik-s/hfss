# ----------------------------------------------
oDesktop.RestoreWindow()
projects = oDesktop.GetProjects()
for oProject in projects:
	projectName=oProject.GetName()
	designlist = oProject.GetTopDesignList()
	projectPath=oProject.GetPath()
	for design in designlist:
		oDesign = oProject.SetActiveDesign(design)
		Design_Type = oDesign.GetDesignType()
		if (Design_Type == 'HFSS'):		
			oModuleSetup = oDesign.GetModule("AnalysisSetup")
			setups = oModuleSetup.GetSetups()
			oModuleBoundary = oDesign.GetModule("BoundarySetup")
			excitations = oModuleBoundary.GetNumExcitations()
			oModuleSolve = oDesign.GetModule("Solutions")
			
			for s in setups:
				sweeps = oModuleSetup.GetSweeps(s)
				if len(sweeps)==0:
					pass
								
				else:
					for sweep in sweeps:
						variation_array = oModuleSolve.ListVariations(s+":"+sweep) 

						if len(variation_array)==1:
							oModuleSolve.ExportNetworkData(variation_array[0], [s+":"+sweep], 3, projectPath + "/" + projectName + "_" + design +"_"+s+ ".s" +str(excitations) + "p", ["All"], True, 50, "S", -1, 0, 15)

						else:
							for variation in variation_array:
								oModuleSolve.ExportNetworkData(variation, [s+":"+sweep], 3, projectPath + "/" + projectName + "_" + design +"_"+s+"_"+sweep+"_"+variation.replace("='","_").replace("' ","_").replace("'","").replace(".","R")+ ".s" +str(excitations) + "p", ["All"], True, 50, "S", -1, 0, 15)
							
							
