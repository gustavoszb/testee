from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):

        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
        
        if(self.email == ''):
            self.email = "email nao fornecido"

        resultados= Professor.objects.filter(login=self.login)
        if len(resultados)>0:
            raise Exception('login ja existe')

        
        super(Professor,self).save()




class Disciplina(models.Model):
        nome = models.TextField(max_length=255)
        ementa = models.TextField(max_length=255)
        
        def save(self):
            print('estou salvando!')

            resultados= Disciplina.objects.filter(nome=self.nome)
            if len(resultados)>0:
                raise Exception('nome ja existe')


            super(Disciplina,self).save()




class DisciplinaOfertada(models.Model):
        
        curso= models.TextField(max_length=255)
        ano=models.TextField(max_length=255)
        semestre= models.TextField(max_length=255)
        turma= models.TextField(max_length=255)
        professor= models.TextField(max_length=255)
        disciplina= models.TextField(max_length=255)

        def save(self):

            print('estou salvando!')


            do= ['ADS','SI','BD']
            if not(self.curso in do):
                raise Exception('Curso invalido')
            '''
            t9a1= DisciplinaOfertada.objects.filter(curso=self.curso)
            t9a2= DisciplinaOfertada.objects.filter(ano=self.ano)
            t9a3= DisciplinaOfertada.objects.filter(semestre=self.semestre)
            t9a4= DisciplinaOfertada.objects.filter(turma=self.turma)
            t9a5= DisciplinaOfertada.objects.filter(curso=self.curso)
            if len(t9a1)>0 and len(t9a2)>0 and len(t9a3)>0 and len(t9a4)>0 and len(t9a5)>0:
                raise Exception('Disipina Cadastrada')'''
            
            super(DisciplinaOfertada,self).save()

gu = DisciplinaOfertada()
gu.curso = 'ADS'
gu.ano = '2018'
gu.semestre = '2'
gu.turma = '2C'
gu.professor = '01'
gu.disciplina = '100'
print(gu)