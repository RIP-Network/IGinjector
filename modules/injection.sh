#!/bin/bash

echo
read -p "Usuario de la víctima : " user
echo
wget --wait=40 --limit-rate=40K -U Mozilla -bq https://www.picnob.com/profile/$user/ -O $user.txt >/dev/null
sleep 6
echo "Information about $user ( Version Reducida ) "
echo "/////////////////////////////////////////////"
echo "Foto de Perfil: " `cat $user.txt | awk '/href/&&/scontent/ {print $2}' | cut -c 7- | rev | cut -c10- | rev`
echo "Usuario: @$user"
echo "Nombre: " `cat $user.txt | awk -F= '/"fullname">/ {print $2}' | cut -c 12- | rev | cut -c6- | rev`
echo "Posts: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==1{print}'`
echo "Seguidores: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==2{print}'`
echo "Siguiendo: " `cat $user.txt | awk -F= '/"num"/ {print $3}' | cut -c 2- | rev | cut -c3- | rev | awk 'NR==3{print}'`
echo "URL Perfil: https://www.instagram.com/$user"
echo "/////////////////////////////////////////////"
