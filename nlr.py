 #! /usr/bin/env python  
 fi = raw_input('''  
 __     ___                
 \ \ _ _  | _ \___ _ __ _____ _____ _ _   
  \ \| ' \ |  / -_) ' \/ _ \ V / -_) '_|  
  \_\_||_| |_|_\___|_|_|_\___/\_/\___|_| v0.1  
                   \n\nEnter the name or path of the file,to remove extra ENTER's. \n\n>>''')  
 try :  
      te = open(fi,'r+w')  
 except :  
      print 'File does no exist'  
 fin=[]
 te1 = te.readlines()  
 te.seek(0,0)  
 te.truncate()  
 for x in te1:  
      if x != '\n':  
           fin.append(x)  
 te.write(''.join(fin))  
 te.close()  
