#!/bin/bash

for fname in *.ipynb; do
    echo $fname
    jupyter nbconvert $fname --to script 
    pyName=${fname/ipynb/py}
    sed -i '/In\[[0-9, ]*\]:/d' $pyName
    autopep8 -i $pyName 2>/dev/null
done

if [ ! -d "pyFiles" ]; then
    mkdir "pyFiles"
fi

mv *.py pyFiles
