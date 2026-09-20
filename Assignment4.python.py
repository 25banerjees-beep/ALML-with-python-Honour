import  sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
b = cur.execute('select * from employee')
for i in b:
    print("name=" ,i[0])
    print("empID=" ,i[1])
    print("salary=" ,i[2])
    con.close()
    