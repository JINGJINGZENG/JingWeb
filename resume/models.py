from django.db import models


class Proof(models.Model):  # 荣誉模型
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='证明描述')  # 文字描述
    photo = models.ImageField(upload_to='Proof/',
                              blank=True,
                              verbose_name='证明照片')  # 图片

    class Meta:
        verbose_name = '证明材料'
        verbose_name_plural = '证明材料'
