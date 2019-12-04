from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class JBox(models.Model):
    archive = models.ImageField(_('archive'), upload_to='uploads/')
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(_('description'), blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def __str__(self):
        return self.name

    def show_html(self):
        return format_html("<img src='{}' alt='{}' width='64' height='64' />", self.archive.url, self.archive.name)

    class Meta:
        verbose_name = _('jbox')
        verbose_name_plural = _('jbox')
        ordering = ['-created']
