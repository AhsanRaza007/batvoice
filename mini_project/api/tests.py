from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from api.models import Transcript
from api.models import Charset
# Create your tests here.


class TrsanscriptValidationTest(APITestCase):

    def setUp(self):
        Charset.objects.create(charset="()'aA-àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûv VwWxXyYzZ", id="1")
        self.create_url = reverse('account-create')
        self.test_user = self.client.post(self.create_url, {'username':'testuser', 'password':'somepassword'})
        self.transcript_url = reverse('transcript-view')

    def test_create_transcript(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': 'ahsan raza.',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);


    def test_charset_valid(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': '1234',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 0);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);

    def test_one_space(self):
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        payload = {'transcription': 'Ahsan  Raza',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 0);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);


    def test_capital(self):
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        payload = {'transcription': 'Aaa AAA aaa.',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);


    def test_create_transcript_with_question_mark(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': 'ahsan raza?',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);

    def test_create_transcript_with_question_mark_followed_by_one_space_and_uppercase_char(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': 'ahsan raza? A',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);

        payload = {'transcription': 'ahsan raza ',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);


    def test_create_transcript_with_smicolon(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': 'ahsan raza; ',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 1);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);

        payload = {'transcription': 'ahsan raza;',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 2);
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);


    def test_create_transcript_without_ending(self):
        user = User.objects.latest('id')

        token = Token.objects.get(user=user)
        payload = {'transcription': 'ahsan raza',
                'audio': './media\\A-01-01.mp3',
                'transcribed': 'true',
                'user': 'raza',
                }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.transcript_url, data=payload, format='json')
        self.assertEqual(Transcript.objects.count(), 0);
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST);
