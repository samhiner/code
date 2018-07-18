#!/usr/bin/env bash

#move any files in your website folder that are not in your github repo to a temporary folder
mv /WEBSITE/FILES/NOT/IN/GITHUB/REPO /FOLDER/OUTSIDE/WEBSITE/FOLDER

#REMEMBER to sudo visudo www-data. 
#make sure you are not inside your website folder, else the script will fail when you delete it
cd /PATH/OUTSIDE/OF/WEBSITE

#delete everything in the website folder (otherwise git clone won't work)
#even if git clone did work in non-empty files, then you would just have two of every file
rm -rf /WEBSITE/FOLDER/*

#clone your github repo into the website folder and delete the .git folder as it is unecessary and can causes permissions issues
git clone https://github.com/smhnr27/portfoliowebsite.git /WEBSITE/FOLDER && rm -rf /WEBSITE/FOLDER/.git

#move everything from your temp folder back to your website
#if some of the files were not on the first level of the website,
#then you will have to create their parent folder again and mv it there
mv /FOLDER/OUTSIDE/WEBSITE/FOLDER/* /WEBSITE/FOLDER
