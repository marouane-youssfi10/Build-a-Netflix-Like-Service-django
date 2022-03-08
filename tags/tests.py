from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.db.utils import IntegrityError
from .models import TaggedItem
from playlists.models import Playlist

class TaggedItemTestCase(TestCase):
    def setUp(self):
        self.ply_obj = Playlist.objects.create(title='New title')
        # self.tag_a = TaggedItem.objects.create(tag='my-new-tag')

    def test_content_type_is_not_null(self):
        with self.assertRaises(IntegrityError):
            TaggedItem.objects.create(tag='my-new-tag')

    def test_create_via_content_type(self):
        c_type = ContentType.objects.get(app_label='playlists', model='playlist')
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=1, tag='new-tag')
        self.assertIsNotNone(tag_a.pk)
        tag_a = TaggedItem.objects.create(content_type=c_type, object_id=100, tag='new-tag2')
        self.assertIsNotNone(tag_a.pk)