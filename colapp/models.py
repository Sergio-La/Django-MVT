from django.db import models
#Modelo estudiante
class estudiante(models.Model):
    id = models.AutoField(primary_key = True)
    est_cod = models.IntegerField()
    est_nom = models.CharField(max_length=20)
    est_ap = models.CharField(max_length=20)
    est_cur = models.CharField(max_length=5)
    
    def __str__(self):
        return '{0},{1}'.format(self.est_ap,self.est_nom)

#Modelo profesor
class profesor(models.Model):
    id = models.AutoField(primary_key = True)
    pro_cod = models.IntegerField()
    pro_nom = models.CharField(max_length=20)
    pro_ap = models.CharField(max_length=20)
    pro_are = models.CharField(max_length=15)
    
    def __str__(self):
        return '{0},{1}'.format(self.pro_ap,self.pro_nom)
        
#Modelo materia
class materia(models.Model):
    id = models.AutoField(primary_key = True)
    ma_cod = models.IntegerField()
    ma_nom = models.CharField(max_length=20)
    
    def __str__(self):
        return '{0}'.format(self.ma_nom)

#Modelo salones
class salones(models.Model):
    id = models.AutoField(primary_key = True)
    sal_cod = models.IntegerField()
    sal_nom = models.CharField(max_length=20)
    sal_cur = models.CharField(max_length=20)
    
    def __str__(self):
        return '{0}'.format(self.sal_nom)        
        