#!/bin/bash

# TEST IF TERNEST IS ALWREADY INSTALLED
cd
if [ -d ".ternest" ] ; then
  echo "Reinstalling ternest..."
  rm -rf .ternest
else
  echo "Installing ternest..."
fi

# GET TERNEST FROM GIT HUB AND MOVE EXE FILE INTO BIN FOLDER
sudo git clone https://github.com/goncalogiga/ternest.git
mv ternest .ternest
cd .ternest/
gcc ternest.c -o ternest
mv ternest ../.local/bin

# Launch the config initializer
bash ./user/first_launch.sh
