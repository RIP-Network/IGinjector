#!/bin/bash

read -p "Nombre de la Victima Por Favor : " victima
echo

sudo wget --wait=40 --limit-rate=40K -U Mozilla -bq https://www.picnob.com/profile/$victima/ -O $victima.txt >/dev/null
sleep 6
echo -e "\e[31mFoto de Perfil: \e[0m" `cat $victima.txt | awk '/href/&&/scontent/ {print $2}' | cut -c 7- | rev | cut -c10- | rev`
