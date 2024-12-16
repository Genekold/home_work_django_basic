from django.core.cache import cache

from blogs.models import Blog
from config.settings import CACHE_ENABLED


def get_blog_from_cache():
    """Функция получает список блогов из кэш, если кэш пуст, получит данные из базы данных"""
    if not CACHE_ENABLED:
        return Blog.objects.all()

    name_key = 'blogs_list'
    blogs = cache.get(name_key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.all()
    cache.set(name_key, blogs)
    return blogs
