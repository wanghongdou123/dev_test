from django.db import models
from personal.models.project import Project



class Module(models.Model):
    """
    ---模块表
    """
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    # 删除项目时，模块随之删除；
    name = models.CharField("名称",max_length=50, null=False)
    describe = models.TextField("描述",default="GE")
    # 自动获取当前时间
    create_time = models.DateTimeField("创建时间",auto_now_add=True)


    def __str__(self):
        return self.name