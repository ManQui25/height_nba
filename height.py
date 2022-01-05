import csv
#https://www.openintro.org/data/csv/nba_heights.csv
menu = """
Which NBA player is the same height as you? 
Find out by typing in nunber your height in meters like that: 1.78 
"""

height = float(input(menu))

if height > 0:
    with open('nba_heights.csv', "r", newline='') as f:
        reader = csv.DictReader(f, delimiter=",")
        p = []
        height = str(height)
        for row in reader:
            if height == row['h_meters']:
                name = row['first_name'] + " " + row['last_name']
                p.append(name)
            else:
                pass
    
    if len(p) > 0:
        for l in p:
            print(l)
    else:
        print("No matches found")
    
                    
else:
    print("Please enter a correct number ")

  

                                 

