from django.test import TestCase

from django.contrib.auth.models import User

from . models import Post


class BlogTest(TestCase):
    @classmethod

    def SetUpTestData(cls):

        testuser1=User.objects.create_user(
            username='testuser1',password='anihortes')
        testuser1.save()

        test_post=Blog.objects.create(
        author=testuser1,title='blog title',body='blog content'
        )
        test_post.save()


    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f'{post.author}'
        title=f'{post.title}'
        body=f'{post.body}'
        
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'blog title')
        self.assertEqual(body,'blog content')
# Create your tests here.
