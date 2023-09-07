#!/bin/bash

wget --wait=40 --limit-rate=40K -U Mozilla -bq https://www.picnob.com/profile/$username/ -O $user.txt >/dev/null
sleep 6
echo"Information about $user ( Version Reducida ) "
echo"//////////////////////////////////////////////////////////////"
echo "Nombre: " `cat $user.txt | awk -F= '/"fullname">/ {print $2}' | cut -c 12- | rev | cut -c6- | rev`
echo "Descripcion: " `cat $user.txt | awk '/div class="sum"/ {print}' | cut -c 18- | rev | cut -c7- | rev | awk 'NR==1{print}'`
echo "Posts: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==1{print}'`
echo "Seguidores: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==2{print}'`
echo "Siguiendo: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==3{print}'`
echo"//////////////////////////////////////////////////////////////"