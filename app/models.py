from platform import machine
from pyexpat import model
from uuid import uuid4
from django.db import models

# Create your models here.
class Machine(models.Model):
    GP_CHOICE = (
        ("Peito","Peito"),
        ("Biceps", "Biceps"),
        ("Triceps", "Triceps"),
        ("Costas", "Costas"),
        ("pos_perna","Posterior de Perna"),
        ("Perna", "Perna")
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=500, null=False, blank=False, unique=True)
    gp_foco = models.CharField(max_length=500,null=False, blank=False,choices=GP_CHOICE, default=GP_CHOICE[0][0])
    gp_aux = models.CharField(max_length=500,null=True, blank=True, choices=GP_CHOICE, default=GP_CHOICE[0][0])

    def __str__(self) -> str:
        return f"{self.name}"

class Set(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_date = models.DateTimeField( auto_now_add=True,
                                        auto_now=False,
                                        null=False,
                                        blank=False)
    machine = models.ForeignKey(to=Machine, verbose_name="Machine", related_name="Machine", on_delete=models.CASCADE)
    reps = models.ManyToManyField(to="Rep",blank=True, related_name='Rep', )
    def __str__(self) -> str:
        return f"{self.machine}"

class Rep(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    weight =  models.PositiveIntegerField(default=0)
    set = models.ForeignKey(to=Set, on_delete=models.CASCADE, related_name="Sets", verbose_name="Sets")
    qtd = models.PositiveIntegerField(default=8)
    created_date = models.DateTimeField( auto_now_add=True,
                                        auto_now=False,
                                        null=False,
                                        blank=False)
    def __str__(self) -> str:
        return f" {self.weight} KG"

class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_date = models.DateTimeField( auto_now_add=True,
                                        auto_now=False,
                                        null=False,
                                        blank=False)
    sets = models.ManyToManyField(to="Set",blank=True, related_name='Set', )
    ...