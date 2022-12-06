import random
import time
from datetime import datetime
from datetime import date
import italian as italian
import english as english
import os
d = {'italian': italian, 'english': english}
lang = input('insert a language: ')
language = d[lang]
today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
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
reaction_times = []
teams = [redbull,mercedes,ferrari,mclaren,alphatauri,alpine,alfa_romeo,aston_martin,haas,alphatauri,williams]
lap = 1 
top6teams = [redbull,ferrari,mercedes]
others = [mclaren,alpine]
other10teams = [alfa_romeo,aston_martin,haas,alphatauri,williams]
top6drivers = [top6teams[0]['first_driver'],top6teams[1]['first_driver'],top6teams[2]['first_driver'],top6teams[0]['second_driver'],top6teams[1]['second_driver'],top6teams[2]['second_driver']]
otherDrivers = [others[0]['first_driver'],others[1]['first_driver'],others[0]['second_driver'],others[1]['second_driver']]
other10drivers = [other10teams[0]['first_driver'],other10teams[1]['first_driver'],other10teams[2]['first_driver'],other10teams[3]['first_driver'],other10teams[4]['first_driver'],other10teams[0]['second_driver'],other10teams[1]['second_driver'],other10teams[2]['second_driver'],other10teams[3]['second_driver'],other10teams[4]['second_driver']]
# DriversOnGrid_Number = (int(len(top6drivers))+int(len(otherDrivers))+int(len(other10drivers)))
# overtakeSuccesMsg =  ["AND HE MAKES IT!","OH MY GOD WHAT A MOVE FROM HIM","HE FINALLY HE OVERTOOK HIM"]
# overtakeFailureMsg = language.overtakeFailureMsg

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
    print(f"{language.starting_grid:} \n{('    , ').join(grid)}")
    print("")

