# -*- coding: utf-8 -*-

import empro.toolkit.sipi as sipi

def main():
	momentum_dir=r"C:\Program Files\Keysight\ADS2020_update2\Momentum\2020.20"
	try:
		sipi.setMomentumDir(momentum_dir)
	except:
		pass
	path=r"E:/Github/youtube-return-current-stitching-via/ReturnCurrentStitchingVIAs_wrk"
	lib=r"PCB11_lib"
	subst=r"PCB011_lib/PCB01.subst"
	substlib=r"PCB011_lib"
	substname=r"PCB01"
	ltdSubst=r"simulation/PCB11_lib/%P%C%B11/sipi%Setup/proj.ltd"
	cell=r"PCB11"
	layout=r"layout"
	sipiSetup=r"sipiSetup"
	libS3D=r"simulation/PCB11_lib/%P%C%B11/sipi%Setup/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"C:\Program Files\Keysight\ADS2020_update2"

	sipi.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, ltd_subst=ltdSubst, cell=cell, layout_view=layout, sipi_view=sipiSetup, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
