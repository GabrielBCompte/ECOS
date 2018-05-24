import datetime
from django.shortcuts import render
from usersapp.models.CustomUser import CustomUser
from shuntsapp.models.Shunt import Shunt


def yesterday():
    """Función que devuelve el dia anterior a hoy, exactamente 24 horas antes"""
    return datetime.datetime.now() - datetime.timedelta(days=1)


def user_history_shunts_view(user_pk):
    """Función que deveulve los shunts de la historia de un 
    usuario concreto ordenando por fecha(primero el mas reciente)
    @:param user_pk(int): PK del usuario del qual sacar la historia
    @:returns (dictionary list): Lista de diccionarios con el siguiente formato 
        {'audio': Contenido del shunt}
    """

    query_list = Shunt.objects.filter(share_type=Shunt.HISTORY_TYPE,
                                      sender__pk=user_pk,
                                      creation_date__gte=yesterday()).order_by('creation_date')

    json_list = [{'audio': shunt.content} for shunt in query_list]

    return json_list


def chat_view(receiver_pk, sender_pk):
    """Función que deveulve los shunts de un char entre dos usuarios 
       ordenando por fecha(primero el mas reciente)
        @:param reciever_pk(int): pk del reciever(usuario con el cual se ha abierto chat)
        @:param sender_pk(int): pk del sender(usuario en el mobil)
        @:returns (dictionary list): Lista de diccionarios con el siguiente formato 
            {'audio': Contenido del shunt
            'owner': Propietario del shunt(el que lo ha enviado)}
        """
    query_list = Shunt.objects.filter(share_type=Shunt.CHAT_TYPE,
                                      sender__pk__in=[receiver_pk, sender_pk],
                                      receiver__pk__in=[receiver_pk, sender_pk],
                                      creation_date__gte=yesterday()).order_by('creation_date')

    json_list = [{'audio': shunt.content,
                  'owner': shunt.sender,
                  } for shunt in query_list]

    return json_list


