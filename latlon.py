#! /usr/bin/env python
import re

def decimalat( DegreeString ):
	# Converts a string for a latitude or a longitude into a float
	SearchString = '(\d+) ([\d\.]+) (\w)'
	Result = re.search( SearchString, DegreeString )
		
	Degree = float( Result.group( 1 ) )
	Minute = float( Result.group( 2 ) )
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute / 60
	 
	if Compass in 'SW':
		DecimalDegree = - DecimalDegree
	
	return DecimalDegree

assert( decimalat('36 30.0 N') == 36.5 )
assert( decimalat('36 30.0 S') == -36.5 )
assert( decimalat('36 30.0 W') == -36.5 )



InfileName = 'Marrus_claudanielis.txt'

InFile = open( InfileName, 'r' )

LineNumber = 0

for Line in InFile:
	Line = Line.strip()
	
	if LineNumber > 0:
		ElementList = Line.split( '\t' )
		print('Depth:{} Lat:{} Lon:{}' .format( ElementList[4], ElementList[2],ElementList[3] ) )

		latitude = decimalat( ElementList[ 2 ] )

		print ( latitude )

	LineNumber = LineNumber + 1

InFile.close()