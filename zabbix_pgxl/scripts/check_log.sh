#!/bin/bash
#
S_DATA=$(date +%F)
#S_TIME=$(date "+%H:%M")
S_TIME=$(date +%F" ""%H":"%M")
File_Log=/data/pgxl/nodes/gtm/gtm.log
case "$1" in
    error)
         sudo grep "${S_TIME}" $File_Log|grep "ERROR"|wc -l
        ;;
    fatal)
         sudo grep "${S_TIME}" $File_Log|grep "FATAL"|grep -v 'Expecting a startup message, but received'|wc -l
        ;;
    warning)
         sudo grep "${S_TIME}" $File_Log|grep "WARNING"|grep -v 'drace: gtm()'|wc -l
        ;;
    *)
        echo "Usage: `basename $0` {error|fatal|warning}"
        exit 3
        ;;
esac
exit 0
