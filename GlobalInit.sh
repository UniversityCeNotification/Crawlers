#!/bin/bash

read -p 'There is .env file in crawler?(y/n) : ' status
if [[ "$status" = "n" ]]; then
  read -p "MongoDbUrl:" url
  read -p "MongoDbName:" name
  echo "MongoDbUri='$url'" > .env
  echo "MongoDbName='$name'" >> .env
fi

runAllCrawlers() {
  for i in $(ls -d ./*/main.py)
  do
      echo ${i%%/main.py}
      cd ${i%%/main.py}
      # Crawler Starting
      virtualenv venv
      source venv/bin/activate
      pip install -r requirements.txt
      python main.py
      deactivate
      # Crawler Finished
      cd -
  done
}

while true
do
  runAllCrawlers
  sleep 10m
done
