from django.db import models

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(str):
    	return self.title

    #class Meta:
        #managed = False
        #db_table = 'language'


class Timezone(models.Model):
    timezone_id = models.AutoField(primary_key=True)
    timezone_name = models.CharField(max_length=64, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'timezone'

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=64)
    skill_description = models.CharField(max_length=64, blank=True, null=True)

    #class Meta:
    #    managed = False
    #    db_table = 'skill'


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    manager_lname = models.CharField(max_length=64, blank=True, null=True)
    manager_fname = models.CharField(max_length=64, blank=True, null=True)

    #class Meta:
    #    managed = False
    #    db_table = 'manager'

class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resource_lname = models.CharField(max_length=64)
    resource_fname = models.CharField(max_length=64)
    timezone_id = models.ForeignKey(Timezone, db_column='timezone_id', on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language, db_column='language_id', on_delete=models.CASCADE)

    #class Meta:
    #    managed = False
    #    db_table = 'resource'


class ResourceSkill(models.Model):
    resource_id = models.ForeignKey(Resource, db_column='resource_id', on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, db_column='skill_id', on_delete=models.CASCADE)
    resource_skill_level = models.DecimalField(max_digits=1, decimal_places=0, null=True)

    class Meta:
    #    managed = False
        unique_together = (("resource_id", "skill_id"),)
    #    db_table = 'resource_skill'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(Manager, db_column='manager_id', on_delete=models.CASCADE)
    project_description = models.CharField(max_length=64, blank=True, null=True)

    #class Meta:
    #    managed = False
    #    db_table = 'project'


class ProjectTeam(models.Model):
    project_id = models.ForeignKey(Project, db_column='project_id', on_delete=models.CASCADE)
    resource_id = models.ForeignKey(Resource, db_column='resource_id', on_delete=models.CASCADE)

    class Meta:
        #managed = False
        unique_together = (("resource_id", "project_id"),)
        #db_table = 'project_team'