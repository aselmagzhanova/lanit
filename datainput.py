import psycopg2
conn = psycopg2.connect("dbname=lanit user=postgres")

import random
n = int(input('Input quantity '))
cur = conn.cursor()


names = ['Tracey','Mark','Carl','Paul','Victoria','Brian','Linda','Jennifer','Julia','Lisa','Adam','Alan','Samantha','Rebecca','Sharon','Catherine','Amanda','Angela','Susan','Donna','Michael','Daniel','Philip','Jason','KKevin','Alan','Adam']


vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
end = ['son','fer','pez','wis','lez','len','ker','ner','man']


professions = ['allergist','cardiologoist','anesthesiologist','dentist','dermatologist','microbiologist','neurologist']

length_n = len(names)-1
length_v = len(vowels)-1
length_c = len(consonants)-1
length_end = len(end)-1
length_p = len(professions)-1

for i in range (0,n):
	query = "INSERT INTO Doctors(FName,LName,Profession) VALUES('%s','%s','%s')" % (names[random.randint(0,length_n)],consonants[random.randint(0,length_c)]+vowels[random.randint(0,length_v)].lower()+consonants[random.randint(0,length_c)].lower()+vowels[random.randint(0,length_v)].lower()+end[random.randint(0,length_end)],professions[random.randint(0,length_p)]) 
	cur.execute(query)


conn.commit()

cur.close()
conn.close()

