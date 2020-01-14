#!/bin/bash

cd
git clone https://github.com/goncalogiga/ternest.git
mv ternest .ternest
cd .ternest/
gcc ternest.c -o ternest
mv ternest ../.local/bin
