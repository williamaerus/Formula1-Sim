# Install
There is nothing to install for this script, it uses this modules:

1. random
2. time
3. datetime

if you miss one of this modules you can install them with `pip`
of course you need to download the complete repository and not just the main.py file
# how to use it
the code works without any kind of setup needed, you just need to run the script using this command: windows `python main.py` linux `python3 main.py`
then you will need to insert the number of laps that you want your race to be, and the language that you want to use english ore italian for now, the script is made for around 30 laps races, of course it's going to work also with longer ones with the risk of not having enough cars on grid. 

When there are not enough cars on grid the script is going to stop automatically and start the finish procedure. 

# grid creation system 
to be able to create a "realistic" starting grid i divided the drivers in 3 groups, front 3 rows, 2 transition teams, and the rest of the grid, so you can't have latifi on pole unless you change the script, pay attention when doing this other parts of code might stop working. the drivers are divided just when creating the grid, after the "qualifying" process they all get stored in the complete grid to avoid any problems by deviding the them, and making a little easier to manage the drivers on grid.
# finish procedure
when the number of laps is reached or there are not enough cars on grid to continue the race (6 cars) the script will run the finish procedure, that shows the podium and the final arrival order, and asks if you want to save the report of the race
# the report
every single time that there is an overtake or a car get's out of the race that event get's stored in the report that you can save at the end of the race to be able to look at it later. The report is saved in a folder named with this format, `race {date} - {time}` in which you will find 2 files_

1. the report
2. the reaction times of the drivers
