import unittest
from django.test import Client
from django.urls import reverse
from utils.models import Game, Player
from django.contrib.messages import get_messages

class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_gamepicker_view(self):
        response = self.client.get(reverse('intro:gamepicker'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'intro/gamepicker.html')
        self.assertContains(response, 'Game List')

    def test_index_view_with_player_info(self):
        player = Player.objects.create(username='test_player')
        self.client.session['player_id'] = player.id

        response = self.client.get(reverse('intro:index'))
        self.assertRedirects(response, reverse('intro:gamepicker'))

    def test_index_view_without_player_info(self):
        response = self.client.get(reverse('intro:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'intro/index.html')
        self.assertContains(response, 'Welcome to the Game')

    def test_stam_view(self):
        response = self.client.get(reverse('intro:stam'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'intro/testform.html')

    def test_login_player_post_with_empty_username(self):
        response = self.client.post(reverse('intro:loginPlayerPost'), {'username': ''})
        self.assertRedirects(response, reverse('intro:index'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Username is required.')

    def test_login_player_post_with_valid_username(self):
        response = self.client.post(reverse('intro:loginPlayerPost'), {'username': 'test_player'})
        self.assertRedirects(response, reverse('intro:gamepicker'))
        player = Player.objects.get(username='test_player')
        self.assertEqual(self.client.session['player_id'], player.id)

    def test_logout_player(self):
        self.client.session['player_id'] = 1

        response = self.client.get(reverse('intro:logoutPlayer'))
        self.assertRedirects(response, reverse('intro:index'))
        self.assertNotIn('player_id', self.client.session)

if __name__ == '__main__':
    unittest.main()