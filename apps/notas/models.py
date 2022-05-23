from django.db import models

# Create your models here.

class Note(models.Model):

    """

    Attributes:
        title = Titulo de la nota
        description = Descripcion de la nota
        create = fecha de creacion de la nota
        archived = si la nota esta archivada
        deleted = si la nota esta eliminada digitalmente
        deleted_datetime = fecha cuando se elimino digitalmente la nota
    """

    title =  models.CharField(max_length=255, blank=True)
    description = models.TextField(blank = True)
    create = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:

        """Clase que usa Django para configurar el modelo.

        docs: https://docs.djangoproject.com/en/4.0/ref/models/options/

        Attributes:
            verbose_name = Un nombre legible por humanos para el objeto, en singular.
            verbose_name_plural = El nombre plural del objeto.
            ordering = El orden predeterminado para el objeto, para usar al obtener listas de objetos, puede ser por mas de un atributo, asd o desc
            permissions = Permisos adicionales para ingresar en la tabla de permisos al crear este objeto.
        """
        
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ["create"]