#!/usr/bin/python
__author__		= "Sander Granneman"
__copyright__	= "Copyright 2020"
__version__		= "0.2.0"
__credits__		= ["Sander Granneman"]
__email__		= "sgrannem@staffmail.ed.ac.uk"
__status__		= "beta"

import sys
import re
from collections import defaultdict

class ParseGenbank():
	""" class to parse .gb GenBank files and to extract information """
	def __init__(self,datafile):
		self.datafile = open(datafile,"r")
		self.genbankdict = defaultdict(lambda: defaultdict(str))
		self.acceptedfeats = ["CDS","mRNA","ncRNA","sRNA","rRNA","tRNA","gene"]
		self.__chromosomeseq = defaultdict(str)
		self.__readDataFile()

	@staticmethod
	def reverseComplement(sequence):
		""" Returns the reverse complement of a DNA string """
		basecomplement = str()
		complement = {"A":"T","G":"C","C":"G","T":"A","a":"t","c":"g","g":"c","t":"a"}
		letters	 = list(sequence)
		for letter in letters:
			if letter in complement:
				basecomplement += complement[letter]
			else:
				basecomplement += letter
		return basecomplement[::-1]

	@staticmethod
	def featstringToDict(featsarray):
		string = "".join(featsarray)
		string = string.replace("\"","")
		a = list(filter(None,re.split("[#=]",string)))
		i = iter(a)
		b = dict(zip(i,i))
		return b

	@staticmethod
	def processGenBankCoordinates(string):
		""" The string could contain:
		123..456
		complement(123..456)
		complement(<123..456)
		complement(123..456>)

		Not entirely sure how to deal with the incomplete record (i.e. with chevrons)
		"""
		strand = "+"
		if re.search("complement",string):
			strand = "-"
		### first thing to do is to split the string based on spaces.
		feature,coordinates = list(filter(None,string.strip().split()))
		Fld = list(filter(None,re.split("[.,<>()A-Za-z]+?",coordinates)))
		allcoordinates = [int(i) for i in Fld]
		start = min(allcoordinates)
		end = max(allcoordinates)
		return (feature,strand,start,end)

	@staticmethod
	def getChromosomeInfo(string):
		feature,coordinates = list(filter(None,string.strip().split()))
		Fld = list(filter(None,re.split('[():]+?',coordinates)))
		allcoordinates = [int(i) for i in Fld[-1].split("..")]
		chromosome = Fld[1]
		start = min(allcoordinates)
		end = max(allcoordinates)
		return (chromosome,start,end)

	@staticmethod
	def stripNumbersAndSpaces(string):
		""" removes any numbers and spaces in a DNA sequence string """
		string = string.strip().replace(" ","")	 # removing spaces
		string = ''.join([i for i in string if not i.isdigit()]) # removing numbers
		return string

	def proteinSeqToFasta(self,outfile=None):
		""" Prints all the protein sequences to a fasta file """
		writeto = sys.stdout
		if outfile:
			writeto = open(outfile,"w")
		for gene in sorted(self.genbankdict):
			translation = self.genbankdict[gene]["translation"]
			if translation:
				writeto.write(">%s\n%s\n" % (gene,translation))

	def geneSeqToFasta(self,gene,ranges=0,outfile=None):
		""" Prints all the gene sequences to a fasta file """
		writeto = sys.stdout
		if outfile:
			writeto = open(outfile,"w")
		for gene in sorted(self.genbankdict):
			sequence = self.getGeneSequence(gene,ranges=ranges)
			if sequence:
				writeto.write(">%s\n%s\n" % (gene,sequence))

	def getGeneSequence(self,gene,ranges=0):
		""" Returns the nucleotide sequence for that gene """
		start,end = self.genbankdict[gene]["coordinates"]
		chromosome = self.genbankdict[gene]["chromosome"]
		strand = self.genbankdict[gene]["strand"]
		start -= 1 # coordinates are 1-based!!:
		if ranges:
			start -= ranges
			end   += ranges
		dnaseq = self.__chromosomeseq[chromosome][start:end]
		if strand == "-":
			dnaseq =  self.reverseComplement(dnaseq)
		return dnaseq

	def getProteinSequence(self,gene):
		""" Returns the protein sequence for that gene """
		return self.genbankdict[gene]["translation"]

	def getGeneAnnotation(self,gene):
		""" Returns the annotation for that gene """
		return self.genbankdict[gene]["annotation"]

	def getGeneProduct(self,gene):
		""" Returns the protein info for that gene """
		return self.genbankdict[gene]["product"]

	def getGeneChromosomeCoordinates(self,gene):
		""" Returns the chromosome coordinates for that gene """
		return self.genbankdict[gene]["coordinates"]

	def getGeneChromosomeName(self,gene):
		""" Returns the chromosome name for that gene """
		return self.genbankdict[gene]["chromosome"]

	def getGeneStrand(self,gene):
		""" Returns the strand for that gene """
		return self.genbankdict[gene]["strand"]

	def getGeneOldLocusTag(self,gene):
		""" Returns the old locus tag for that gene """
		return self.genbankdict[gene]["old_locus_tag"]

	def getGeneProteinID(self,gene):
		""" Returns the protein id for that gene """
		return self.genbankdict[gene]["protein_id"]

	def getChromosomeSequence(self,chromosome):
		""" Returns the nucleotide sequence for that chromosome """
		return self.__chromosomeseq[chromosome]

	def getChromosomeNames(self):
		""" Returns all the chromosome names found in the genbank file """
		return sorted(self.__chromosomeseq.keys())

	def geneNames(self):
		""" Returns all the locus_tags indentified in the genbank file """
		return sorted(self.genbankdict.keys())

	def __collectChromosomeSequence(self,chromosome):
		""" Loop to grab the chromosome sequence """
		while True:
			line = next(self.datafile)
			if line.startswith("ORIGIN"):
				continue
			elif re.search("[a,t,c,g,n]",line,re.I):
				self.__chromosomeseq[chromosome] += self.stripNumbersAndSpaces(line)
			elif line.startswith("//"):
				break

	def __readDataFile(self):
		""" Parses the genbank datafile """
		featstring = str()
		feature = str()
		strand = str()
		start = int()
		end = int()
		coordinates = list()
		datadict = defaultdict(list)
		while True:
			try:
				line = next(self.datafile)
				linespace = len(line.rstrip()) - len(line.strip())
				newline = line.strip()
				if newline.startswith("/"):
					newline = list(newline)
					newline[0] = "#"
					newline = "".join(newline)
				if "misc_feature" in newline:
					continue
				elif linespace == 5 and not newline[0].isdigit():
					feature,strand,start,end = self.processGenBankCoordinates(newline)
					coordinates.append((feature,strand,start,end))
				elif linespace == 21:
					datadict[(feature,strand,start,end)].append(newline)
				elif line.startswith("CONTIG"):
					chromosome,start,end = self.getChromosomeInfo(newline)
					for i in coordinates:
						datadict[i].append("#chromosome=\"%s\"" % chromosome)
					coordinates = list()  # resetting the list for the next gene
					self.__collectChromosomeSequence(chromosome) # collecting the chromosome DNA sequences

			except StopIteration:
				break
		for key in datadict:
			feature,strand,start,end = key
			featsdict = self.featstringToDict(datadict[key])
			if feature in self.acceptedfeats:
				try:
					gene_name = featsdict["locus_tag"]
				except:
					gene_name = featsdict["label"]
				self.genbankdict[gene_name]["strand"] = strand
				self.genbankdict[gene_name]["exons"]
				self.genbankdict[gene_name]["coordinates"] = (start,end)
				self.genbankdict[gene_name]["annotation"] = feature
				for i in featsdict:
					self.genbankdict[gene_name][i] = featsdict[i]
