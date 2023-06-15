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
clear
python3 IGinjector.py