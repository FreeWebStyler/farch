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

#script_dir="$( cd "$(dirname "$0")" ; pwd -P )"echo $script_dir
#echo $base_dirp echo $base_dir_name
#echo $install_to/$base_dir_name
cp -r $base_dirp $install_to/$base_dir_name
chown $iu:$iu -R $install_to/$base_dir_name
ln -s $install_to/$base_dir_name/$exec_name /usr/bin/$bin_name

desktop_copy_to=/home/$iu/Desktop/$bin_name.desktop
#echo $desktop_copy_to

cat >$desktop_copy_to <<EOL
#!/usr/bin/env xdg-open
[Desktop Entry]
Exec=farch
Icon=$install_to/$base_dir_name/res/farch32.png
Name=Fast Archiver
Categories=System;Filesystem;GTK;Utility;
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
X-DBUS-ServiceName=
X-DBUS-StartupType=
X-KDE-SubstituteUID=false
X-KDE-Username=
EOL

#cat $install_to/$base_dir_name/distr/$bin_name.desktop
#cp $install_to/$base_dir_name/distr/$bin_name.desktop $desktop_copy_to
chown $iu:$iu -R $desktop_copy_to