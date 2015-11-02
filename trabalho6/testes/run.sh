#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

javac Main.java
cd ..
make
cd testes

for file in *.txt
do
  if [[ -f $file ]]; then
    nosso=`../main < $file`
    tjava=`java Main < $file`

    if [ "$nosso" = "$tjava" ]; then
      printf "${GREEN}✓ ${file}${NC}\n"
      printf "\t ${nosso}\n"
      printf "\t ${tjava}\n"
    else
      printf "${RED}✗ ${file}${NC}\n"
      printf "\t ${nosso}\n"
      printf "\t ${tjava}\n"
    fi
  fi
done
