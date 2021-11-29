import requests
from rest_framework.response import Response

from .dynamic import dynamic_link


def get_hostname(request) :
    print(request.get_host())
    print(request.get_host().split(':')[0].lower(),'000')
    return request.get_host().split(':')[0].lower()

def get_tenant(request):
    hostname=get_hostname(request)
    print(hostname,'hh')
    subdomain=hostname.split('.')[0]
    print(subdomain,'subbbb')
    services='apigateway'
    dynamic=dynamic_link(services,'apigateway/user/tenant'+ '/' + str(subdomain))
    print(dynamic,'ddd')
    response=requests.get(dynamic).json()
    print(response,'rrr')
    return response
    # return User.objects.filter(tenant_company=subdomain)