#! /usr/bin/env python
#Author: Amir S 

from helper.easierlife import *
import json
import fileinput

BlockSize=3
FID_IN=128
FID_OUT=192
STRIDE=2
PADDING=0
for row in fileinput.input():
	obj = json.loads(row)
	image_id = obj["image_id"]
	ws = obj ["ws"]
	ls = obj ["ls"]
	layer=obj["layer"]
	
	n_row=ws[0]
	n_col=ls[0]
	values=[]
	for i in range(0,n_row-BlockSize+1,STRIDE):
		for j in range(0,n_col-BlockSize+1,STRIDE):
			values.append(None)		
	for f in range(0,FID_OUT):
		print json.dumps({
			"image_id":image_id,
			"fid":f,
			"num_rows":(n_row-BlockSize)/STRIDE+1,
			"num_cols":(n_col-BlockSize)/STRIDE+1,
			"values":values,
			"layer":layer
			})


				
					