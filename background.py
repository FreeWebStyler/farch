from pprint import pprint

import base64
import os
import re
import subprocess
import time
from pathlib import Path

class Background:

    dev = None

    @staticmethod
    def pktar(fp, pfp):
        print(fp)
        print(pfp)
        print(os.path.basename(fp))
        up = Path(fp).parent
        print(up)
        if os.path.isfile(fp):
            dir = os.path.dirname(fp)
            #print(dir)
            #return
            #out = subprocess.run(['tar', '-c', '-v', '-f', pfp, '--add-file', fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            #out = subprocess.run(['tar', '-c', '-v', '-f', pfp, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            #out = subprocess.run(['tar', '-c', '-v', '-f', pfp, '-C', dir, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            out = subprocess.run(['tar', '-c', '-f', pfp, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
        else:
            #out = subprocess.run(['tar', '-c', '-v', '-f', pfp, '-C', fp, '.'], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            #out = subprocess.run(['tar', '-c', '-v', '-f', '--strip-components=2', pfp, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            #out = subprocess.run(['tar', '-c', '-v', '-f', pfp, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            out = subprocess.run(['tar', '-C', up, '-c', '-f', pfp, os.path.basename(fp)], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
            #cmd = "cd "+ fp +' && tar -cf '+ pfp +' .'
            
            '''cmd = "cd "+ fp +' && tar -cf '+ pfp +' '+ os.path.basename(fp)
            print(cmd)
            #return
            pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            fbuf = pipe.stdout
            for line in fbuf.readlines():
                lines = line.decode().split("\n") #            
                print(lines)'''
        out = out.stdout.decode("utf-8") 
        out = out.split("\n")
        print(out)
        return

    @staticmethod
    def pkzip(fp, pfp): # file path , packed file path
        print(fp)
        print(pfp)
        up = Path(fp).parent
        print(up)
        #print(type(up))
        #out = subprocess.run(['zip', '-0', '-j', '-q', '-r', pfp, fp], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
        
        '''out = subprocess.run(['zip', '-0', '-r', pfp, fp +'/*'], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
        out = out.stdout.decode("utf-8") 
        #out = out.split(display_name)
        #out = out.split("\n")
        out = out.split("\n")
        print(out)'''

        cmd = 'cd "'+ str(up) +'" && zip -0 -r "'+ pfp +'" "'+ os.path.basename(fp) +'"'
        #print(type(cmd))
        print(cmd)
        #return
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        fbuf = pipe.stdout
        for line in fbuf.readlines():
            lines = line.decode().split("\n") #            
            print(lines)
        return