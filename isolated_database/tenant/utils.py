from django.db import connection

def hostname_from_request(request):
    return request.get_host().split(':')[0].lower()

def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    tenant_map = get_tenant_map()
    print(tenant_map.get(hostname),hostname)
    return tenant_map.get(hostname)    

def get_tenant_map():
    return {
        'dilshad.school.local': 'dilshad',
        'vipin.school.local': 'vipin'
    }