#! /usr/bin/env python

# This is a comment

DNASeq = raw_input ( "Enter DNA Sequence:" )

DNASeq = DNASeq.upper()

print ('Sequence ' + DNASeq )

SeqLength = float( len ( DNASeq ) )

print( 'Length is' + str( SeqLength ) )


NumberA = DNASeq.count( 'A' )
NumberT = DNASeq.count( 'T' )
NumberG = DNASeq.count( 'G' )
NumberC = DNASeq.count( 'C' )

print('A: ' + str( NumberA / SeqLength ) )
print('T: ' + str( NumberT / SeqLength ) )
print('G: ' + str( NumberG / SeqLength ) )
print('C: ' + str( NumberC / SeqLength ) )