from django.db import models

from django_hana import column_store, row_store


class SimpleModel(models.Model):
    char_field = models.CharField(max_length=100)

    class Meta:
        app_label = 'test_dhp'


class ComplexModel(models.Model):
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=100)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField()
    file_path_field = models.FilePathField(path='/home/foobar/')
    float_field = models.FloatField()
    image_field = models.ImageField()
    integer_field = models.IntegerField()
    generic_ip_address_field = models.GenericIPAddressField()
    null_boolean_field = models.NullBooleanField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

    class Meta:
        app_label = 'test_dhp'


class RelationModel(models.Model):
    to_one_field = models.ForeignKey(ComplexModel)
    to_many_field = models.ManyToManyField(ComplexModel)

    class Meta:
        app_label = 'test_dhp'


@column_store
class SimpleColumnModel(models.Model):
    char_field = models.CharField(max_length=50)

    class Meta:
        app_label = 'test_dhp'


@row_store
class SimpleRowModel(models.Model):
    char_field = models.CharField(max_length=50)

    class Meta:
        app_label = 'test_dhp'
