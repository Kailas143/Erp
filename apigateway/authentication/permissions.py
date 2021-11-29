
from rest_framework.permissions import BasePermission



from .models import User,Employee,emp_roles


def roles_users(request):
    role_list=[]
    print(request.user.id)
    emp=Employee.objects.filter(employee=request.user.id).first()
    for i in emp.roles.all():
        role_list.append(i.roles)
        print(i.roles)
        print(role_list,'======')
    
    return role_list

class IsRawmaterials(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_employee:
            if 'Rawmaterials' in roles_users(request):
                return True
            else :
                return False


class IsProduction(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_employee:
            print(request)
            if 'Production' in roles_users(request):
                return True
            else :
                return False


class IsJoborder(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_employee:
            print(request)
            if 'Joborder' in roles_users(request):
                return True
            else :
                return False


class IsProduction(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_employee:
            print(request)
            if 'Production' in roles_users(request):
                return True
            else :
                return False
       
