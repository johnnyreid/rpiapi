#!/bin/bash

[[ $(id -u) = "0" ]] || { echo "Please run the script as root user. sudo $0"; exit; }

# Install dependencies
apt-get -y install python3 python3-pigpio apache2 apache2-utils libapache2-mod-wsgi-py3

# Enable module wsgi
a2enmod wsgi

# Copy configuration file to apache2 directory conf-enabled
cp rpiapi.conf /etc/apache2/conf-enabled/

# Add user www-data to the gpio group (So that the API can access the GPIO pins)
adduser www-data gpio

# Restart apache2 ir order to reload configurations
systemctl restart apache2

# Clear the screen
clear

echo -e "Enter the new password for the user admin \n\n\n"

# Change the password for the admin user (default: admin)
htpasswd /var/www/rpiapi/src/.htpasswd admin

ip=$(hostname -I | cut -d " " -f1) 

echo "Initialising the output pins...."
python3 initialiseGpos.py

echo "All set."
echo "You can check the API at http://$ip/rpiapi"
