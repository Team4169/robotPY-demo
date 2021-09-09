# Team 4169 robotPY demo
This is demo code built with robotPY to be tested in the lab for the 2021 FRC season, and updated for the 2022 season.

This is only demo code, and should not be deployed in a production environment by any team.
#Setup your machines environment
Start by creating a venv (virtual environment) by running
``` shell
python3 -m venv environment
```
Enter your venv
```shell
source environment/bin/activate
```
Install requirements
```shell
pip3 install -r requirements.txt
```
#Deploy and run demo code
The optional nc param activates net console, which allows you to see that robots python logs on your local machine.
```shell
python3 robot.py deploy --nc
```
Finally, run your robot code!
```shell
python3 robot.py run --nc
``` 
