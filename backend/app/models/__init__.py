from tortoise import fields, models

class PeriodoLetivo(models.Model):
    id: int = fields.IntField(pk=True)
    ano: int = fields.IntField()
    semestre: int = fields.IntField()
    data_inicio: datetime = fields.DateField()
    data_fim: datetime = fields.DateField()


    class Meta:
        table = "periodo_letivo"
        unique_together = (("ano", "semestre"),
                           )

    