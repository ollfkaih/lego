from rest_framework import status

import lego.apps.events.tests.test_events_api as event_api
from lego.apps.events.models import Event
from lego.apps.tags.models import Tag
from lego.apps.users.models import User
from lego.utils.test_utils import BaseAPITestCase


class TagsTestCase(BaseAPITestCase):
    fixtures = ["test_abakus_groups.yaml", "test_tags_data.yaml", "initial_tags.yaml"]

    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_authenticate(user)

    def test_add_existing_tag(self):
        pk = 1
        event = self.client.get(event_api._get_detail_url(pk))
        event_data = event.json()
        del event_data["cover"]
        # Make sure that we're not adding a tag which is there already.
        # The simplest way to do this is to ensure that the event has no tags.
        self.assertEquals(len(event_data.pop("tags")), 0)
        tag = Tag.objects.first()
        event_data["tags"] = [tag.tag]
        res = self.client.put(event_api._get_detail_url(pk), event_data)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTrue(tag.tag in res.json().pop("tags"))

    def test_remove_tag(self):
        pk = 2
        event = self.client.get(event_api._get_detail_url(pk))
        event_data = event.json()
        del event_data["cover"]
        tags = event_data.pop("tags")
        removed = tags.pop()
        event_data["tags"] = tags
        res = self.client.put(event_api._get_detail_url(pk), event_data)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertFalse(removed in res.json().pop("tags"))

    def test_add_duplicate_tag(self):
        pk = 2
        event = self.client.get(event_api._get_detail_url(pk))
        event_data = event.json()
        del event_data["cover"]
        tags = event_data.pop("tags") or []
        self.assertTrue(len(tags) > 0)
        event_data["tags"] = tags + tags
        total_tags_before = Tag.objects.count()
        res = self.client.put(event_api._get_detail_url(pk), event_data)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        total_tags_after = Tag.objects.count()
        self.assertEquals(total_tags_before, total_tags_after)
        self.assertEquals(res.json()["tags"], tags)

    def test_add_new_tag(self):
        pk = 1
        event = self.client.get(event_api._get_detail_url(pk))
        event_data = event.json()
        del event_data["cover"]

        tag = "ayyy-totaly-unique123"
        self.assertIsNone(Tag.objects.filter(tag=tag).first())

        event_data["tags"] = [tag]
        res = self.client.put(event_api._get_detail_url(pk), event_data)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTrue(tag in res.json().pop("tags"))
        self.assertIsNotNone(Tag.objects.filter(tag=tag).first())

    def test_add_invalid_tags(self):
        pk = 1
        event = self.client.get(event_api._get_detail_url(pk))
        event_data = event.json()

        event_data["tags"] = ["invalid tag with space"]
        response = self.client.patch(event_api._get_detail_url(pk), event_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_preserve_tags(self):
        """Preserve tags when no tags is posted"""
        event = Event.objects.get(pk=1)
        tag = Tag.objects.create(pk="test-tag")
        event.tags.add(tag)

        response = self.client.get(event_api._get_detail_url(event.pk))
        event_data = response.json()

        del event_data["cover"]
        del event_data["tags"]
        response = self.client.patch(event_api._get_detail_url(event.pk), event_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            list(event.tags.values_list("pk", flat=True)), response.json()["tags"]
        )
        self.assertEquals(len(response.json()["tags"]), 1)

    def test_clear_tags(self):
        """Clear tags when [] is posted"""
        event = Event.objects.get(pk=1)
        response = self.client.get(event_api._get_detail_url(event.pk))
        event_data = response.json()

        del event_data["cover"]
        event_data["tags"] = []
        response = self.client.patch(event_api._get_detail_url(event.pk), event_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        event.refresh_from_db()
        self.assertEquals(list(event.tags.values_list("pk", flat=True)), [])
