#!/bin/bash
IFS=$'\n'
for name in $(ls); do
    #echo $name
    if [ -d $name ]; then
        #echo $name | sed -e "s/-/. /";
        mv $name $(echo $name | sed -e 's/-/. /')
    fi
done
