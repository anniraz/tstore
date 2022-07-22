from django.db import models
from django.contrib.auth  import get_user_model

User = get_user_model()
# from django.utils.safestring import mark_safe


class Category(models.Model):

    title=models.CharField(max_length=255)
    parent=models.ForeignKey('self',on_delete=models.CASCADE ,related_name='children', null=True,blank=True)
    slug=models.SlugField( unique=True ,blank=True,null=True)

    def __str__(self):
        return self.title


class Technology(models.Model):

    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    price=models.PositiveIntegerField()
    image =models.ImageField(upload_to='technology/')
    video=models.URLField()
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True,verbose_name='дата публикации')
    slug=models.SlugField(unique=True,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

class Images(models.Model):

    product=models.ForeignKey(Technology,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='technology/')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'





class Characteristics(models.Model):

    techn_name=models.ForeignKey(Technology,on_delete=models.CASCADE ,related_name='characteristics')
    diagonal=models.CharField(max_length=100 ,verbose_name='Диогональ')
    cpu=models.CharField(verbose_name='Процессор', max_length=255)
    operating_system=models.CharField(verbose_name='Операционная система', max_length=255,default='Без операционной системы')
    ram=models.CharField(verbose_name='Объем оперативной памяти',max_length=255)
    hard_disk_type=models.CharField(verbose_name='Тип жесткого диска',max_length=255)
    storage_capacity=models.CharField(verbose_name='Объем накопителя ',max_length=255)
    video_adapter=models.CharField(verbose_name='Видеоадаптер',max_length=255)
    video_adapter_chipset=models.CharField(verbose_name='Чипсет видеоадаптера ',max_length=255)
    video_adapter_memory_size=models.CharField( verbose_name='Объем памяти видеоадаптера', max_length=255)


    def __str__(self):
        return f'{self.techn_name}'



class Reviews(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    
    auth=models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=5000)
    rating = models.IntegerField(choices=RATING ,blank=True, null=True)
    time_pub = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Technology, on_delete=models.CASCADE ,related_name='reviews')
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True ,related_name='children')

    def __str__(self):
        return f"{self.auth} - {self.product} {self.text}"

    class Meta:

        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering=['pk']