#!/usr/bin/python3

from multiprocessing import Pool
from multiprocessing import cpu_count
from subprocess import call
from os.path import exists
import glob
import sys

#path_output = "/home/ygari/scratch/"
path_output = ""
#path_input = "/home/ygari/rla_input/"
path_input = ""

def simulateCase(case):
	case = case.strip()
	
	# search parameters
	print("Simulating case: '" + case + "'...")
	
	caseId = case.replace("-", "").replace(" ", "")
	outputFile = open(path_output+"logs/simulation-" + caseId + ".out", "a")
	command = [path_output+"scripts/simulate-case.sh", case]
	call(command, stdout=outputFile, stderr=outputFile)
	outputFile.close()
	
	# show progress
	call([path_output+"scripts/show-progress.sh"])
	print("")


def getRunNumber(case):
	index = case.find("-r ") + 3
	return int(case[index: index + 2].strip())


def simulateCases(casesFilename, processes):
	print("\n >>> Simulating cases (" + casesFilename + ")...")
	with open(casesFilename) as casesFile:
		pool = Pool(processes=processes)  # start n worker processes
		cases = [case.strip() for case in casesFile.readlines()]

		# this chunksize permits executing first all the cases with run=1, then run=2, etc...
		#chunksize, remainder = divmod(len(cases) / 10, processes)
		#if remainder > 0:
		#	chunksize = chunksize + 1
		#chunksize = 30
		#print("chinksize: " + str(chunksize))
		#pool.map(simulateCase, cases, chunksize)
		pool.map(simulateCase, cases)


if __name__ == '__main__':
	try:
		PROCESSES = int(sys.argv[1])  # number of workers
		CASES_FILE = sys.argv[2]  # case id
	except:
		PROCESSES = cpu_count()
		CASES_FILE = "cases"
	
	#print("\n >>> Initializing simulations...")
	#call([path_input+"scripts/init-simulations.sh"])

	print("\n >>> Using " + str(PROCESSES) + " workers...")

	#for casesFilename in sorted(glob.glob('cases?.csv')):
	simulateCases(path_input + CASES_FILE, PROCESSES)

	print("DONE")

