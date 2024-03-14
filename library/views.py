from django.shortcuts import*
from django.contrib.auth import*
from .models import*
from django.db.models import F

def index(request):
    return render(request,"index.html")


def logboth(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=authenticate(request,username=username1,password=password1)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return redirect(admnlog)
        elif user is not None and user.is_staff==0 and user.is_active==1:
            login(request,user)
            return redirect(studlog)
        else:
            error="Invalid username / password"
            return HttpResponse(error)
    else:
      return render(request,"login.html")

def regform(request):
    if request.method=='POST':
        name1=request.POST['fname']
        name2=request.POST['lname']
        e=request.POST['email']
        admno=request.POST['admissionNo']
        u=request.POST['username']
        if User.objects.filter(username=u).exists():
           return HttpResponse("username already exists..please Try another one username...")
        p=request.POST['password']
        User.objects.create_user(first_name=name1,last_name=name2,email=e,admission_number=admno,username=u,password=p)
        return redirect(logboth)
    else:
        return render(request,'regform.html')
    

def admnlog(request):
    return render(request,'admnlog.html')


def addbook(request):
    if request.method=='POST':
        bookid=request.POST['book_id']
        bookname=request.POST['book_name']
        authrname=request.POST['author_name']
        quantity=request.POST['quantity']
        x=Add_Book.objects.create(Book_id=bookid,Book_name=bookname,Author_name=authrname,Quantity=quantity)
        x.save()
        return render(request,'addbook.html')
    else:
       return render(request,'addbook.html')
    
def view_admbook(request):
    x=Add_Book.objects.all()
    return render(request,'viewbook.html',{"view":x})


def update_book(request):
    x=Add_Book.objects.all()
    return render(request,'updatebook.html',{"view":x})


def both_logout(request):
    logout(request)
    return redirect(logboth)

def book_search(request):
    if request.method=='POST':
        b_id=request.POST['book_id']
        x=Add_Book.objects.get(Book_id=b_id)
        return render(request, 'view.html',{'view':x})
    else:
        x=Add_Book.objects.all()
    return render(request,'updatebook.html',{"view":x})

def book_edit(request,Book_id):
 if request.method=='POST':
    b_id=request.POST['book_id']
    b_name=request.POST['book_name']
    b_authname=request.POST['author_name']
    b_quantity=request.POST['book_quantity']
    data=Add_Book.objects.filter(Book_id=Book_id)
    data.update( Book_id= b_id,Book_name=b_name,Author_name=b_authname,Quantity=b_quantity)
    return redirect(book_search)
 else:
    obj=Add_Book.objects.get(Book_id=Book_id)
    return render(request,"editbook.html",{'view': obj})
 
def deletebook(request,id):
    x=Add_Book.objects.get(id=id)
    x.delete()
    return redirect(book_search)

def studlog(request):
    if request.method=='POST':
        b_name=request.POST['book_name']
        x=Add_Book.objects.get(Book_name=b_name)
        return render(request, 'viewstud.html',{'view':x})
    else:
       x=Add_Book.objects.all()
    return render(request,'studlog.html',{"data":x})

def view_studbook(request):
  x=Student_Book.objects.filter(user=request.user)
  return render(request,'viewbookstud.html',{"view":x})

def order_book(request):
    if request.method=='POST':
        b_name=request.POST['book_name']
        x=Add_Book.objects.get(Book_name=b_name)
        return render(request, 'orderdetials.html',{'view':x})
      
    else:

        x=Add_Book.objects.all()
    return render(request,'orderplace.html',{"data":x})

def order_bookdetials(request):
    if request.method=="POST":
        b_name=request.POST['book_name']
        a_name=request.POST['auther_name']
        s_name=request.POST['stud_name']
        b_id=request.POST['book_id']
        s_id=request.POST['stud_id']
        x=Student_Book.objects.create( book_name=b_name,stud_name=s_name,author_name=a_name,book_id=b_id,user_id=s_id,issue_date=None,expiry_date=None)
        x.save()
        return redirect(order_book)
    
    else: 
     return redirect(order_book)
    
def adm_view_order(request):
    x=Student_Book.objects.all()
    return render(request,"adm_view_order.html",{"data":x})


def adm_confirmation(request,id,book_id):
    if request.method =='POST':
        obj=Student_Book.objects.get(pk=id)
        if obj != None:
            i_date=request.POST['issue_date']
            e_date=request.POST['expiry_date']
            fine=request.POST['fine']
            confirm=request.POST['confirm']
            Student_Book.objects.filter(pk=id).update(issue_date=i_date,expiry_date=e_date,fine=fine,confirm=confirm)
            Add_Book.objects.filter(Book_id=book_id).update(Quantity=F('Quantity') - 1)
            obj=Add_Book.objects.get(Book_id=book_id)
            a=int(obj.Quantity)
           
            if  a <= 0 :
                  Add_Book.objects.filter(Book_id=book_id).update(Quantity="out of stock")
                
            return redirect(adm_view_order)
    else:
        obj=Student_Book.objects.get(pk=id)
      
        return render(request,"adm_order_confirmation.html",{'data': obj})

def view_dateinfo(request):
    x=Student_Book.objects.filter(user=request.user,confirm=True)
    return render(request,'stud_dateinfo_view.html',{'Books':x})

def stud_return_book(request,book_id,id):
    Add_Book.objects.filter(Book_id=book_id).update(Quantity=F('Quantity') + 1)
    obj=Student_Book.objects.get(id=id)
    obj.delete()
    return redirect(view_dateinfo)

