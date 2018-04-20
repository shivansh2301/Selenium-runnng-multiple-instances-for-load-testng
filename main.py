import sys
import os
import subprocess

print ("python script to generate traffic on website for load testing")
filee=open("filename.txt","r")						#username and password are same, stored in this file
i=0
#print filee.read()
for line in filee:
	print ('for Reg No '+line+' :::::: running an instance\n')
	#os.system("python runner.py "+line+"&")
	#os.spawnl(os.P_NOWAIT, 'python runner.py',line)	
	

	subprocess.Popen(["python runner.py "+line],shell=True)		#run concurrent subprocesses
	i=i+1
print("\nTotal "+str(i)+" users have been logged on the website")

filee.close()
