#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please, run as root"
  exit
fi

iu=$1

bin_name=farch
exec_name=farch.py

install_to=/home/$iu/0data/progs

base_dirp="$(cd "$(dirname "$0")"; pwd)";

IFS='/' # hyphen (-) is set as delimiter
read -ra ADDR <<< "$base_dirp" # str is read into an array as tokens separated by IFS
IFS=' ' # reset to default value after usage
base_dir_name=${ADDR[-1]}

#echo $install_to/$base_dir_name exit 0
#echo $install_to/$base_dir_name
#exit 1
rm -rf $install_to/$base_dir_name > /dev/null 2>&1
rm /usr/bin/$bin_name > /dev/null 2>&1 |
rm /home/$iu/Desktop/$bin_name.desktop