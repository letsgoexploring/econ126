import runProcs,os

pwd=os.getcwd()

for f in os.listdir(pwd):
	if f.startswith('Slides') and f.endswith('tex'):
		runProcs.handout(f)

for f in os.listdir(pwd):
	if (f.startswith('Slides') or f.startswith('Handout')) and f.endswith('tex'):
		runProcs.tex(f)