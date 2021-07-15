#!/bin/bash

git checkout master
git pull origin master
docker-compose build
docker-compose restart
