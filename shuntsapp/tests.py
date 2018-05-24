from django.test import TestCase
from shuntsapp.models.CustomUser import CustomUser
from shuntsapp.models.Shunt import Shunt


class ShuntsappTestCase(TestCase):

    def setUp(self):
        user_1 = CustomUser.objects.create_user(
            username='UserTest1',
            email='test@gmail.com',
            password='testpassword',
            phone_number='600788156'
        )

        user_2 = CustomUser.objects.create_user(
            username='UserTest2',
            email='test2@gmail.com',
            password='testpassword2',
            phone_number='600788180'
        )

    def test_users_are_created_correcty(self):
        user_1 = CustomUser.objects.get(name='UserTest1')
        self.assertEqual(user_1.email, 'test@gmail.com', msg='El correo no se ha asignado correctamente')
        self.assertEqual(user_1.phone_number, '600788156', msg='El numero de telefono no se ha asignado correctamente')
