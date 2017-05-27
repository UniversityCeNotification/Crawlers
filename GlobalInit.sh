#!/bin/bash

read -p 'There is .env file in crawler?(y/n) : ' status
if [[ "$status" = "n" ]]; then
  read -p "MongoDbUrl:" url
  read -p "MongoDbName:" name
  echo "MongoDbUrl='$url'" > .env
  echo "MongoDbName='$name'" >> .env
fi

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
