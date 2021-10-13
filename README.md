# Auto Cookie Clicker

A simple bot that plays cookie clicker for you.

## Features
 * Purchases upgrades and products for you, at a regular interval
 * Includes a GUI that allows you to tell the bot to rapid click _n_ number of times
 * Runs in its own instance of Chrome

## How to use
  1. Download the zip containing the project
  2. Unzip and naviagate to the directory in Terminal
  3. Make sure you have Python installed
  4. Run `python3 -m venv venv`
  5. Run `source venv/bin/activate`
  6. Run `pip install -r requirements.txt`
  7. You may need to run `chmod u+x run.sh` for the runner
  8. Run `./run.sh`
  9. Enjoy!

## Notes
 * Each execution of rapid clicks halts all other processes. Please wait until it finishes completely
 * Make sure to disable Vimium if running through the Repl

## Stack
 * Python
    * Selenium
    * APscheduler
    * tkinter
 * Bash

