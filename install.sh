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
git clone https://github.com/goncalogiga/ternest.git
mv ternest .ternest
cd .ternest/
gcc ternest.c -o ternest
mv ternest ../.local/bin

touch $HOME/.ternest/user/your_marks.txt
mkdir cache
touch $HOME/.ternest/cache/new_marks.txt

echo "Ternest is now installed! Use ternest --config to set it up completly."
