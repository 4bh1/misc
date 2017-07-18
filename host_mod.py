 #! /usr/bin/env python
 import os  
 def main():  
   #change the current directory to the host file directory  
   os.chdir("C:\Windows\System32\drivers\etc")  
   #opening the host file  
   fi = open("hosts","a")  
   #changing the dns information  
   fi.write('\n127.0.0.1 \t www.google.com')  
   #flushdns cache on the system  
   os.system('ipconfig /flushdns')  
   #closeing the file  
   fi.close()  
 if __name__=='__main__':  
   main()  
