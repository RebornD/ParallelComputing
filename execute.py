import subprocess;
import multiprocessing as mp;


def function(name):
	subprocess.call(name);

def multi(list):
	p = mp.Pool(mp.cpu_count());
	p.map(function,list);
	p.close();

if __name__ == "__main__":

	OBJECTIVES = [2,3,4,5,6,8,10];
	POPULATIONSIZES = [100,105,120,126,126,120,220];
	PROBLEMS = ["DTLZ1","DTLZ2","DTLZ3","DTLZ4"];
	list = [];



	for obj,popsize in zip(OBJECTIVES,POPULATIONSIZES):
		for problem in PROBLEMS:
			###################################### you should modify following codes if you use this program##########################################
			#list.append(["NSGAII.exe","-Problem" ,problem,"-populationSize", str(popsize),"-Objectives",str(obj)]); 								#
			##########################################################################################################################################
			
		
	multi(list);
	