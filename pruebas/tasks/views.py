from rest_framework.views import APIView
from pruebas.utils import set_schema, CONNECTION_DETAILS
from django.http import HttpResponse
from tasks.models import Task
import psycopg2

class Env(APIView):
    
    def get(self, request, *args, **kwargs):
        con = psycopg2.connect(**CONNECTION_DETAILS)
        cur = con.cursor()
        if (kwargs.get("change_schema") != None):
            data = Task.objects.all().values()
            return HttpResponse(data)
        else:
            cur.execute("SELECT * FROM auth_group;")
            data = cur.fetchall()
            cur.close()
            con.close()
            return HttpResponse(data)
