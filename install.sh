#!/bin/bash

# TEST IF TERNEST IS ALWREADY INSTALLED
cd
if [ -d ".ternest" ] ; then
  echo "Reinstalling ternest..."
  rm -rf .ternest
else
  echo "Installing ternest..."

# GET TERNEST FROM GIT HUB AND MOVE EXE FILE INTO BIN FOLDER
git clone https://github.com/goncalogiga/ternest.git
mv ternest .ternest
cd .ternest/
gcc ternest.c -o ternest
mv ternest ../.local/bin

# GET THE USER'S CONFIG
echo "Please configure ternest:"
read "Your birthdate (DDMMYYYY): " birthdate
read "Your student number: " student_id
#read "Your prefered browser (Firefox or Chrome) :" browser

sed -i '1\dataNaissance = $birthdate' ./.ternest/user/config.txt
sed -i '2\codeEtudiant = $student_id' ./.ternest/user/config.txt
sed -i '1\browser = Firefox' ./.ternest/user/config.txt

# CREATE NECESSARY FOLDERS
touch ./.ternest/user/your_marks.txt
touch ./.ternest/cache/new_marks.txt

# LAUNCH TERNEST FOR TESTING
ternest
