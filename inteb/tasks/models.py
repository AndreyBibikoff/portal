from django.db import models
from staff.models import IntebUser

class IntebTasks(models.Model):
    # NEW = 'NEW'
    # IN_WORK = 'IN_WORK'
    # PAUSE = 'PAUSE'
    # COMPLETE = 'COMPLETE'
    # FAIL = 'FAIL'
    #
    # STATUS_CHOICES = (
    #     (NEW, 'Новая'),
    #     (IN_WORK, 'В работе'),
    #     (PAUSE, 'Пауза'),
    #     (COMPLETE, 'Завершено'),
    #     (FAIL, 'Невозможно выполнить'),
    # )

    author = models.ForeignKey(IntebUser, related_name='task_author', null=False, db_index=True, on_delete=models.PROTECT)
    topic = models.CharField(verbose_name='тема', max_length=64, )
    text = models.TextField(verbose_name='текст')
    # is_active = models.BooleanField(default=True)
    # create = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
    # update = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True, blank=True)
    # deadline = models.DateTimeField(verbose_name='дедлайн', blank=True)
    # status = models.CharField(verbose_name='статус', max_length=30, choices=STATUS_CHOICES)



class Executors(models.Model):
    task = models.ForeignKey(IntebTasks, related_name='task_executor', on_delete=models.CASCADE)
    executor = models.ForeignKey(IntebUser, related_name='user_executor', null=False, on_delete=models.PROTECT)
    create = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
    update = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True, blank=True)

# class TaskComment(models.Model):
#     task = models.OneToOneField(IntebTasks, related_name='task_comment', on_delete=models.CASCADE)
#     author = models.OneToOneField(IntebUser, related_name='comment_author', null=False,
#                                           on_delete=models.PROTECT)
#     comment_text = models.TextField(verbose_name='текст коммента')
#     create = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
#     update = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True, blank=True)
#
#
# class TaskPictures(models.Model):
#     task = models.OneToOneField(IntebTasks, related_name='task_picture', blank=True, on_delete=models.CASCADE)
#     author = models.OneToOneField(IntebUser, related_name='picture_author', null=False,
#                                           on_delete=models.PROTECT)
#     picture = models.ImageField(blank=True)
#     create = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
#     update = models.DateTimeField(verbose_name='дата редактирования', auto_now_add=True, blank=True)