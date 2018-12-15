from django.shortcuts import render, HttpResponse
import json


def mainpage(request):
    database = open('database.json')
    db = database.read()
    database.close()
    db_json = json.loads(db)
    return render(request, 'mainpage.html', {'a': db_json})


def admin(request):
    return render(request, 'admin.html')


def login(request):
    data = open("logs.json").read()
    data = json.loads(data)
    if request.POST:
        for i in data:
            if i['login'] == request.POST.get('username') and i['password'] == request.POST.get('password'):
                database = open('database.json')
                db = database.read()
                database.close()
                db_json = json.loads(db)
                return render(request, "login.html", {'a': db_json})
    return render(request, 'error.html')


def organisation(request):
    if request.POST:
        name = request.POST.get("name")
        database = open('database.json')
        db = database.read()
        database.close()
        db_json = json.loads(db)
        for i in db_json:
            if i["OrganisationName"]==name:
                return render(request, 'organisation.html', {'a': i})

def order(requests):
    if requests.POST:
        name_order = requests.POST.get("order")
        database = open('database.json')
        db = database.read()
        database.close()
        db_json = json.loads(db)
        for num,i in enumerate(db_json):
            if requests.POST.get("OrganisationName") == i['OrganisationName']:
                order_list = i['orders']
                for k,j in enumerate(order_list):
                    print(j["description"]==name_order)
                    if j["description"]==name_order:
                        c = db_json[num]["orders"][k]
                        print(i)
                        return render(requests,"order.html",{'a':c})

def edit(request):
    if request.POST:
        database = open('database.json')
        db = database.read()
        database.close()
        db_json = json.loads(db)
        for num,i in enumerate(db_json):
            if request.POST.get("OrganisationName") == i['OrganisationName']:
                neworder = {
                    "autor": request.POST.get("autor"),
                    "description": request.POST.get("description"),
                    "departuredate": request.POST.get("departuredate"),
                    "enddate":request.POST.get("enddate"),
                    "status": request.POST.get("status")
                }
                db_json[num]["orders"].append(neworder)
                database = open('database.json', 'w').write(json.dumps(db_json))
                return render(request, 'organisation.html', {'a': i})


def error(request):
    return render(request, 'error.html')


def addnew(request):
    if request.POST:
        database = open('database.json')
        db = database.read()
        database.close()
        db_json = json.loads(db)
        new_organisation = {
            "OrganisationName": request.POST.get("OrganisationName"),
            "data": request.POST.get("data"),
            "head": {"name": request.POST.get("name"),
                     "DateOfBirth": request.POST.get("DateOfBirth")},
            "orders": []
        }
        db_json.append(new_organisation)
        database = open('database.json', 'w').write(json.dumps(db_json))
        return render(request, "login.html", {'a': db_json})