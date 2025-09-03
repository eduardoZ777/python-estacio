from tortoise import fields, models

class PeriodoLetivo(models.Model):
    id = fields.IntField(pk=True)
    ano = fields.IntField() # ano que pode ser 2020, 2025
    semestre = fields.IntField() # semestre que pode ser 1 ou 2
    data_inicio = fields.DateField()
    data_fim = fields.DateField()

    class Meta:
        table = "periodos_letivos"
        unique_together = (("ano", "semestre"),)
        indexes = (("ano", "semestre"),)

class Professor(models.Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField
    Disciplina = fields.ManyToManyField("models.Disciplina", related_name="professores", through="professor_disciplinas")
    cpf = fields.CharField(max_length=14, unique=True)
    Turma = fields.ForeignKeyField("models.Turma", related_name="professores")
    email = fields.CharField(max_length=100, unique=True)
    numero_de_contato = fields.CharField
    
    

class Curso(models.Model):
    nome = fields.CharField(max_length=100)
    alunos = fields.IntField()  
    id = fields.IntField(pk=True)
    Disciplina = fields.ManyToManyField("models.Disciplina", related_name="cursos", through="curso_disciplinas")

    


class Disciplina(models.Model):
    Professor = fields.ForeignKeyField("models.Professor", related_name="disciplinas")
    Aluno = fields.ManyToManyField("models.Aluno", related_name="disciplinas", through="aluno_disciplinas")
    horario = fields.CharField(max_length=50) 
    notas = fields.JSONField()  

    

class Matriz(models.Model):
    Curso = fields.ForeignKeyField("models.Curso", related_name="matrizes")
    ano = fields.IntField()  
    semestre = fields.IntField()  
    Disciplinas = fields.ManyToManyField("models.Disciplina", related_name="matrizes", through="matriz_disciplinas")
    id = fields.IntField(pk=True)
class Turma(models.Model):
    Professor = fields.ForeignKeyField("models.Professor", related_name="turmas")
    Disciplina = fields.ForeignKeyField("models.Disciplina", related_name="turmas")
    PeriodoLetivo = fields.ForeignKeyField("models.PeriodoLetivo", related_name="turmas")
    Aluno = fields.ManyToManyField("models.Aluno", related_name="turmas", through="matriculas")
    numero_turma = fields.CharField(max_length=10)  
    sala = fields.CharField(max_length=20)  
    
class Aluno(models.Model):
 id = felds.IntField(pk=True)
Turma = fields.ForeignKeyField("models.Turma", related_name="alunos")
turno = fields.CharField(max_length=20)  
nome = fields.CharField(max_length=100)
idade = fields.IntField()
numero_matricula = fields.CharField(max_length=20, unique=True)
numero_de_contato = fields.CharField(max_length=15)
email = fields.CharField(max_length=100, unique=True)


class Matricula(models.Model):
    nomeCompleto = fields.CharField(max_length=100)
    id = fields.IntField(pk=True)
    data_matricula = fields.DateField()
    rg = fields.CharField(max_length=20)
    cpf = fields.CharField(max_length=14, unique=True)
    curso = fields.ForeignKeyField("models.Curso", related_name="matriculas")
    periodo_letivo = fields.ForeignKeyField("models.PeriodoLetivo", related)
    dataDeNascimento = fields.DateField()

                                            
class Historico(models.Model):
    notas = fields.JSONField()  
    presencas = fields.JSONField()  
    faltas = fields.IntField()  
    atividades_concluidas = fields.IntField() 
    atividades_pendentes = fields.IntField()  
    advertencias = fields.IntField() 