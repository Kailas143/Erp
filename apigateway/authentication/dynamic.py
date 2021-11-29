


from django.db import connections

def dynamic_link(service,api):
    with connections['dynamic'].cursor() as mycursor:
        query="select * from domain_tbl WHERE service = '%s'" % service 
        mycursor.execute(query)
        domain_details=mycursor.fetchall()
        url = f"{domain_details[0][2]}://{domain_details[0][1]}:{domain_details[0][3]}/{api}/"
        print(url,'uu')
        return url
                