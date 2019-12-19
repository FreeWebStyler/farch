#!/bin/bash
#read -s -p "Enter Password: " pass
#echo $pass

#echo $XDG_DESKTOP_DIR
#exit 1
iu=$(whoami) # initial user #echo $iu #exit 0
sudo bash $PWD/suinstall.sh $iu