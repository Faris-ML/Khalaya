from django.shortcuts import render
import requests
from datetime import date
import hashlib
from Apps.Web.apps import WebConfig


# Create your views here.
user = {'auth':False}
error = {'error':''}
def home(request):
    error['error']=''
    return render(request, 'index.html',user)

def result(request):
    error['error'] = ''
    input = str(request.GET['input'])
    rest_api_url = ' https://u47snfxcw6.execute-api.eu-west-1.amazonaws.com/Test/arabiclanguageanalysis'
    response = requests.post(url = rest_api_url, json = {"text":input}, headers = {'content-type': 'application/json'})
    res = response.json()
    data = WebConfig.db['Text_data_predicted']
    res['text'] = input
    data.insert_one(res)
    return render(request,'sss.html',res)

def sign_in(request):
    error['error'] = ''
    return render(request,'sign_in.html',error)
def sign_in_data(request):
    cln = WebConfig.db['Clients']
    auths = WebConfig.db['Authentication']
    id = cln.find_one({'Email':request.GET['Email']}).get('_id')
    auth_info = {'Client_id':id,'authentication_key': hashlib.sha256((request.GET['Email']+request.GET['Password']).encode('UTF-8')).hexdigest()}
    if auths.find_one(auth_info) != None:
        c = cln.find_one({'Email': request.GET['Email']})
        user['auth'] = True
        user['First_name'] = c.get('First_name')
        user['Last_name'] = c.get('Last_name')
        user['Email'] = c.get('Email')
        user['Phone_number'] = c.get('PhoneNo')
        user['Creat_date'] = c.get('Creat-Date')
        error['error']=''
        return render(request, "index.html",user)
    else:
        error['error']='password or email are wrong'
        return render(request,"sign_in.html",error)
def sign_up(request):
    error['error']=''
    return render(request,"sign_up.html",error)
def sign_up_data(request):

    cln = WebConfig.db['Clients']
    auths = WebConfig.db['Authentication']

    fn = request.GET['First_name']
    ln = request.GET['Last_name']
    email = request.GET['Email']
    pswd = request.GET['Password']
    cpswd = request.GET['cPassword']
    phone = request.GET['Phone_number']

    if cpswd.strip() != pswd.strip():
        error['error'] = 'password and the confirmed password dont match'
        return render(request, "sign_up.html", error)

    if cln.find_one({'Email':email}) != None:
        error['error'] = 'email is already used'
        return render(request, "sign_up.html", error)

    new_user = {
        "First_name": fn,
        "Last_name":ln,
        "Email": email,
        "PhoneNo":phone,
        "Creat-Date": date.today().strftime("%d/%m/%Y")
    }
    cln.insert_one(new_user)
    new_user_auth = {
        'Client_id': cln.find_one(new_user).get('_id'),
        'authentication_key': hashlib.sha256((email+pswd).encode('UTF-8')).hexdigest()
    }
    auths.insert_one(new_user_auth)
    error['error'] = ''
    return render(request,"sign_in.html")

def sign_out(request):
    user['auth']=False
    error['error'] = ''
    return render(request, "index.html", user)

def account(request):
    error['error'] = ''
    return render(request, "account.html", user)

def account_edit(request):
    return render(request,"account_edit.html",user)

def account_edit_data(request):
    return render(request, "account.html", user)