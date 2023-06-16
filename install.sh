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
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
sleep 3
apt-get install unzip
unzip chromedriver_linux64.zip
sleep 2
cd chromedriver_linux64
mv chromedriver /usr/local/bin
sleep 2
chmod +x /usr/local/bin/chromedriver
sleep 2
clear
echo "Instalado con exito!"
