import os 

def listFile(p):
       #print(p)
       if(os.path.isdir(p)):
              dirs = os.listdir(p)
              for x in dirs:
                  if(os.path.isfile(x)):
                     makeFile(x)
                  else:
                      listFile(os.path.abspath(p+'\\'+x))
       else:
         makeFile(p)

def makeFile(x):
    arr=os.path.split(x)
    arr2 = arr[1].split('.')
    if(len(arr2)>=2):
           a = arr2[0]
           t = arr2[1]
           #print(t)
           if(t=='jar' or t=='pom'):
               arr2 = arr[0].split('\\');
               lens=len(arr2)
               v = arr2[lens-1]
               arr3 = arr2[3:lens-2]
               g = arr2[2]
               for i in arr3:
                 g = g+'.'+i
               cmd='mvn install:install-file  -Dfile='+x+'  -DgroupId='+g+'  -DartifactId='+a+'  -Dversion='+v+'  -Dpackaging='+t
               print(cmd)
               os.system(cmd)
#maven_install();
listFile(os.getcwd())



