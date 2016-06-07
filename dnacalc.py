#! /usr/bin/env python

# DNASeq = raw_input ( "Enter DNA Sequence:" )
DNASeq = 'ATGATTGTACCCTGACCCTGAT'

DNASeq = DNASeq.upper()

print ('Sequence ' + DNASeq )

SeqLength = float ( len ( DNASeq ) )


TotalStrong = 0
TotalWeak = 0

Bases = "CGTA"

for Base in Bases:
	Count = DNASeq.count( Base )
	Frequency = Count / SeqLength
	print ( '{}: {:.2f}'.format ( Base, Frequency ) )
	if Base in 'GC' : 
		TotalStrong = TotalStrong + Count
	else:
		TotalWeak = TotalWeak + Count
	

print( 'Length is' + str ( SeqLength ) )


if SeqLength <=14: 
	MeltTemp = ( 4 * TotalStrong) + (2* TotalWeak )
	print( "Using long formula." )
else: 
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print( "Using long formula." )

print ( ' Melting Temp: {}'.format(MeltTemp) )

print('Done')