#!/bin/bash

# Add the git-core PPA and install git
sudo add-apt-repository ppa:git-core/ppa -y
sudo apt-get update
sudo apt-get install python3-pip -y
sudo apt-get install git -y

# Install Python packages from requirements.txt
pip install -r requirements.txt