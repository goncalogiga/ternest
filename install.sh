#!/bin/bash

cd
if [ -d ".ternest" ] ; then
  echo "Reinstalling ternest..."
  rm -rf .ternest
else
  echo "Installing ternest..."
git clone https://github.com/goncalogiga/ternest.git
mv ternest .ternest
cd .ternest/
gcc ternest.c -o ternest
mv ternest ../.local/bin
