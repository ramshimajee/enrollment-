from django.shortcuts import render,redirect
from guest.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def login(request):
     return render(request,"guest/login.html") 
def loginaction(request):
    if request.method=="POST":
        print("hai")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if  student_details.objects.filter(username=username , password=password).exists():
            loginobj =  student_details.objects.get(username=username, password=password)
            request.session['username'] = loginobj.username
            request.session['loginid'] = loginobj.studentid 
            request.session['fullname'] = loginobj.fullname
            # print(session['loginid'])
           
            # categoryview = category.objects.all()
            # productview = product.objects.all()
            # context = {'username' : username,'fullname':loginobj.fullname}
            if 'loginid' in request.session:
                # coursedetailsview = course_details.objects.all()
                # subjectdetailsview = subject_details.objects.all()
                # return render(request, 'customer/cusindex.html',{'coursedetails' :coursedetailsview, 'subjectdetails' :subjectdetailsview})
                return redirect('cusindex')
            return render(request,"guest/login.html")
                
        elif admin_log.objects.filter(admin_username=username,admin_password=password).exists():
            print("hi")
            return render(request, 'admin/index.html')
        
        else :
            admin_login= admin_log.objects.last()
            print(admin_login.admin_username,admin_login.admin_password)
            messages.success(request,"CHECK USERNAME OR PASSWORD")
            return render(request,"guest/login.html")
      

def studentregistration(request):
     return render(request,"guest/studentregistration.html") 

def studentregistrationaction(request):
    if request.method=="POST":
       print("hai")
       fullname = request.POST.get('fullname')
       emailid = request.POST.get('email')
       contactno = request.POST.get('contact')
       registerdate = request.POST.get('date')
       address = request.POST.get('address')
       username = request.POST.get('username')
       password = request.POST.get('password')
       
      
       
       studentregform_obj = student_details()
       
       studentregform_obj.fullname = fullname 
       studentregform_obj.email_id = emailid
       studentregform_obj.contact_no = contactno
       studentregform_obj.register_date= registerdate
       studentregform_obj.address=address
       studentregform_obj.username=username
       studentregform_obj.password=password
       
      
       
       
       studentregform_obj.save()
       
       return login(request)  
  
def  studentregistrationview(request):
       studentregistrationview = student_details.objects.all()
       return render(request,"guest/studentregistrationview.html",{'student_details': studentregistrationview}) 
  
def staffdetails(request):
     return render(request,"admin/staffdetails.html") 

def staffdetailsaction(request):
    
    if request.method=="POST":
       print("hai")       
       staffname = request.POST.get('staffname')
       emailid = request.POST.get('email')
       contactno = request.POST.get('contact')
       registerdate = request.POST.get('date')
       qualification = request.POST.get('qualification')
       username = request.POST.get('username')
       password = request.POST.get('password')
    #    registerdate = datetime.strptime(registerdate, '%d/%m/%Y').strftime('%Y-%m-%d')
       
       staffregform_obj = staff_details()
       
       staffregform_obj.staffname =staffname 
       staffregform_obj.email_id= emailid
       staffregform_obj.contact_no =contactno
       staffregform_obj.register_date= registerdate
       staffregform_obj.qualification_details=qualification
       staffregform_obj.username=username
       staffregform_obj.password=password
        
       staffregform_obj.save()
         
       return login(request)
   
def staffdetailsview(request):
       staffdetailsview= staff_details.objects.all()
       return render(request,"admin/staffdetailsview.html",{'staffdetails': staffdetailsview}) 
 
def guestindex(request):
    return render(request,"guest/index.html")
                 
def coursedetails_view(request):
    return render(request,"admin/coursedetails.html") 

def coursedetailsaction(request):
    if request.method == "POST":
        coursename = request.POST.get('coursename')
        coursedescription = request.POST.get('description')  
        courseimage = request.FILES.get('file')  
        
        course_obj = course_details()
        
        course_obj.coursename = coursename
        course_obj.course_description =  coursedescription
        # print(course_obj.course_description)
        course_obj.course_image = courseimage
        
        course_obj.save()
        
        return coursedetailsview(request)
    
def coursedetailsview(request):
    coursedetailsviews= course_details.objects.all()
    print(coursedetailsviews)

    return render(request,"admin/coursedetailsview.html",{'course_details':coursedetailsviews})


def coursedetailsedit(request,id):
    if request.method=="POST":
    
       coursename=request.POST.get('coursename')
       coursedescription=request.POST.get('description')
       courseimage = request.FILES.get('file')
    
       courseedit_obj=course_details.objects.get(course_id=id)
       
       if courseimage:
           courseedit_obj.coursename=coursename
           courseedit_obj.course_description=coursedescription
           courseedit_obj.course_image=courseimage
       
       courseedit_obj.save()
       return coursedetailsview(request)

    else:
        courseedit_obj=course_details.objects.get(course_id=id)
        return render (request,"admin/coursedetailsedit.html",{"edit":courseedit_obj })
    
def coursedetailsdelete(request,id):
    coursedata=course_details.objects.get(course_id=id)
    coursedata.delete()
    messages.success(request,'deleted successfully')
    return coursedetailsview(request)  

def subjectdetails(request):
    coursedetailsview= course_details.objects.all()
    staffdetailsview=staff_details.objects.all()
    return render(request,"admin/subjectdetails.html",{"course_details":coursedetailsview,'staff_details':staffdetailsview})

