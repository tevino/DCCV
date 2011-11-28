#!/usr/bin/bash

chmod +x ./dccv.py
current_dir=$(dirname -- $(readlink -f -- "$0")) 
echo \#Start alias for DCCV >>~/.bashrc
echo alias\ d\="$current_dir/dccv.py" >>~/.bashrc 
echo \#End alias for DCCV >>~/.bashrc
echo Installation finished.
