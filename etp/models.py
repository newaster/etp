from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone


class User_addon(models.Model):
	def __str__(self):
		na= self.user.username +"-"+self.role
		return na

	class Meta():
		unique_together = ('user', 'azones')


			
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobileno = models.CharField(max_length=15)
	company_name = models.CharField(max_length=40)
	location = models.CharField(max_length=20)
	role = models.CharField(max_length=20)
	password_text = models.CharField(max_length=30)
	createdby= models.IntegerField()
	azones=models.CharField(max_length=255)
	quota= models.IntegerField(default=0)



class user_approval(models.Model):

	def __str__(self):
		na = self.username
		return na


	first_name=models.CharField(max_length=15) 
	last_name=models.CharField(max_length=15) 
	username=models.CharField(max_length=15) 
	password=models.CharField(max_length=15)
	email=models.CharField(max_length=15)
	mobileno = models.CharField(max_length=15)
	company_name = models.CharField(max_length=40)
	role = models.CharField(max_length=20)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
   



class site(models.Model):
	def __str__(self):
		na = self.smno
		return na

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=25)
	smno = models.CharField(max_length=25)
	lat = models.CharField(max_length=25)
	lon= models.CharField(max_length=25)
	status= models.CharField(max_length=25)
	opc=models.IntegerField()
	techno= models.CharField(max_length=150)
	techemail= models.CharField(max_length=100)
	city= models.CharField(max_length=25)
	dnt=models.DateTimeField(auto_now_add=True)
	ud=models.DateTimeField(auto_now_add=True)

	def default_vd():
		return datetime.now() + timedelta(days=365)

	vd = models.DateTimeField(default=default_vd)

	dl=models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		delta = self.vd - timezone.now()
		self.dl = delta.days
		super().save(*args, **kwargs)



class zones(models.Model):

	def __str__(self):
		na = self.zname
		return na

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	zname = models.CharField(max_length=55)
	zid=models.CharField(max_length=200)



class fault(models.Model):
	site=models.ForeignKey(site, on_delete=models.CASCADE)
	fname= models.CharField(max_length=100)
	dnt=models.DateTimeField(auto_now_add=True)

class ticket(models.Model):

	uname=models.CharField(max_length=50)
	uemail=models.CharField(max_length=120)
	umob=models.CharField(max_length=20)
	mdate=models.CharField(max_length=50)
	mtime=models.CharField(max_length=50)
	site=models.ForeignKey(site,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Desc=models.CharField(max_length=200,default="")
	status=models.CharField(max_length=10,default="sent")


class etpflow(models.Model):
	def __str__(self):
		na = self.smno+"-"+str(self.dnt)+"-"+self.name
		return na


	dnt=models.DateTimeField(auto_now_add=True)
	smno= models.CharField(max_length=25) 
	name= models.CharField(max_length=25)
	fstatus= models.CharField(max_length=25)
	ib= models.CharField(max_length=25)
	ob= models.CharField(max_length=25) 
	etp= models.CharField(max_length=25) 
	obh= models.CharField(max_length=25) 
	flowvalue=models.DecimalField(max_digits=15, decimal_places=2)
	tot= models.DecimalField(max_digits=15, decimal_places=2) 
	itp1= models.CharField(max_length=25)
	itp2= models.CharField(max_length=25)
	ffp1= models.CharField(max_length=25)
	ffp2= models.CharField(max_length=25)
	b1= models.CharField(max_length=25)
	b2= models.CharField(max_length=25)
	stp1= models.CharField(max_length=25)
	stp2= models.CharField(max_length=25)
	pos= models.CharField(max_length=25)
	nop= models.CharField(max_length=25)
	itpr= models.DecimalField(max_digits=15, decimal_places=2)
	ffpr= models.DecimalField(max_digits=15, decimal_places=2)
	blwrr= models.DecimalField(max_digits=15, decimal_places=2)
	stpr= models.DecimalField(max_digits=15, decimal_places=2)
	itpc= models.DecimalField(max_digits=15, decimal_places=2)
	itp1c= models.DecimalField(max_digits=15, decimal_places=2)
	itp2c= models.DecimalField(max_digits=15, decimal_places=2)
	ffpc= models.DecimalField(max_digits=15, decimal_places=2)
	ffp1c= models.DecimalField(max_digits=15, decimal_places=2)
	ffp2c= models.DecimalField(max_digits=15, decimal_places=2)
	bwlrc= models.DecimalField(max_digits=15, decimal_places=2)
	bwlr1c= models.DecimalField(max_digits=15, decimal_places=2)
	bwlr2c= models.DecimalField(max_digits=15, decimal_places=2)
	stpc= models.DecimalField(max_digits=15, decimal_places=2)
	stp1c= models.DecimalField(max_digits=15, decimal_places=2)
	stp2c= models.DecimalField(max_digits=15, decimal_places=2)
	mpv= models.DecimalField(max_digits=15, decimal_places=2)
	nobkwsh= models.DecimalField(max_digits=15, decimal_places=2)
	itpophr= models.DecimalField(max_digits=15, decimal_places=2)
	itp1ophr= models.DecimalField(max_digits=15, decimal_places=2)
	itp2ophr= models.DecimalField(max_digits=15, decimal_places=2)
	ffpophr= models.DecimalField(max_digits=15, decimal_places=2)
	ffp1ophr= models.DecimalField(max_digits=15, decimal_places=2)
	ffp2ophr= models.DecimalField(max_digits=15, decimal_places=2)
	blwrophr= models.DecimalField(max_digits=15, decimal_places=2)
	blwr1ophr= models.DecimalField(max_digits=15, decimal_places=2)
	blwr2ophr= models.DecimalField(max_digits=15, decimal_places=2)
	stpophr= models.DecimalField(max_digits=15, decimal_places=2)
	stp1ophr= models.DecimalField(max_digits=15, decimal_places=2)
	stp2ophr= models.DecimalField(max_digits=15, decimal_places=2)
	stpserhr= models.DecimalField(max_digits=15, decimal_places=2)
	stpon= models.DecimalField(max_digits=15, decimal_places=2)








