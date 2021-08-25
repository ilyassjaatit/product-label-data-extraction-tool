from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductRawData(models.Model):
    """Raw data of a product
    Attributes:
        name (str): name
        sources (list): The source of the data can only be: web scraping, manual input, Reading labels
        row_data (json): product data
        is_processed (bool):  If the data obtained is processed
        is_validate (bool): if the data is validated
    """

    WEB_SCRAPING = "WE"
    MANUAL_INPUT = "MI"
    READING_LABELS = "RL"
    SOURCES_CHOICES = [
        (WEB_SCRAPING, _("web scraping")),
        (MANUAL_INPUT, _("manual input")),
        (READING_LABELS, _("Reading labels")),
    ]
    name = models.CharField(max_length=256, null=False)
    geeks_field = models.CharField(max_length=2, choices=SOURCES_CHOICES, default=MANUAL_INPUT)
    raw_data = models.JSONField()
    is_processed = models.BooleanField(default=False)
    is_validate = models.BooleanField(default=False)


class Product(models.Model):
    """Product information
    Attributes:
        name (str): name
        product_row_data (ProductRowData): relation one to many
    """

    name = models.CharField(max_length=256, null=False)
    product_raw_data = models.ForeignKey(ProductRawData, on_delete=models.CASCADE, null=True)
