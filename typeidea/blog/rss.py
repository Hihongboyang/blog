from typing import Dict, Any
from xml.sax.handler import ContentHandler
from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.safestring import SafeText
from .models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler: ContentHandler, item: Dict[str, Any]) -> None:
        return super().add_item_elements(handler, item)

class LatestPostFeed(Feed):
    feed_type = Rss201rev2Feed
    title = "Typeidea Blog System"
    link = "/rss/"
    description = "typeidea is a blog system power by django"

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]
        
    def item_title(self, item: Model) -> SafeText:
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item: Model) -> str:
        return reverse('post-detail', args=[item.pk])

    def item_extra_kwargs(self, item: Model) -> Dict[Any, Any]:
        return {'content_html': self.item_content_html(item)}
    
    def item_content_html(self, item):
        return item.content_html

    
