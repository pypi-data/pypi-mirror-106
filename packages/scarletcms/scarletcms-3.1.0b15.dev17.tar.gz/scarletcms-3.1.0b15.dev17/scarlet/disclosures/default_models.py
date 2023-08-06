"""
This file can be copied into a project's app folder as models.py for
default implementation of disclosure models.
"""
from django.db import models
from scarlet.disclosures.models import BaseGlossaryTerm, BaseGlossaryDisclosure
from scarlet.versioning.models import Cloneable


class GlossaryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().prefetch_related("glossarydisclosures")


class GlossaryTerm(Cloneable, BaseGlossaryTerm):
    objects = GlossaryManager

    def __str__(self):
        return self.keyword


class GlossaryDisclosure(Cloneable, BaseGlossaryDisclosure):

    def __str__(self):
        return self.title
