from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            email="test@email.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Amazing body',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEquals(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEquals(f'{self.post.title}', 'A good title')
        self.assertEquals(f'{self.post.author}', 'user')
        self.assertEquals(f'{self.post.body}', 'Amazing body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Amazing body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "New title")
        self.assertContains(response, "New text")

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEquals(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEquals(response.status_code, 302)


