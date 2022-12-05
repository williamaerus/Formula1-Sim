## code made by Francesco Serangeli

# this is not meant to be realistic or any kind of similar to the reality


import random
import time
from datetime import datetime
from datetime import date
now = datetime.now()
drivers_number = {'Lewis Hamilton': 44, 'Max Verstappen': 33, 'Charles Leclerc': 16, 'Sergio Perez': 11, 'Carlos Sainz': 55, 'Lando Norris': 4, 'Daniel Ricciardo': 3, 'Esteban Ocon': 31, 'Pierre Gasly': 10, 'Fernando Alonso': 14, 'Sebastian Vettel': 5, 'Guanju Zhou': 24, 'Yuki Tsunoda': 22, 'Alexander Albon': 23, 'Mick Schumacher': 47, 'Kevin Magnussen': 20, 'George Russell': 63, 'Valtteri Bottas': 77, 'Lance Stroll': 18,'Nicholas Latifi':6}
mercedes = {'name':'Mercedes Amg',
            'first_driver': 'Lewis Hamilton',
            'second_driver': 'George Russell',
            'car_power': 3}
redbull = {'name':'Redbull',
            'first_driver': 'Max Verstappen',
            'second_driver': 'Sergio Perez',
            'car_power': 1}
ferrari = {  'name':'Scuderia Ferrari',
            'first_driver': 'Charles Leclerc',
            'second_driver': 'Carlos Sainz',
            'car_power': 2}
mclaren = {'name':'claren',
            'first_driver': 'Lando Norris',
            'second_driver': 'Daniel Ricciardo',
            'car_power': 4}
alpine = {'name':'Alpine',
            'first_driver': 'Fernando Alonso',
            'second_driver': 'Esteban Ocon',
            'car_power': 5}
alfa_romeo = {'name':'Alfa Romeo',
            'first_driver': 'Valtteri Bottas',
            'second_driver': 'Guanju Zhou',
            'car_power': 6}
aston_martin = {'name':'Aston Martin',
            'first_driver': 'Sebastian Vettel',
            'second_driver': 'Lance Stroll',
            'car_power': 7}
haas = {    'name':'Haas',
            'first_driver': 'Kevin Magnussen',
            'second_driver': 'Mick Schumacher',
            'car_power': 8}
alphatauri = {'name':'Alphatauri',
            'first_driver': 'Pierre Gasly',
            'second_driver': 'Yuki Tsunoda',
            'car_power': 9}
williams = {'name':'williams',
            'first_driver': 'Alexander Albon',
            'second_driver': 'Nicholas Latifi',
            'car_power': 10}

Positions = {'Lewis Hamilton':1, 'Sergio Perez':2, 'Charles Leclerc':3, 'George Russel':4, 'Carlos Sainz':5, 'Max Verstappen:':6,
                'Daniel ricciardo':7, 'Lando norris':8, 'Esteban Ocon':9, 'Fernando Alonso':10,
                'Sebastian Vettel':11, 'Nicholas Latifi':12, 'Kevin Magnussen':13, 'Alexander Albon':14, 'Pierre Gasly':15, 'Valteri Bottas':16, 'Yuki Tsunoda':17, 'Lance Stroll':18, 'Mick Schumacher':19, 'Guanju Zhou':20}
grid = []
MOMENTARYOVERTAKER = 0 
MOMENTARYOVERTAKEN = 0 

