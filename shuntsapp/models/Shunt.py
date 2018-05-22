# -*- coding: utf-8 -*-
"""Clase que representa un Shunt, es decir la unidad de audio que se enviara entre chats o a la historia
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Shunt(models.Model):
    """Modelo shunt con las siguientes propiedades:
    content: Archivo de audio del shunt
    creation_date: Fecha de creacion
    sender: El usuario que envia el shunt
    receiver: El usuario al que se lo envian, None si se envia a la historia
    share_type: Tipo, puede ser CHAT, o HISTORY """

    HISTORY_TYPE = 1
    CHAT_TYPE = 2

    SHUNT_TYPES = (
        (HISTORY_TYPE, _("Historia")),
        (CHAT_TYPE, _('Chat')),
    )

    content = models.FileField(verbose_name=_('Audio'))  # TODO: Añadir validadores
    creation_date = models.DateTimeField(verbose_name=_('Fecha de creacion'), default=timezone.now)
    sender = models.ForeignKey('usersapp.CustomUser', verbose_name=_(u"Propietario"), related_name="shunts",
                                on_delete=models.CASCADE)
    receiver = models.ForeignKey('usersapp.CustomUser', verbose_name=_(u"Receptor"), related_name="received_",
                                  on_delete=models.CASCADE, blank=True, null=True)
    share_type = models.IntegerField(verbose_name=_(u"Tipo de elemento"), choices=SHUNT_TYPES)