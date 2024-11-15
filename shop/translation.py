from modeltranslation.translator import register, TranslationOptions
from .models import ShopMainView


@register(ShopMainView)
class ShopMainViewTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
