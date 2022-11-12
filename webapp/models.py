from django.db import models
STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nazvanie')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='active', verbose_name='Status')
    email_author = models.EmailField(max_length=30, verbose_name='E-mail')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data Sozdaniya")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data Izmeneniya")
    content = models.TextField(max_length=2000, verbose_name='Opisanie')


    def __str__(self):
        return f"{self.pk}, {self.title}, {self.status}, {self.email_author}, {self.content}, {self.created_at}, {self.updated_at}"

    class Meta:
        db_table = "guestbook"
        verbose_name = "Запись"
        verbose_name_plural = "Записи"