import sqlite3

conn = sqlite3.connect('Adoptee Entry.db')
c = conn.cursor()


def create_tableadoptees():
    c.execute('CREATE TABLE IF NOT EXISTS Adoptees(Firstname TEXT, Lastname TEXT, Location TEXT, Birthdate REAL, Race TEXT)')

def create_tablebioparents():
    c.execute('CREATE TABLE IF NOT EXISTS BiologicalParents(Firstname TEXT, Lastname TEXT, Location TEXT, ChildBirthdate REAL, Race TEXT) ')
    
def data_adoptees():
    KeepGoing = 'y'
    while KeepGoing == 'y':
        print("These questions are for adoptees")
        Firstname = input("What is your first name?")
        Lastname = input ("What is your last name?")
        Location = input("Where are you from?")
        Birthdate = input("When were you born?")
        Race = input("What is your race?" )
        KeepGoing = input("Are there any more adoptees to account for?" + "\n")

        c.execute ("INSERT INTO Adoptees (Firstname, Lastname, Location, Birthdate, Race) VALUES (?, ?, ?, ?, ?)",
                    (Firstname, Lastname, Location, Birthdate, Race))

    conn.commit()


def data_bioparents():
    KeepGoing = 'y'
    while KeepGoing == 'y':
        print("\n" + "These questions are for biological parents")
        Firstname = input("What is your first name?")
        Lastname = input ("What is your last name?")
        Location = input("Where did you leave your child?")
        ChildBirthdate = input("When is your child's birthday?")
        Race = input("What is your race?")
        KeepGoing = input("Are there any more biological parents to account for?" + "\n")
        c.execute ("INSERT INTO BiologicalParents (Firstname, Lastname, Location, ChildBirthdate, Race) VALUES (?, ?, ?, ?, ?)",
                    (Firstname, Lastname, Location, ChildBirthdate, Race))
        
    conn.commit()

def comparison():
    LastnameAdoptees= c.execute('''SELECT Lastname FROM Adoptees''')
    LastnameBio = c.execute('''SELECT Lastname FROM BiologicalParents''')
    LocationBio = c.execute('''SELECT Location FROM BiologicalParents''')
    LocationAdoptees= c.execute('''SELECT Location FROM Adoptees''')
    ChildbirthdateAdoptees= c.execute('''SELECT Birthdate FROM Adoptees''')
    ChildbirthdateBio = c.execute('''SELECT Childbirthdate FROM BiologicalParents''')
    RaceBio= c.execute('''SELECT Race FROM BiologicalParents''')
    RaceAdoptees = c.execute('''SELECT Race FROM Adoptees''')
    similarities = 0
    for item in LastnameAdoptees:
        if item == item in LastnameBio:
            return (item)
            similarities = similarities + 1
    if LocationAdoptees == LocationBio:
        similarities = similarities +1 
    if ChildbirthdateAdoptees == ChildbirthdateBio:
        similarities = similarities +1 
    if RaceAdoptees == RaceBio:
        similarities = similarities +1
    if similarities >= 2:
        print("There is a good possibility that you have found your adoptee or biological parent.")
    else:
        print("You're unlikely to have found your adoptee or biological parent.")





create_tableadoptees()
create_tablebioparents()
data_adoptees()
data_bioparents()




