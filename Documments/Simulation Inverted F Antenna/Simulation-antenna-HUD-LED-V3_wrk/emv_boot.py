# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/DELL/Documents/GitHub/Altium-cp1/HW_HUBV3_V1/Documments/Simulation Inverted F Antenna/Simulation-antenna-HUD-LED-V3_wrk"
	lib=r"Simulation-antenna-HUD-LED-V3_lib"
	subst=r"Simulation-antenna-HUD-LED-V3_lib/Stackup.subst"
	substlib=r"Simulation-antenna-HUD-LED-V3_lib"
	substname=r"Stackup"
	cell=r"Antenna"
	view=r"layout"
	libS3D=r"simulation/Simulation-antenna-HUD-LED-V3_lib/%Antenna/_3%D%Viewer/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
