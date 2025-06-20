#!/bin/bash

# Update system
sudo dnf update -y

# Install Python 3, pip, and git
sudo dnf install -y python3 python3-pip git

# Upgrade pip
sudo pip3 install --upgrade pip

# Clone GitHub repo
cd /home/ec2-user
git clone https://github.com/noyaams1/pokeapi
cd pokeapi
# Installing requirements
sudo pip3 install -r requirements.txt

# Set permissions so ec2-user owns the files
sudo chown -R ec2-user:ec2-user /home/ec2-user/pokeapi

# Creating a welcome message
echo 'echo "Welcome to the Pokemon Drawer! To start the app, type: python3 main.py"' >> /home/ec2-user/.bashrc
echo 'cd ~/pokeapi && python3 main.py' >> /home/ec2-user/.bashrc