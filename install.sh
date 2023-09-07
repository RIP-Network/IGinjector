#!/bin/bash
clear
echo "                       #################################################################################   "
echo "                       #                                                                               #    "
echo "                       #   ██╗ ██████╗ ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗  #   "
echo "                       #   ██║██╔════╝ ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗ #   "
echo "                       #   ██║██║  ███╗██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝ #   "
echo "                       #   ██║██║   ██║██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗ #    "
echo "                       #   ██║╚██████╔╝██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║ #    "
echo "                       #   ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ #    "
echo "                       #################################################################################"                                                                   
echo
echo
sleep 4
apt-get update
apt-get upgrade
clear
apt-get install python3
apt-get install python3-pip
pip3 install selenium
pip3 install pystyle
chmod +x * modules/photo.sh
chmod +x * modules/core.sh
chmod +x * IGinjector.py
sleep 2
clear
echo "Instalado con exito!"
