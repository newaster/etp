from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import User_addon, user_approval,etpflow,fault,site,zones,ticket,UserProfile,credithistory
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .vdata import data_parse
from django.utils import timezone
from django.db.models import Max, OuterRef, Subquery
import ast
from django.db.models import Sum
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import base64
import os 

def viewraw(request):
    with open('etpraw.txt', 'r') as fp:
        lines = fp.readlines()

    last_5000_records = lines[-5000:][::-1]

    return render(request,'viewdata.html',{'context': last_5000_records})

def viewpolish(request):
    with open('etppolished.txt', 'r') as fp:
        lines = fp.readlines()

    last_5000_records = lines[-5000:][::-1]

    return render(request,'viewdata.html',{'context': last_5000_records})




def faultfunc(user):
    faults = fault.objects.filter(site__user=user).order_by('-dnt')[:6]

    return faults


def logout_call(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def newetp(request):
    if request.method == 'POST':
        nd= request.POST.get('Data')
        with open('etpraw.txt', 'a') as fp:
            fp.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -- {dict_data}\n")

        if nd[-1]=='e':
            dict_data=nd
        else:
            dict_data=data_parse(nd)
        remote_addr = request.META.get('REMOTE_ADDR')
        with open('etppolished.txt', 'a') as fp:
            fp.write(f" {remote_addr}-- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -- {dict_data}\n")

        ef = etpflow(smno=dict_data['smno'], name=dict_data['name'], fstatus=dict_data['fstatus'], ib=dict_data['ib'], ob=dict_data['ob'], etp=dict_data['etp'], obh=dict_data['obh'], flowvalue=float(dict_data['flowvalue']), tot=float(dict_data['tot']), itp1=dict_data['itp1'], itp2=dict_data['itp2'], ffp1=dict_data['ffp1'], ffp2=dict_data['ffp2'], b1=dict_data['b1'], b2=dict_data['b2'], stp1=dict_data['stp1'], stp2=dict_data['stp2'], pos=dict_data['pos'], nop=dict_data['nop'], itpr=float(dict_data['itpr']), ffpr=float(dict_data['ffpr']), blwrr=float(dict_data['blwrr']), stpr=float(dict_data['stpr']), itpc=float(dict_data['itpc']),itp1c=float(dict_data['itp1c']),itp2c=float(dict_data['itp2c']), ffpc=float(dict_data['ffpc']),ffp1c=float(dict_data['ffp1c']),ffp2c=float(dict_data['ffp2c']), bwlrc=float(dict_data['bwlrc']),bwlr1c=float(dict_data['bwlr1c']),bwlr2c=float(dict_data['bwlr2c']), stpc=float(dict_data['stpc']),stp1c=float(dict_data['stp1c']),stp2c=float(dict_data['stp2c']), mpv=float(dict_data['mpv']), nobkwsh=float(dict_data['nobkwsh']), itpophr=float(dict_data['itpophr']),itp1ophr=float(dict_data['itp1ophr']),itp2ophr=float(dict_data['itp2ophr']), ffpophr=float(dict_data['ffpophr']),ffp1ophr=float(dict_data['ffp1ophr']),ffp2ophr=float(dict_data['ffp2ophr']), blwrophr=float(dict_data['blwrophr']),blwr1ophr=float(dict_data['blwr1ophr']),blwr2ophr=float(dict_data['blwr2ophr']), stpophr=float(dict_data['stpophr']),stp1ophr=float(dict_data['stp1ophr']),stp2ophr=float(dict_data['stp2ophr']), stpserhr=float(dict_data['stpserhr']), stpon=float(dict_data['stpon']))
        ef.save()

    return HttpResponse(status=200)




def home(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']

        if u=="" or p=="":
            return HttpResponse("<script>alert('Invalid Username or Password');window.location.assign('/');</script>")

        else:
            try:
                selUser = authenticate(username=u, password=p)
            except:
                return render(request, 'error.html')

        if selUser:
            login(request, selUser)

            uObj = User_addon.objects.get(user__username=request.user)
            if uObj.role == "admins":
                return redirect('admins/')
            elif uObj.role == "user":
                return redirect('user/')
            elif uObj.role == "guest":
                return redirect('guest/')
        else:
            return HttpResponse("<script>alert('Incorrect Username or Password');window.location.assign('/');</script>")

    return render(request, 'index.html')



def common_view(request, smno,s):
    bardict = {}
    bardict2 = {}
    bardict3 = {}
    result2=[0,0,0,0]
    result=[0,0,0,0]
    lates=""
    
    result = etpflow.objects.filter(smno=smno).aggregate(
        total1=Sum('itp1ophr'),
        total2=Sum('itp2ophr'),
        total3=Sum('ffp1ophr'),
        total4=Sum('ffp2ophr'),
        total5=Sum('stp1ophr'),
        total6=Sum('stp2ophr'),
        total7=Sum('blwr1ophr'),
        total8=Sum('blwr2ophr')
    )
    
    bardict["sum_value1"] = result.get('total1', 0) or 0
    bardict["sum_value2"] = result.get('total2', 0) or 0
    bardict["sum_value3"] = result.get('total3', 0) or 0
    bardict["sum_value4"] = result.get('total4', 0) or 0
    bardict["sum_value5"] = result.get('total5', 0) or 0
    bardict["sum_value6"] = result.get('total6', 0) or 0
    bardict["sum_value7"] = result.get('total7', 0) or 0
    bardict["sum_value8"] = result.get('total8', 0) or 0

    result2 = etpflow.objects.filter(smno=smno).order_by('-dnt')[:7]
    bardict2["itp1ophr"] = [int(i.itp1ophr) / 10 for i in result2]
    bardict2["itp2ophr"] = [int(i.itp2ophr) / 10 for i in result2]
    bardict2["ffp1ophr"] = [int(i.ffp1ophr) / 10 for i in result2]
    bardict2["ffp2ophr"] = [int(i.ffp2ophr) / 10 for i in result2]
    bardict2["blwr1ophr"] = [int(i.blwr1ophr) / 10 for i in result2]
    bardict2["blwr2ophr"] = [int(i.blwr2ophr) / 10 for i in result2]
    bardict2["stp1ophr"] = [int(i.stp1ophr) / 10 for i in result2]
    bardict2["stp2ophr"] = [int(i.stp2ophr) / 10 for i in result2]

    #bardict3["itp1"]=( bardict["sum_value1"] /(bardict["sum_value1"]+ bardict["sum_value2"]) )*100

    if result2:
        if len(result2)>0:
            lates=result2[0]
        else:
            lates=""
    
    return render(request, 'main.html', {'faults': faultfunc(request.user), 'site': s, 'bardict': bardict, 'bardict2': bardict2, 'latest':lates})

@login_required(login_url='/')
def admin(request):
    current_time = timezone.now()
    time_threshold = current_time - timezone.timedelta(hours=24)
    faults = fault.objects.filter(dnt__gte=time_threshold).order_by('-dnt')[:6]
    s = site.objects.all()
    nsmno = s.first().smno

    if request.method == 'POST':
        nsmno = request.POST['siteid']

    return common_view(request, nsmno,s)

@login_required(login_url='/')
def user(request):
    s = site.objects.filter(user=request.user)
    try:
        nsmno = s.first().smno
    except:
        nsmno=""

    if request.method == 'POST':
        nsmno = request.POST['siteid']


    return common_view(request, nsmno,s)

@login_required(login_url='/')
def guest(request):
    siteallocated = []
    noofzone = User_addon.objects.get(user=request.user).azones
    if noofzone != "":
        try:
            si = ast.literal_eval(zones.objects.get(zname=noofzone).zid)

            for i in si:
                newsite = site.objects.get(smno=i[:10])
                siteallocated.append(newsite)

        except:
            return HttpResponse("<script>alert('Zone Not Assigned');window.location.assign('/guest/');</script>")

    s = siteallocated
    nsmno = s[0].smno

    if request.method == 'POST':
        nsmno = request.POST['siteid']

    return common_view(request, nsmno,s)


def signup_call(request):
    if request.method=='POST':
        fname=request.POST['nm1']
        lname=request.POST['nm2']
        email=request.POST['email']
        username1=request.POST['usrname']
        password=request.POST['pwd']
        mobileno1=request.POST['mobileno']


        company_name=request.POST['cname']

        role="user"

        check=User.objects.filter(username=username1)
        check2 =user_approval.objects.filter(username=username1)

        
        if check or check2:
            return HttpResponse("<script>alert('Username Already exist!');window.location.assign('/signup/');</script>")
        else:
            u = user_approval(first_name=fname, last_name=lname, username=username1, password=password, email=email,mobileno=mobileno1,company_name=company_name,role=role)
            u.save()
            return HttpResponse("<script>alert('Account sent for Approval!'); window.location.assign('/');</script>")
            return redirect('/')


    return render(request,'signup.html')

@login_required(login_url='/')
def approval(request):
    subject="Account Created!!"

    allapproval=user_approval.objects.all()

    if request.method=='POST':
        uname=request.POST['username']
        approve_user=user_approval.objects.get(username=uname)

        u = User(first_name=approve_user.first_name, last_name=approve_user.last_name, username=approve_user.username, password=make_password(approve_user.password), email=approve_user.email)
        u.save()
        up = User_addon(user=u,mobileno=approve_user.mobileno,company_name=approve_user.company_name,role=approve_user.role,password_text=approve_user.password,createdby=1)
        up.save()

        user_approval.objects.filter(username=uname).delete()


        html_message = render_to_string('../templates/signup_notification.html', {'u':u,'addon':up})
        mailinput=plain_message = strip_tags(html_message)

        send_mail(subject,mailinput,EMAIL_HOST_USER,[u.email],fail_silently=False,html_message=html_message)


    return render(request,'approval.html',{'all':allapproval})



def privacy(request):

    return render(request,'privacy.html')

@login_required(login_url='/')
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If UserProfile object does not exist, create a new one
        user_profile = UserProfile(user=request.user)

    if request.user.user_addon.role=='user':
        credit=credithistory.objects.filter(usr=request.user).order_by("-dnt")
    else:
        credit=""


        
    if request.method=="POST":
        profile_photo = request.FILES.get('profile_picture')

        #print(profile_photo)

        if profile_photo:
            
            user_profile.profile_picture = profile_photo

            # Rename the file
            file_extension = os.path.splitext(profile_photo.name)[1]
            new_filename = f"{request.user.first_name}_profile_picture{file_extension}"
            user_profile.profile_picture.name = new_filename

            user_profile.save()
            
        return redirect('profile')


    return render(request,'profile.html',{"credit":credit})

@login_required(login_url='/')
def hmi(request):
    latest_etp_flow = etpflow.objects.filter(smno='9100000011').latest('id')
    
    return render(request,'hmi.html',{'etp_flow': latest_etp_flow})

@login_required(login_url='/')
def hmi_view(request):

    latest_etp_flow = etpflow.objects.filter(smno='9100000011').latest('id')

    # Prepare the data to be returned
    data = {
        'ib': latest_etp_flow.ib,
        'ob': latest_etp_flow.ob,
        'etp': latest_etp_flow.etp,
        'pos': latest_etp_flow.pos,
        'nop': latest_etp_flow.nop,
    }

    return JsonResponse(data)

@login_required(login_url='/')
def faultreport(request):
    g=True
    freportlist=[]
    siteallocated=[]
    
    freport = fault.objects.filter(site__user=request.user)
    asite = site.objects.filter(user=request.user)

    if request.user.username=='Admin':
        freport=fault.objects.all()
        asite=site.objects.all()

    

    
    if request.user.user_addon.role=='guest':
        g=False
        freport=freportlist
       
        noofzone=User_addon.objects.get(user=request.user).azones
        if noofzone!="":
            try:        
                si=ast.literal_eval(zones.objects.get(zname=noofzone).zid)                

                for i in si:
                    newsite=site.objects.get(smno=i[:10])
                    siteallocated.append(newsite)

                    ns=fault.objects.filter(site__smno=i[:10]).order_by('-dnt')[:1]
                    
                    freportlist.append(ns)

                #print(freport)

                freport=freportlist


            except:
                return HttpResponse("<script>alert('Zone Not Assigned');window.location.assign('/guest/');</script>")

        asite=siteallocated

    


    if request.method=="POST":
        sid=request.POST['siteid']
        fromd=request.POST['fromdate']
        tod=request.POST['todate']

        if fromd!="" and tod!="":
            fromdate=datetime.strptime(request.POST['fromdate'], '%Y-%m-%d')
            todate=datetime.strptime(request.POST['todate'], '%Y-%m-%d')
            freport = fault.objects.filter(site__smno=sid, dnt__range=(fromdate, todate)).order_by('-dnt')

        else:
            freport=fault.objects.filter(site__smno=sid).order_by('-dnt')

        
        
        return render(request,'faultreport.html',{'faults':faultfunc(request.user),'fr':freport,'site':asite,'post':True,'g':g})


    

    return render(request,'faultreport.html',{'faults':faultfunc(request.user),'fr':freport,'site':asite,'g':g})


@login_required(login_url='/')
def plantreport(request):
    preportlist=[]
    siteallocated=[]
    
    
    s=site.objects.filter(user=request.user)
    if request.user.username=='Admin':
        s = site.objects.all()
    for i in s:
        a = etpflow.objects.filter(smno=i.smno).order_by('-dnt')[:1]
        preportlist.append(a)

    preport=preportlist

    
    if request.user.user_addon.role=='guest':
       
        noofzone=User_addon.objects.get(user=request.user).azones
        if noofzone!="":
            try:        
                si=ast.literal_eval(zones.objects.get(zname=noofzone).zid)                

                for i in si:
                    newsite=site.objects.get(smno=i[:10])
                    siteallocated.append(newsite)

                    ns=etpflow.objects.filter(smno=i[:10]).order_by('-dnt')[:1]
                    
                    preportlist.append(ns)

                preport=preportlist


            except:
                return HttpResponse("<script>alert('Zone Not Assigned');window.location.assign('/guest/');</script>")

        s=siteallocated

    if request.method=="POST":
        sid=request.POST['siteid']
        fromd=request.POST['fromdate']
        tod=request.POST['todate']
        
        if fromd!="" and tod!="":
            fromdate=datetime.strptime(request.POST['fromdate'], '%Y-%m-%d')
            todate=datetime.strptime(request.POST['todate'], '%Y-%m-%d')
            preport = etpflow.objects.filter(smno=sid, dnt__range=(fromdate, todate)).order_by('dnt')

        else:
            preport=etpflow.objects.filter(smno=sid).order_by('dnt')

        
        
        return render(request,'plantreport.html',{'faults':faultfunc(request.user),'pr':preport,'site':s,'post':True})

        

    return render(request,'plantreport.html',{'faults':faultfunc(request.user),'pr':preport,'site':s})

@login_required(login_url='/')
def createsite(request):
    subject="New Site Added to your Account!!"
    szone=zones.objects.filter(user=request.user)
    if request.method=="POST":
        sitename=request.POST['sitename']
        smno=request.POST['smno']

        try:
            if request.user.user_addon.quota==0:
                return HttpResponse("<script>alert('Zero Credit Left Contact Support!');window.location.assign('/createsite/');</script>")

            if site.objects.get(smno=smno):
                return HttpResponse("<script>alert('Modem Number Already exist!');window.location.assign('/createsite/');</script>")



        except:
            lat=request.POST['lat']
            lon=request.POST['lon']
            city=request.POST['city']
            status=request.POST['status']
            phone=request.POST['phone'] 
            email=request.POST['email']
            opc=request.POST['opc']
            dropdown=request.POST['zdropdown']           


            if dropdown=="yes":
            
                zoid=request.POST['zname']

                z1=zones.objects.get(id=zoid)
                a=z1.zid
                a1=a[:-1]+","+"'"+smno+"-"+sitename+"'"+a[-1]
                z1.zid=a1
                z1.save()

            s=site(user=request.user,name=sitename,smno=smno,lat=lat,lon=lon,status=status,techno=phone,techemail=email,city=city,opc=opc)
            s.save()

            ruser=User_addon.objects.get(user=request.user)
            ruser.quota=ruser.quota-1
            ruser.save()

            c=credithistory(usr=request.user,desc="Create Site : "+s.smno,status="-1")
            c.save()

            html_message = render_to_string('../templates/site_notification.html', {'s': s,'u':request.user})
            mailinput=plain_message = strip_tags(html_message)

            send_mail(subject,mailinput,EMAIL_HOST_USER,[request.user.email],fail_silently=False,html_message=html_message)


            return HttpResponse("<script>alert('Wow You created a site!');window.location.assign('/managesite/');</script>")





    return render(request,'createsite.html',{'faults':faultfunc(request.user),'zo':szone})


@login_required(login_url='/')
def managesite(request):
    managesite=site.objects.filter(user=request.user)

    return render(request,'managesite.html',{'faults':faultfunc(request.user),'ms':managesite})


@login_required(login_url='/')
def editsite(request,id):

    esite=site.objects.get(id=id)
    if request.method=="POST":
        sitename=request.POST['sitename']
        lat=request.POST['lat']
        lon=request.POST['lon']
        city=request.POST['city']
        status=request.POST['status']
        phone=request.POST['phone'] 
        email=request.POST['email']
        opc=request.POST['opc']

        e=site.objects.get(id=id)
        e.name=sitename
        e.lat=lat
        e.lon=lon
        e.city=city
        e.status=status
        e.techno=phone
        e.techemail=email
        e.opc=opc
        e.save()
        return HttpResponse("<script>alert('Site Updated Successfully!');window.location.assign('/managesite/');</script>")        

    return render(request,'createsite.html',{'faults':faultfunc(request.user),'edit':True,'es':esite})


@login_required(login_url='/')
def renewsite(request,id):
    if request.user.user_addon.quota==0:
        return HttpResponse("<script>alert('Zero Credit Left Contact Support!');window.location.assign('/createsite/');</script>")
    else:
        ruser=User_addon.objects.get(user=request.user)
        ruser.quota=ruser.quota-1
        ruser.save()

        rsite=site.objects.get(id=id)

        c=credithistory(usr=request.user,desc="Renew Site : "+rsite.smno,status="-1")
        c.save()

        rsite.ud = datetime.now()
        rsite.vd = rsite.vd + timedelta(days=365)
        rsite.save()

    
    return redirect('managesite')



@login_required(login_url='/')
def createuser(request):
    zo=zones.objects.filter(user=request.user)
    if request.method=='POST':
        fname=request.POST['nm1']
        lname=request.POST['nm2']
        email=request.POST['email']
        username1=request.POST['usrname']
        password=request.POST['pwd']
        mobileno1=request.POST['mobileno']
        azone=request.POST['azone']


        seluser=User.objects.get(username=request.user.username)
        seluser2=User_addon.objects.get(user=seluser)
        company_name=seluser2.company_name

        role="guest"

        check=User.objects.filter(username=username1)
        check2 =user_approval.objects.filter(username=username1)

        
        if check or check2:
            return HttpResponse("<script>alert('Username Already exist!');window.location.assign('/createuser/');</script>")
        else:
            u = User(first_name=fname, last_name=lname, username=username1, password=make_password(password), email=email)
            u.save()
            up = User_addon(user=u,mobileno=mobileno1,company_name=company_name,role=role,password_text=password,createdby=seluser.id,azones=azone)
            up.save()

            return redirect('/user/')

    return render(request,'createuser.html',{'faults':faultfunc(request.user),'z':zo})


@login_required(login_url='/')
def manageuser(request):
    muser=User_addon.objects.filter(createdby=request.user.id)
    muser_ids = muser.values_list('user', flat=True)
    muser2 = User.objects.filter(id__in=muser_ids)



    return render(request,'manageuser.html',{'faults':faultfunc(request.user),'mu':muser2})


@login_required(login_url='/')
def edituser(request,id):
    zo=zones.objects.filter(user=request.user)
    euser=User.objects.get(id=id)
    nuser=User_addon.objects.get(user=euser)
    if request.method=='POST':
        fname=request.POST['nm1']
        lname=request.POST['nm2']
        email1=request.POST['email']
        password1=request.POST['pwd']
        



        u=User.objects.get(id=id)
        u.first_name=fname
        u.last_name=lname
        u.email=email1


        if password1!="":
            u.password=make_password(password1)
        u.save()

        u1=User_addon.objects.get(user__id=id)

        if request.user.username!="Admin":
            azone=request.POST['azone']            
            u1.azones=azone

        if password1!="":
            u1.password_text=password1  

        if request.user.username=="Admin":
            nq=request.POST['quota']
            u1.quota=nq

        u1.save() 
            
        return redirect('/manageuser/')

    return render(request,'createuser.html',{'faults':faultfunc(request.user),'edit':True,'eu':euser,'z':zo,'aszone':nuser.azones})



@login_required(login_url='/')
def createzone(request):

    nosites=site.objects.filter(user=request.user)
    if request.method=='POST':
        z=request.POST['zonename']
        s=request.POST.getlist('sites')    
        
    
        newzone=zones(user=request.user,zname=z,zid=s)
        newzone.save()
        return HttpResponse("<script>alert('Wow You created a zone!');window.location.assign('/managezone/');</script>")




    return render(request,'createzone.html',{'faults':faultfunc(request.user),'nos':nosites})


@login_required(login_url='/')
def managezone(request):
    mzone=zones.objects.filter(user=request.user)

    return render(request,'managezone.html',{'faults':faultfunc(request.user),'mz':mzone})


@login_required(login_url='/')
def editzone(request,id):
    nosites=site.objects.filter(user=request.user)
    ezone=zones.objects.get(id=id)
    if request.method=='POST':
        z=request.POST['zonename']
        s=request.POST.getlist('sites')

        z1=zones.objects.get(id=id)
        z1.zname=z
        z1.zid=s
        z1.save()

        return redirect('/managezone/')


    return render(request,'createzone.html',{'faults':faultfunc(request.user),'edit':True,'ez':ezone,'nos':nosites})


@login_required(login_url='/')
def createticket(request):
    subject="New Ticket for Maintenance"

    csites=site.objects.filter(user=request.user)
    if request.method=="POST":
        c=request.POST["cname"]
        s=request.POST["site"]
        p=request.POST["phone"]
        e=request.POST["email"]
        d=request.POST["date"]
        t=request.POST["time"]


        newsite=site.objects.get(id=s)
        ct=ticket(uname=c,uemail=e,umob=p,mdate=d,mtime=t,site=newsite,user=request.user)
        ct.save()


        html_message = render_to_string('../templates/maintenance_notification.html', {'machine': newsite,'maintenance_date':d ,'maintenance_time': t,'cname':c,})
        mailinput=plain_message = strip_tags(html_message)

        send_mail(subject,mailinput,EMAIL_HOST_USER,[e],fail_silently=False,html_message=html_message)

        return HttpResponse("<script>alert('Ticket Created!');window.location.assign('/manageticket/');</script>")



    return render(request,'createticket.html',{'faults':faultfunc(request.user),'s':csites})


@login_required(login_url='/')
def manageticket(request):

    mticket=ticket.objects.filter(user=request.user)

    return render(request,'manageticket.html',{'faults':faultfunc(request.user),'mt':mticket})


@login_required(login_url='/')
def editticket(request,id):

    if request.method=="POST":
        json_data = json.loads(request.body)
        t=ticket.objects.get(id=id)
        t.Desc=json_data['description']
        t.status=json_data['status']
        t.save()

        return JsonResponse({'message': 'Description updated successfully.'})


    return render(request,'createticket.html',{'faults':faultfunc(request.user),'edit':True})





@login_required(login_url='/')
def addcredit(request,id):

    if request.method=="POST":
        print("aaya")
        json_data = json.loads(request.body)
        t=User_addon.objects.get(id=id)
        t.quota=json_data['quota']
        t.save()

        usr=User_addon.objects.get(id=id)

        c=credithistory(usr=usr.user,desc="Purchased Credit",status="+"+json_data['quota'])
        c.save()

        return JsonResponse({'message': 'Credit Added successfully.'})


    return redirect("admins")