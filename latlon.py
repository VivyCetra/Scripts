#! /usr/bin/env python

InfileName = 'Marrus_claudanielis.txt'

InFile = open( InfileName, 'r' )

LineNumber = 0

for Line in InFile:
	Line = Line.strip()
	
	if LineNumber > 0:
		ElementList = Line.split( '\t' )
		print('Depth:{} Lat:{} Lon:{}' .format( ElementList[4], ElementList[2],ElementList[3] ) )

	LineNumber = LineNumber + 1

InFile.close()
