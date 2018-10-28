from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import pymysql
from web.models import message
from django.db.models import Q
pymysql.install_as_MySQLdb()

# Create your views here.
def index(request):
    return HttpResponse('Hello!')
def table(request):
    return render(request,'table.html')
def get_data(sql):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='uJU1tqx_8Kd>',
                           db='text',
                           port=3306,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results= cur.fetchall()
    cur.close()
    conn.close()
    return results
def tz(request):
    sql = '''SELECT id,time,title,url from tongzhi'''
    m_data = get_data(sql)
    return render(request, 'table.html', {'tz': m_data})
def search(request):
    q = request.GET.get('q','')
    message_list= message.objects.filter(title__icontains=q)
    return render(request, 'search.html',{'message_list': message_list})