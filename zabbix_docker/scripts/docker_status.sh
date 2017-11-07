#!/bin/bash
#
function countContainers() {
    sudo /usr/bin/docker ps -q $1 | wc -l
}

function countCrashedContainers() {
    sudo /usr/bin/docker ps -a | grep -v -F 'Exited (0)' | grep -c -F 'Exited ('
}

TYPE=${1-all}

case $TYPE in
    running) COUNT_FUNCTION="countContainers"; shift;;
    crashed) COUNT_FUNCTION="countCrashedContainers"; shift;;
    all) COUNT_FUNCTION="countContainers -a"; shift;;
esac

$COUNT_FUNCTION
