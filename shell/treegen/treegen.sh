#!/usr/bin/env bash

# Bash script to generate tree structure of Directory
# Pravendra Singh : @hackpravj

pwd=$(pwd)
find $pwd -print | sed -e "s;$pwd;\.;g;s;[^/]*\/;|__;g;s;__|; \\\;g"
