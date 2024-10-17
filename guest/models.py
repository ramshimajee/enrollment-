from django.db import models

class student_details(models.Model):
    studentid = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)   
    email_id = models.CharField(max_length=50) 
    contact_no = models.CharField(max_length=50)    
    register_date= models.DateField()
    address= models.TextField()
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    
    def __str__(self):
        return self.fullname
    
class admin_log(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=100)  
    admin_password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.admin_username
    
class staff_details(models.Model):
    staffid = models.AutoField(primary_key=True)  
    staffname = models.CharField( max_length=50)
    email_id = models.CharField( max_length=50)  
    contact_no= models.CharField(max_length=50)
    register_date= models.DateField()
    qualification_details=models.CharField(max_length=50)
    username = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.staffname
    
class course_details(models.Model):
    course_id = models.AutoField(primary_key=True)
    coursename = models.CharField( max_length=50) 
    course_description= models.TextField()  
    course_image = models.ImageField(upload_to='images/') 
    
    def __str__(self):
        return self. coursename
    
class subject_details(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField( max_length=50)
    course = models.ForeignKey(course_details, on_delete=models.CASCADE, null=True, blank=True)
    staff =models.ForeignKey(staff_details, on_delete=models.CASCADE, null=True, blank=True)
    subject_fee=models.BigIntegerField()
    subject_description= models.TextField() 
    
    def __str__(self):
        return self.subject_name
    
class enrolled_details(models.Model):
    enrollmentid = models.AutoField(primary_key=True)  
    student = models.ForeignKey(student_details, on_delete=models.CASCADE,null=True, blank=True)
    subject= models.ForeignKey(subject_details, on_delete=models.CASCADE,null=True, blank=True)
    register_date= models.DateField()
    status= models.CharField(max_length=100)
    
    def __str__(self):
        return self.register_date
     

     
    

    

      
