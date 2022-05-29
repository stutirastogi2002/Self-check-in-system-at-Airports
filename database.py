import mysql.connector as connector


class DBHelper:
    pnrNo = "NA"
    firstName = "NA"
    lastName = "NA"
    fDay = "NA"
    origin = "NA"
    destination = "NA"

    def __init__(self):
        self.con = connector.connect(host='localhost', user='root', password='stu@@@', database='faces')
        query = 'create table if not exists tableface(pnrNo varchar(5) primary key,firstName varchar(30),lastName ' \
                'varchar(30),fDay varchar(10),origin varchar(30),destination varchar(30)) '
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    def insert_user(self, pnrno, firstname, lastname, fday, origin, destination):
        query = "insert into tableface(pnrNo,firstName,lastName,fDay,origin,destination)values('{}','{}','{}','{}'," \
                "'{}','{}')".format(pnrno, firstname, lastname, fday, origin, destination)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("saved to db")

    def fetch(self, pnr):
        query = "select * from tableface where pnrNo='{}'".format(pnr)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            self.pnrNo = row[0]
            self.firstName = row[1]
            self.lastName = row[2]
            self.fDay = row[3]
            self.origin = row[4]
            self.destination = row[5]
            return row[0]

    # getter functions
    def getPnr(self):
        return self.pnrNo

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFDay(self):
        return self.fDay

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.destination


''''
obj.insert_user("A11A11","Bill","Gates","Sunday","New Delhi","California")
obj.insert_user("B22B22","Sundar","Pichai","Sunday","New Delhi","Mumbai")
obj.insert_user("C33C33","Jeff","Bezos","Monday","New Delhi","London")
obj.insert_user("D44D44","Ratan","Tata","Sunday","Mumbai","Sydney")
'''
