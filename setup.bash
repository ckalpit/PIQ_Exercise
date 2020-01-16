#!/bin/bash
# this is pressuming that the machine has latest virtualenv installed as older version of virtula env causes issue while running through bash 
virtualenv -p /usr/bin/python3 plateiq_env
source ./plateiq_env/bin/activate
pip install -Ur requirements.txt