def subjectdetailsaction(request):
    if request.method == "POST":
        courseid = request.POST.get('courseid')
        staffid= request.POST.get('staffid')
        subjectname = request.POST.get('subjectname') 
        subjectfee = request.POST.get('subjectfee') 
        description  = request.POST.get('description')
        
        subject_obj = subject_details()
        
        subject_obj.course_id = courseid
        subject_obj.staff_id=staffid
        subject_obj.subject_name= subjectname
        subject_obj.subject_fee= subjectfee
        subject_obj.subject_description = description 
       
        subject_obj.save()
        return subjectdetailsview(request)
    
def subjectdetailsview(request):
    # Assuming ForeignKey relationship between GuestCourseDetails and GuestSubjectDetails
    results =  subject_details.objects.select_related('course','staff').all()
    return render(request, "admin/subjectdetailstable.html", {'subjectdetails': results})

def subjectdetailsedit(request,id):
    if request.method == "POST":
        print("id kittunnilla");
        id = request.POST.get('courseid')
        staffid=request.POST.get('staffid')
        subjectname = request.POST.get('subjectname')
        subjectfee = request.POST.get('subjectfee')
        description = request.POST.get('description')

        subjectedit_obj = subject_details.objects.get(subject_id=id)
        
        
        subjectedit_obj.course_id = id
        subjectedit_obj.staff_id = staffid
        subjectedit_obj.subject_name = subjectname
        subjectedit_obj.subject_fee = subjectfee
        subjectedit_obj.subject_description = description

        subjectedit_obj.save()

        return subjectdetailsview(request)

    else:
        print(id);
        subjectedit_obj = subject_details.objects.get(subject_id=id) 
        coursedetailsview = course_details.objects.all()
        staffdetailsview = staff_details.objects.all()
        return render(request, "admin/subjectdetailsedit.html", {"edit": subjectedit_obj, 'coursedetails': coursedetailsview,'staffdetails':staffdetailsview})

    
def subjectdetailsdelete(request,id):
    subjectdata=subject_details.objects.get(subject_id=id)
    subjectdata.delete()
    messages.success(request,'deleted successfully')
    return subjectdetailsview(request)    
    
    
def enrolleddetails(request):
     coursedetailsview = course_details.objects.all()
     staffdetailsview = subject_details.objects.all()
     studentregistrationview=student_details.objects.all()
     return render(request,"customer/enrolleddetails.html",{'course_details':coursedetailsview,'subject_details':staffdetailsview,'student_details':studentregistrationview}) 
 
def enrolleddetailsaction(request,id):
    if request.method == "GET":
        studentid = request.session['loginid']
        subject  = id
        date = timezone.now().date()
        status = "Enrolled"
        
        enrolled_obj = enrolled_details()
        
        enrolled_obj.student_id= studentid
        enrolled_obj.subject_id= subject
        enrolled_obj.register_date = date 
        enrolled_obj.status = status
        enrolled_obj.save()
        
        return enrolleddetailsview(request)
    
    
def enrolleddetailsview(request):
    results =  enrolled_details.objects.select_related('student','subject').all()
    for status in results :
        enrolled_status = status.status
        print(enrolled_status)
    return render(request, "admin/enrolleddetailstable.html", {'enrolleddetails': results})


def cusindex(request):
    if 'loginid' in request.session:
       coursedetailsview = course_details.objects.all()
       subjectdetailsview = subject_details.objects.all()
            
       # Redirect to the home page if the value doesn't exist
       return render(request,"customer/cusindex.html",{'coursedetails' :coursedetailsview, 'subjectdetails' :subjectdetailsview})
       # return render(request,"guest/login.html")
    return render(request,"guest/login.html") 
   
def getsubjectview(request, id):
    # Fetch course details
    coursedetailsview = course_details.objects.all()
    # print('hi')

    # Retrieve session information
    username = request.session.get('username')
    customerid = request.session.get('loginid')
    subjectDetails = subject_details.objects.filter(course=id)
    if customerid:
        return render(request, "customer/getsubjectview.html",{"subjectdetails":subjectDetails})
    # If no customer ID is found, redirect to the guest index page
    return render(request, "guest/index.html")

def subjectviewmore(request, id):
    # Fetch course details
    coursedetailsview = course_details.objects.all()

    # Define and execute the SQL query using Django ORM with JOIN between tables
    sql_query = """
        SELECT * 
        FROM guest_course_details c
        INNER JOIN guest_subject_details s 
        ON c.course_id = s.course_id
        WHERE c.course_id = %s;
    """
    subjectdetailsview = subject_details.objects.raw(sql_query, [id])

    # Pass both course and subject details to the template
    return render(request, "customer/subjectviewmore.html", {
        'coursedetails': coursedetailsview,
        'subjectdetails': subjectdetailsview
    })

def addtoenrolled(request,id):
       enrolled_status = "Admitted"
       enrolled_details_obj = enrolled_details.objects.get(enrollmentid=id)
       enrolled_details_obj.status = enrolled_status
       enrolled_details_obj.save() 
            
       return enrolleddetailsview(request)
   
def addtoenrollment(request,id): 
       enrolled_status  = "Deactivate"
       enrolled_details_obj = enrolled_details.objects.get(enrollmentid=id)
       enrolled_details_obj.status = enrolled_status
       enrolled_details_obj.save() 
        
       return enrolleddetailsview(request)

