import subprocess 

def install_pip(host):
	cmd="pip install "+host
	proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	output,error=proc.communicate()
	exitcode=proc.returncode
	if exitcode==0:
		return "Successfully Installed \n"+str(output,"utf-8")
	if exitcode==100:
		cmd="sudo -S "+cmd
		password=input("Enter Password:\n")
		proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		output,error=proc.communicate(input=password)
		exitcode=proc.returncode
		if exitcode==0:
			return "Successfully Installed \n"+str(output,"utf-8")
	return "Error while downloading: \n"+str(error,"utf-8")+"\n\nError Code:"+str(exitcode)



def install_ei(host):
	cmd="easy_install "+host
	proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	output,error=proc.communicate()
	exitcode=proc.returncode
	if exitcode==0:
		return "Successfully Installed \n"+str(output,"utf-8")
	if exitcode==100:
		cmd="sudo -S "+cmd
		password=input("Enter Password:\n")
		proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		output,error=proc.communicate(input=password)
		exitcode=proc.returncode
		if exitcode==0:
			return "Successfully Installed \n"+str(output,"utf-8")
	return "Error while downloading: \n"+str(error,"utf-8")+"\n\nError Code:"+str(exitcode)

print (install_ei("bs4"))
