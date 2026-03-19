from django.db import models

class BasicUnitMeasure(models.TextChoices):
    UNIDADE = "UN", "Unidade"
    CAIXA = "CX", "Caixa"


class ProductType(models.TextChoices):
    INSUMO = "1", "Insumo"
    MATERIA_PRIMA = "2", "Matéria Prima"
    EMBALAGEM = "3", "Embalagem"
    MATERIAL_ACABADO = "4", "Material Acabado"

class Product(models.Model):
    product_code = models.CharField(max_length=20, blank=False, null=False, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    umb = models.CharField(max_length=2, choices=BasicUnitMeasure, default=BasicUnitMeasure.UNIDADE)
    quantity = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    product_type = models.CharField(max_length=2, choices=ProductType)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_code} - {self.name}"
