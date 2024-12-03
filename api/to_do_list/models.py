from django.db import models

class ToDoList(models.Model):
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'to_do_list' 

    def __str__(self):
        return self.task_name