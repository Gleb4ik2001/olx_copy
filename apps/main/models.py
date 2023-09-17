from django.db import models

class Products(models.Model):
    NON_CATEGORY = 'Не указано'
    HOME = 'HM'
    CLOTHES = 'CLTHS'
    SCHOOL = 'SCHL'
    DACHA = 'DCH'
    KIDS_FOR = 'KDSFR'
    EDUCATION = 'DCTN'
    CATOGORIES_CHOISES = [
        (NON_CATEGORY,'Без категории'),
        (HOME,'Для дома'),
        (CLOTHES,'Одежда'),
        (SCHOOL,'Школа'),
        (DACHA,'Дача'),
        (KIDS_FOR,'Для детей'),
        (EDUCATION,'Образование'),
    ]
    title = models.CharField(
        verbose_name='название товара',
        max_length=200,
        null=False
    )
    photo = models.ImageField(
        verbose_name='фото',
        upload_to='media/photos',
        null=True,
        blank=True
    )
    price = models.PositiveIntegerField(
        verbose_name='цена(KZT)'
    )
    category = models.CharField(
        verbose_name='категория',
        choices=CATOGORIES_CHOISES,
        default=NON_CATEGORY,
        max_length=10
    )
    description = models.TextField(
        verbose_name='описание'
    )

    def __str__(self) -> str:
        return f'{self.title}: KZT{self.price}. Category: {self.category}'
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title',)
