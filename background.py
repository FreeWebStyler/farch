from pprint import pprint

import base64
import os
import re
import subprocess
import time

class Background:

    dev = None
    model = None
    kdbx_fp = '/home/alex/0Dropbox/My/KDBX/nevi.kdbx'

    @staticmethod
    def pktar():
        out = subprocess.run(['lsblk', '--output', 'KNAME,SIZE,HOTPLUG'], stdout=subprocess.PIPE,  stdin=None, shell=False, input=None) #,LABEL,MODEL
        out = out.stdout.decode("utf-8") 
        #out = out.split(display_name)
        #out = out.split("\n")
        out = out.split("\n")
        #print(out)
        #return
        return dev

    @staticmethod
    def get_model():
        
        dev = Background.dev +''
        dev = re.sub('\d', '', dev)
        dev = '/dev/'+ dev
        cmd_ar = ['lsblk', dev, '--output', 'MODEL']
        #print(' '.join(cmd_ar))
        out = subprocess.run(cmd_ar, stdout=subprocess.PIPE,  stdin=None, shell=False, input=None)
        out = out.stdout.decode("utf-8")

        out = out.split("\n")
        del out[0]
        out = out[0].strip()
        #print(out)
        Background.model = out
        #return out
        #out = out.split("\n")

    @staticmethod
    def mount_usb(sp): #dev, dirn
        #print(sp)
        pipe = subprocess.Popen("echo "+ sp +" | sudo -S whoami ", shell=True, stdout=subprocess.PIPE)
        fbuf = pipe.stdout
        for line in fbuf.readlines():
            lines = line.decode().split("\n") #            
            print(lines)
            if lines[0] != 'root':
                print('Wrong root pass!')
            else:
                return Background.mount_usb_action(sp)

    @staticmethod
    def mount_usb_action(sp): #dev, dirn
        
        dev = '/dev/'+ Background.dev
        #print(dev)        print(dev)
        #dirp = '/media/alex/'+ Background.model #dirn

        #udisksctl mount --block-device /dev/sdc1

        #return
        
        with open(os.devnull, 'w') as devnull:
            #out = subprocess.run(['sudo', 'mount', '-t', 'vfat', dev, dirp, '-o', 'uid=1000,gid=1000,utf8,dmask=027,fmask=137'], stdin=cmd1.stdout, stdout=devnull, stderr=devnull)
            #cmd1 = subprocess.Popen(['echo', sp], stdout=subprocess.PIPE)
            out = subprocess.run(['udisksctl', 'mount', '--block-device', dev], stdin=devnull, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            err = out.stderr.decode("utf-8")
            if err != '':

                if "Mounted" not in err:
                    return

                print(err)
                dirp = err.split('at `')
                dirp = dirp[1].split("'")
                dirp = dirp[0]                

            else:
                out = out.stdout.decode("utf-8")
                
                #print(out)                print(out)
                out = out.split("\n")
                out = out[0]
                out = out.split('at ')
                out = out[1]
                dirp = out[:-1]
        #print(dirp)
        #print('=============')
        return dirp

    @staticmethod
    def preex(user_uid, user_gid):
        os.setuid(user_uid)
        #os.setgid(user_gid)

    @staticmethod
    def check_encfs_mounted():

        if os.path.isfile(Background.kdbx_fp):
            Background.login()
            return True     

        while(not time.sleep(1)):        #print(123)
            res = Background.check_encfs_mounted()       #print(dev)
            if res:
                return

    @staticmethod
    def mount_encfs(dirp):    
        
        fp = dirp +'/sysconfig.cfg'

        if not os.path.exists(fp):
            #p = subprocess.Popen("echo '"+ fp + "' >> /tmp/00000000NNNN.txt", shell=True)
            #p = subprocess.Popen("touch /tmp/0000000000NNNNNNNNNNNNNNNNNNNNN", shell=True)
            return

        with open(fp) as f:
            content = f.readlines()
            #print(content)
        
        fp = base64.b64decode(content[0]).decode('utf-8')
        Background.sp = base64.b64decode(content[1]).decode('utf-8')

        p = subprocess.run(['bash', '/home/alex/0Documents/Encrypts/to_mount_cli.sh', fp], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=None, shell=False, input=None)
        #err = p.stderr.decode("utf-8")  
        out = p.stdout.decode("utf-8")
        #print(out)
        out = out.split("\n")
        #print(out)
        dpm = out[-3]
        mm = out[-2]

        if "already mounted" in dpm and "already mounted" in mm:
            Background.login()
            return
            
        Background.check_encfs_mounted()
        return
        
    @staticmethod
    def login():    
        
        p = subprocess.Popen("echo "+ Background.sp +" | keepassxc --pw-stdin /home/alex/0Dropbox/My/KDBX/nevi.kdbx", shell=True)
        Background.window.quit()
        #out = subprocess.run(['keepassxc', '--pw-stdin', Background.kdbx_fp], stdout=subprocess.PIPE,  stdin=None, shell=True, input=None)

        return

    @staticmethod
    def set_window(window):        
        Background.window = window
        return