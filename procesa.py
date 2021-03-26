from ftplib import FTP
import sys, os, os.path, operator

def upload(handle,filename):
	f = open(filename,"rb")
	(base,ext) = os.path.splitext(filename)
	picext = ".bmp .jpg .jpeg .dib .tif .tiff .gif .png"
	if(operator.contains(picext,ext)):
		try:
			handle.storbinary("STOR " + filename,f,1)
		except Exception:
			print "Successful upload."
		else:
			print "Successful upload."
		f.close()
		return

	try:
		handle.storbinary("STOR " + filename,f)
	except Exception:
		print "Successful upload."
	else:
		print "Successful upload."
	f.close()
	return


def download(handle,filename,prefix):
	rtn=0
	if os.path.exists(prefix+filename):
		pass
	else:
		f2 = open(prefix+filename,"wb")
		try:
			handle.retrbinary("RETR " + filename,f2.write)
		except Exception:
			print "Error in downloading the remote file.",filename
			rtn = 1
		else:
			print "Successful downloaded!",filename
			rtn = 0
		f2.close()
	return rtn

host_name = "dmmotion.upload.akamai.com"
if "http://" in host_name:
	host_name = host_name.replace("http://","")
host_name = host_name.replace("\n","")
user = "eluniadmtv"
pwd = "uni512ve"

try: ftph = FTP(host_name)
except:
	print "Host could not be resolved."
	raw_input()
	sys.exit()
else: pass
try:
	ftph.login(user,pwd)
except Exception:
	if user == "anonymous" or user == "Anonymous" and pwd == "anonymous" or pwd == "Anonymous":
		print "The server does not accept anonymous requests."
		raw_input()
		sys.exit()
	else:
		print "Invalid login combination."
		raw_input()
		sys.exit()
else:
	print "Successfully connected!\n"

print ftph.getwelcome()
flag = 1
count = 0
path = ftph.pwd()
mydirs=("mp3/","flv/")
cnt=0
for i in mydirs:
	ftph.cwd(i)
	path = ftph.pwd()
	print "Moviendose a directorio",path
	#_eldir=ftph.dir()
	filelist= ftph.nlst()
	for fl in filelist:
		download(ftph,fl,i)
		cnt+=1
	ftph.cwd("/")