teams = [redbull,mercedes,ferrari,mclaren,alphatauri,alpine,alfa_romeo,aston_martin,haas,alphatauri,williams]
lap = 1 
top6teams = [redbull,ferrari,mercedes]
others = [mclaren,alpine]
other10teams = [alfa_romeo,aston_martin,haas,alphatauri,williams]
top6drivers = [top6teams[0]['first_driver'],top6teams[1]['first_driver'],top6teams[2]['first_driver'],top6teams[0]['second_driver'],top6teams[1]['second_driver'],top6teams[2]['second_driver']]
otherDrivers = [others[0]['first_driver'],others[1]['first_driver'],others[0]['second_driver'],others[1]['second_driver']]
other10drivers = [other10teams[0]['first_driver'],other10teams[1]['first_driver'],other10teams[2]['first_driver'],other10teams[3]['first_driver'],other10teams[4]['first_driver'],other10teams[0]['second_driver'],other10teams[1]['second_driver'],other10teams[2]['second_driver'],other10teams[3]['second_driver'],other10teams[4]['second_driver']]
DriversOnGrid_Number = (int(len(top6drivers))+int(len(otherDrivers))+int(len(other10drivers)))
overtakeSuccesMsg =  ["AND HE MAKES IT!","OH MY GOD WHAT A MOVE FROM HIM","HE FINALLY HE OVERTOOK HIM"]
overtakeFailureMsg = ["unfortnately he can't overtake him","but there is not enough space there, so he backs out"]

report = []


def create_grid():
    drivers = drivers_number.keys()
    global top6teams
    global top6drivers
    global others
    global otherDrivers
    global other10teams
    global other10drivers
    random.shuffle(top6drivers)
    random.shuffle(otherDrivers) 
    random.shuffle(other10drivers)
    
    for i in top6drivers:
        grid.append(i)
    for i in otherDrivers:
        grid.append(i)
    for i in other10drivers:
        grid.append(i)
    print("")
    print("")
    # print(f"here is the starting grid: \n{('    , ').join(top6drivers)}    , {('    , ').join(otherDrivers)}    , {('    , ').join(other10drivers)}")
    print(f"here is the starting grid: \n{('    , ').join(grid)}")
    print("")

