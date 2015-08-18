#!/bin/bash

python prettyxml.py $1 | sed -e 's/\s*\t*\s*$//g'
