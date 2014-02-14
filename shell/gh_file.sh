#!/bin/bash

# my attempt when first time, I came through people near to me 
# using nice dotfiles collection

# I use it, when I have to use/download
# a particular file from a "GitHub" Repo(not entire repo files)
# it sounds much-more helpful when particular file is too lengthy
# like using "facebook-php-sdk", you basically need these two php files
# https://github.com/facebook/facebook-php-sdk/blob/master/src/base_facebook.php
# https://github.com/facebook/facebook-php-sdk/blob/master/src/facebook.php

# it takes arguments as follows('user/organization','repository','path','filename')
# 'path' argument is like 'branch'+'file_path' : 'master/src/facebook.php' for given example

# defauls
raw_url="https://raw.github.com"
user='pravj'
repo='gunnu'
path=''
file=''
 
# number of input arguments
args=$#
 
if [ $args -eq 4 ]
then
	user=$1
	repo=$2
	path=$3
	file=$4
	touch $file
	curl "$raw_url/$user/$repo/$path/$file" > $file

else
	echo "it needs 4 arguments to process: $# provided"
fi

#ToDO
#to save file in directory as, it is stuructured in GitHub Repo