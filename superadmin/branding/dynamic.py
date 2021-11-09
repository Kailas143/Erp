import mysql.connector


mydb=mysql.connector.connect(
        host  = 'localhost',
        user = 'root',
        password ='password',
        database ='dynamicdb_erp2', 
)

mycursor=mydb.cursor()
mycursor.execute("Select * from domain_tbl ")
domain_details=mycursor.fetchall()



def dynamic_link(service,api):
    mycursor=mydb.cursor()
    query="select * from domain_tbl WHERE service = '%s'" % service 
    mycursor.execute(query)
    domain_details=mycursor.fetchall()
    url = f"{domain_details[0][2]}://{domain_details[0][1]}:{domain_details[0][3]}/{api}/"
    return url
        
