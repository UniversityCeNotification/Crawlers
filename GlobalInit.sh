#!/bin/bash

runAllCrawlers() {
  for i in $(ls -d ./*/init.sh)
  do
      echo ${i%%/init.sh}
      cd ${i%%/init.sh}
      bash init.sh
      cd -
  done
}

while true
do
  runAllCrawlers
  sleep 10m
done
