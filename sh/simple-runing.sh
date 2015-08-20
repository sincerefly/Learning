#!/bin/bash

BASEDIR='/server'

while true; do

    PRO_NOW=`netstat -tunlp| grep "7000" | wc -l 2>/dev/null`

    if [ $PRO_NOW -eq 0 ]; then
        cd $BASEDIR
        node ./bin/www > /tmp/run_node.log 2>&1  &
    else
        echo "`date`  7000 is listening..."
    fi
    sleep 3

done
