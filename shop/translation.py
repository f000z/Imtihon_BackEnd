from modeltranslation.translator import register, TranslationOptions
from .models import ShopMainView, Furniture


@register(ShopMainView)
class ShopMainViewTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Furniture)
class FurnitureTranslationOptions(TranslationOptions):
    fields = ('name',)
