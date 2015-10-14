import argparse

def Working_Experience():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        Calender = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        for line in f:
            line = line.rstrip('\n')
            timeline = [[i.split() for i in a.split('-')] for a in line.split(';')]
            total_time = 0
            for time in timeline:
            	years_diff = (int(time[1][1])- int(time[0][1]))*12
            	print('{}-{} = {} months'.format(time[1][1],time[0][1],years_diff))
            	months_diff = Calender[time[1][0]]- Calender[time[0][0]]
            	total_time  += (years_diff+months_diff)//12
            print(total_time)	
Working_Experience()