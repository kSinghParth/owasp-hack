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

def find_all(file_name, path=None):
    if path is None:
        name = platform.system()
        if name=="Linux":
            path = "/home/"
        elif name=="Darwin":
            path="/Users"
        elif name=="Windows":
            path="C:"
    result = []
    for root, dirs, files in os.walk(path):
        if file_name in files:
            result.append(os.path.join(root, file_name))
    return result

def search(package):
    cmd = "pip search "+ package
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	exitcode=p.returncode
	if exitcode==0:
		return "Successfully Installed \n"+str(output,"utf-8")
	if exitcode==100:
		cmd="sudo -S "+cmd
		password=input("Enter Password:\n")
		p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
		output,error=p.communicate(input=password)
		exitcode=p.returncode
		if exitcode==0:
			out, err = p.communicate()
    		l = str(out, 'utf-8').split("\n")
	return "Error while downloading: \n"+str(error,"utf-8")+"\n\nError Code:"+str(exitcode)

def whl_install(package):
    path = find_all(package)
    for file in path:
        cmd = "pip install "+file
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		exitcode=p.returncode
		if exitcode==0:
			return "Successfully Installed \n"+str(output,"utf-8")
		if exitcode==100:
			cmd="sudo -S "+cmd
			password=input("Enter Password:\n")
			p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
			output,error=p.communicate(input=password)
			exitcode=p.returncode
			if exitcode==0:
				return "Successfully Installed \n"+str(output,"utf-8")
	return "Error while downloading: \n"+str(error,"utf-8")+"\n\nError Code:"+str(exitcode)
