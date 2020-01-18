from django.db import models

# Create your models here.

class Openess(models.Model):
    openess_type = models.CharField(max_length=20)
    def __str__(self):
        return self.openess_type

class Product(models.Model):
    product_type = models.CharField(max_length=200)
    def __str__(self):
        return self.product_type

class ScreenColor(models.Model):
    screen_color = models.CharField(max_length=200)
    def __str__(self):
        return self.screen_color

class Frame(models.Model):
    frame_color = models.CharField(max_length=200)
    def __str__(self):
        return self.frame_color

class Custom(models.Model):
    custom_type = models.CharField(max_length=200)
    def __str__(self):
        return self.custom_type

class AngleBuildOut(models.Model):
    angle_build_out = models.CharField(max_length=200)
    def __str__(self):
        return self.angle_build_out

class SafetyDrive(models.Model):
    safety_drive = models.CharField(max_length=200)
    def __str__(self):
        return self.safety_drive

class Radio(models.Model):
    radio = models.CharField(max_length=20)
    def __str__(self):
        return self.radio

class Remotes(models.Model):
    remotes = models.CharField(max_length=20)
    def __str__(self):
        return self.remotes

class Helper(models.Model):
    helper = models.CharField(max_length=5)
    def __str__(self):
        return self.helper

class Extreme(models.Model):
    extreme = models.CharField(max_length=5)
    def __str__(self):
        return self.extreme

class VinylPanels(models.Model):
    vinyl_panels = models.CharField(max_length=200)
    def __str__(self):
        return self.vinyl_panels

class Mortar(models.Model):
    mortar = models.CharField(max_length=5) 
    def __str__(self):
        return self.mortar   