def starting_animation(timess):
    while timess:
        mins, secs = divmod(timess, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        timess -= 1
      
    print("AND IT'S LIGHTS OUT AND AWAY WE GO\n")
    time.sleep(0.5)
timess = 5
def start():
    create_grid()
    report.append(f"starting grid:          {grid}")
    starting_animation(5)
    print("")
    print("LAP:     1")
    def polewell():
        options = ['yes','no']
        x = random.choice(options)
        if x == 'yes':
            print(f"{top6drivers[0]} get's away well from pole so {top6drivers[1]} can't even try to overtake him\n")
        else:
            def overtakepole():
                options = ['yes','no']
                y = random.choice(options)
                if y == 'yes':
                    print(f"{top6drivers[0]} doesn't get away well from pole {top6drivers[1]} tryes to overtake him {random.choice(overtakeSuccesMsg[0:1])}")
                    overtakenDriver = top6drivers[0]
                    overtakerDriver = top6drivers[1]
                    report.append(f"{top6drivers[0]}({drivers_number[overtakerDriver]}) overtakes {top6drivers[1]}({drivers_number[overtakenDriver]})")
                    grid[0],grid[1] = grid[1],grid[0]
                else: 
                    print(f"{top6drivers[0]} doesn't get away well from pole, {top6drivers[1]} {random.choice(overtakeFailureMsg)}")
            overtakepole()

    
    polewell()

def overtake():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global MOMENTARYOVERTAKEN
    global MOMENTARYOVERTAKER
    maxNumber = (int(len(grid))-1)
    if maxNumber <= 6:
        finishProcedure()
    def makeOvertake():
        Overtaken = random.randrange(maxNumber)
        Overtaker = int(Overtaken+1)
        overtakenDriver = grid[Overtaken]
        overtakerDriver = grid[Overtaker]
        print(f"{current_time}:       {grid[Overtaker]} overtakes {grid[Overtaken]}")
        report.append(f"LAP {lap}:           {grid[Overtaker]}({drivers_number[overtakerDriver]}) overtakes {grid[Overtaken]}({drivers_number[overtakenDriver]})")    
        grid[Overtaker], grid[Overtaken] = grid[Overtaken], grid[Overtaker]
        print("")     
        print()
    makeOvertake()
def crash():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    MaxNumber = int(len(grid)-1)
    if MaxNumber <= 6:
        finishProcedure()
    crashed = int(random.randrange(MaxNumber))
    crashMsgs = [f"{current_time}:       OH MY GOD, {grid[crashed]} is out of the race", f"{current_time}:       and here is {grid[crashed]} retired due to an engine failure", f"{current_time}:       and there he is {grid[crashed]} who has gone straight into the barrier", f"{current_time}:       and there he is {grid[crashed]} stuck in the gravel" ]
    crashMsg = random.choice(crashMsgs)
    crashedDriver = grid[crashed]
    print(f"{crashMsg}\n")
    report.append(f"LAP: {lap} {grid[crashed]}({drivers_number[crashedDriver]}) is out of the race")
    grid.remove(grid[crashed])
def doubleCrash():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    MaxNumber = int(len(grid)-1)
    if MaxNumber <= 6:
        finishProcedure()
    crashed1 = int(random.randrange(MaxNumber))
    if crashed1 == 0:
        crashed1 = crashed1 + 1
    crashed2 = int(crashed1-1)
    crashedDriver1 = grid[crashed1]
    crashedDriver2 = grid[crashed2]
    crashMsgs = [f"{current_time}:       OH NO {grid[crashed1]} crashed in {grid[crashed2]}",f"{current_time}:       damn 2 cars are involved in a incident, {crashedDriver2} has been hit by {crashedDriver1} and now they are both out of the race", f"{current_time}:       WOW that was an impossible move by  {crashedDriver1} who tried to overtake {crashedDriver2} in a impossible place, and now they are both out.",f"{current_time}:       how unlucky for {crashedDriver2} who has been taken out from {crashedDriver1} now they are both out"]
    print(random.choice(crashMsgs))
    report.append(f"LAP     {lap} {grid[crashed1]}({drivers_number[crashedDriver1]}) and {grid[crashed2]}({drivers_number[crashedDriver2]}) are out of the race")
    grid.remove(crashedDriver1)
    grid.remove(crashedDriver2)



def Lap():
    global lap
    numbers = [0,0,0,0,1,1,2,2,3]
    x = random.choice(numbers)
    lap = lap+1
    print(f"LAP:    {lap}") 
    print("")
    events = [crash,doubleCrash,overtake,overtake,overtake,overtake,overtake,overtake,overtake,crash]
    for _ in range(x):
        if x == 0:
            print("     - - - - - - - - ")
            Lap()
        
        print("")       
        random.choice(events)()
           
def finishProcedure():
    report.append(f"final grid:         {grid}")
    print(f"podium:\n | 2nd {grid[1]} | 1st {grid[0]} | 3rd {grid[2]} |")
    print("")
    print(f"final arrival order:        {('     , ').join(grid)}")
    def saveque():
        saveQ = input(f"do you want to save this report? ")
        if saveQ == "yes":
            saveReport()
            print("report saved")
        elif saveQ == "YES":
            saveReport()
            print("report saved")
        elif saveQ == "Yes":
            saveReport()
            print("report saved")
        elif saveQ == "yEs":
            saveReport()
            print("report saved")
        elif saveQ == "yeS":
            saveReport()
            print("report saved")
        elif saveQ == "YEs":
            saveReport()
            print("report saved")
        elif saveQ == "yES":
            saveReport()
            print("report saved")    
        elif saveQ == "no":
            print("report not saved")
        elif saveQ == "NO":
            print("report not saved")
        elif saveQ == "nO":
            print("report not saved")
        elif saveQ == "No":
            print("report not saved")
        else: 
            print("this is not a valid option please type it again\n")
            saveque()
    saveque() 
    
    exit()

def saveReport():
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open(f"report {today} - {current_time}.txt", "w")
    f.write(f"report of the race {today} - {current_time}\n")
    f.writelines(f"{('     , ').join(report)}")


def main():
    
    laps = input("how many laps is this race going to be:       ")
    laps = int(laps)
    start()
    for _ in range(laps):
        Lap()
        time.sleep(0.5)
    # report.append("\n\n\n\n")
    # driverTest = str(grid[1])
    # report.append(f"{drivers_number[driverTest]}")
    # print(report)

    finishProcedure()
    
main()
