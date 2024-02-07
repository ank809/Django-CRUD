from django.db import models

# Create your models here.
class Cars(models.Model):
    car_name=models.CharField(max_length=30)
    model= models.CharField(max_length=20)
    engine=models.CharField(max_length=20)
    speed=models.IntegerField()
    description=models.TextField()
    seats= models.IntegerField()
    color= models.CharField(max_length=20)
    sunroof=models.BooleanField()

''' Open the terminal run command  --> python manage.py shell (this will open django shell)
A) CREATE

1. Create object of Cars class
car= Cars(car_name='Toyota Corolla',
    model='2021',
    engine='Inline-4',
    speed=150,
    description='A compact sedan known for its reliability.',
    seats=5,
    color='Silver',
    sunroof=False)
2. car.save()
3. To see the result run -> car

Another way 

1. car= Cars.objects.create(car_name='Toyota Corolla',
     model='2021',
     engine='Inline-4',
     speed=150,
     description='A compact sedan known for its reliability.',
     seats=5,
     color='Silver',
    sunroof=False)

By this method you do not have to save it will automatically save

B) Read
1. To get the name of the car with id 1 (django automatically adds a unique id to each object)
Cars.objects.all()[0].car_name 
Or
Cars.objects.get(id=1).car_name        --->If the id is not found it will five error
Or
Cars.objects.filter(id=1)              ---> It will not give you any error if the id does not exist and return an empty list

C) Update

1. update car_name to toyota where id =1
It will only update the car_name to toyota where id =1 not anywhere else
car=Cars.objects.get(id=1)
car.car_name="Toyota"
car.save()


2. Update the car_name to Toyota Corolla in all the places where where car_name is Toyota
Update function updates at multiple locations
Cars.objects.filter(car_name="Toyota").update(car_name="Toyota Corolla")

3. Delete
delete the car where id =1
Cars.objects.get(id=1).delete()

To delete all the data
Cars.objects.all().delete()

'''