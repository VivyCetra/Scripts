#! /usr/bin/env python

# DNASeq = raw_input ( "Enter DNA Sequence:" )
DNASeq = 'ATGATTGTACCCTGACCCTGAT'

DNASeq = DNASeq.upper()

print ('Sequence ' + DNASeq )

SeqLength = float ( len ( DNASeq ) )

print( 'Length is' + str ( SeqLength ) )


NumberA = DNASeq.count( 'A' )
NumberT = DNASeq.count( 'T' )
NumberG = DNASeq.count( 'G' )
NumberC = DNASeq.count( 'C' )


print ('A: {:.2f}'.format ( NumberA / SeqLength ) )
print ('T: {:.2f}'.format ( NumberT / SeqLength ) )
print ('G: {:.2f}'.format ( NumberG / SeqLength ) )
print ('C: {:.2f}'.format ( NumberC / SeqLength ) )

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <=14: 
	MeltTemp = ( 4 * TotalStrong) + (2* TotalWeak )
	print( "Using long formula." )
else: 
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print( "Using long formula." )

print ( ' Melting Temp: {}'.format(MeltTemp) )

print('Done')