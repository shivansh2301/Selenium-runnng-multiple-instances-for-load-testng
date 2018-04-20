# Selenium-runnng-multiple-instances-for-load-testng

A python script for user simulation on a website using browser simulation tool Selenium

The script(main.py) reads username and password from a file and then passes them as arguements to (runner.py) to perform simulation.

runner.py is spawned as a subprocess so many instances can be run concurrently.