def starting_animation(timess):
    while timess:
        mins, secs = divmod(timess, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        timess -= 1
      
    print(language.starting_message)
    time.sleep(0.5)
timess = 5
def start():
    create_grid()
    report.append(f"{language.starting_grid}:          {grid}")
    starting_animation(5)
    print("")
    print("LAP:     1")
    reactionTimes()
    def polewell():
        options = ['yes','no']
        x = random.choice(options)
        if x == 'yes':
            print(f"{top6drivers[0]} {language.starts_good} {top6drivers[1]} {language.cant_overtake}\n")
        else:
            def overtakepole():
                options = ['yes','no']
                y = random.choice(options)
                if y == 'yes':
                    print(f"{top6drivers[0]} {language.starts_bad} {top6drivers[1]} {random.choice(language.overtake_attempt)} {random.choice(language.pole_overtake)}")
                    overtakenDriver = top6drivers[0]
                    overtakerDriver = top6drivers[1]
                    report.append(f"{top6drivers[0]}({drivers_number[overtakerDriver]}) overtakes {top6drivers[1]}({drivers_number[overtakenDriver]})")
                    grid[0],grid[1] = grid[1],grid[0]
                else: 
                    print(f"{top6drivers[0]} {language.starts_bad}, {top6drivers[1]} {random.choice(language.overtakeFailureMsg)}")
            overtakepole()

    
    polewell()
def reactionTimes():
    for i in grid:
        x = random.randrange(200,400)
        reaction_times.append(f"{i}:    0,{x}")
def overtake():
    overtake_attempt = [language.overtake_attempt1,language.overtake_attempt2]
    options = ['yes','no']
    x = random.choice(options)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global MOMENTARYOVERTAKEN
    global MOMENTARYOVERTAKER
    maxNumber = (int(len(grid))-1)
    if maxNumber <= 6:
        finishProcedure()
    def makeOvertake():
        if x == "yes":
            
            Overtaken = random.randrange(maxNumber)
            Overtaker = int(Overtaken+1)
            overtakenDriver = grid[Overtaken]
            overtakerDriver = grid[Overtaker]
            print(f"{current_time}:       {grid[Overtaker]} {random.choice(overtake_attempt)} {grid[Overtaken]} {random.choice(language.overtakeSuccesMsg)}")
            report.append(f"{language.LAP} {lap}:           {grid[Overtaker]}({drivers_number[overtakerDriver]}) overtakes {grid[Overtaken]}({drivers_number[overtakenDriver]})")    
            grid[Overtaker], grid[Overtaken] = grid[Overtaken], grid[Overtaker]
            print("")     
            print()
        else:
            Overtaken = random.randrange(maxNumber)
            Overtaker = int(Overtaken+1)
            overtakenDriver = grid[Overtaken]
            overtakerDriver = grid[Overtaker]
            print(f"{current_time}:       {grid[Overtaker]} {random.choice(overtake_attempt)} {grid[Overtaken]} {random.choice(language.overtakeFailureMsg)}")

    makeOvertake()
def crash():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    MaxNumber = int(len(grid)-1)
    if MaxNumber <= 6:
        finishProcedure()
    crashed = int(random.randrange(MaxNumber))
    crashMsgs = [f"{current_time}:       {language.oh_god}, {grid[crashed]} {language.out}", f"{current_time}:       {language.there_is} {grid[crashed]} {language.retired} {language.engine_fail}", f"{current_time}:       {language.there_is} {grid[crashed]} {language.barrier}", f"{current_time}:       {language.there_is} {grid[crashed]} {language.gravel}" ]
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
    crashMsgs = [f"{current_time}:       {language.oh_no} {grid[crashed1]} {language.crash_type1} {grid[crashed2]}",f"{current_time}:       {language.damn} {crashedDriver2} {language.hit_by} {crashedDriver1} {language.both_out}", f"{current_time}:       {language.impossible_move} {crashedDriver1} {language.who_tried} {crashedDriver2} {language.impossible_place}",f"{current_time}:       {language.unlucky} {crashedDriver2} {language.taken_out} {crashedDriver1} {language.both_out}"]
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
    print(f"{language.podium}:\n | 2nd {grid[1]} | 1st {grid[0]} | 3rd {grid[2]} |")
    print("")
    print(f"{language.arrival_order}        {('     , ').join(grid)}")
    def saveque():
        saveQ = input(f"{language.save_report}")
        if saveQ == "yes":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "YES":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "Yes":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "yEs":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "yeS":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "YEs":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "yES":
            makedir()
            saveReport()
            print(language.saved)  
        elif saveQ == "si":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "Si":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "SI":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "sI":
            makedir()
            saveReport()
            saveReactions()
            print(language.saved) 
        elif saveQ == "no":
            print(language.not_saved)
        elif saveQ == "NO":
            print(language.not_saved)
        elif saveQ == "nO":
            print(language.not_saved)
        elif saveQ == "No":
            print(language.not_saved)
        else: 
            print(f"{language.invalid_option}")
            saveque()
    saveque() 
path = os.getcwd()
reportDir =  (f"{path}/race {today} - {current_time}")  
def makedir():
    os.makedirs(reportDir)
def saveReport():
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open(f"{reportDir}/report.txt", "w")
    f.write(f"report of the race {today} - {current_time}\n")
    f.writelines(f"{('     , ').join(report)}")

def saveReactions():
    f = open(f"{reportDir}/reactions.txt", "w")
    f.write(f"{('   , ').join(reaction_times)}")
    # f.writelines(f"{('     , ').join(report)}")
    

def main():
    
    laps = input(f"{language.lapsQ}       ")
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






    # Bahrain GP
    # Saudi Arabian GP
    # Australian GP
    # Emilia Romagna GP
    # Miami GP
    # Spanish GP
    # Monaco GP
    # Azerbaijan GP
    # Canadian GP
    # British GP
    # Austrian GP
    # French GP
    # Hungarian GP
    # Belgian GP
    # Dutch GP
    # Italian GP
    # Singapore GP
    # Japanese GP
    # United States GP
    # Mexico City GP
    # Brazilian GP
    # Abu Dhabi GP
