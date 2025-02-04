from django.db import models
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from service.snippets import SocialPage, VideoSection, ConcernPage
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from home.block import SimpleCrousal, AdvanceCrousal, TermPageCard


class HomePage(Page):

    section_video_title = models.CharField(max_length=200, help_text="title of the video section")
    section_video_icon = models.ForeignKey('wagtailimages.Image',
                                           on_delete=models.SET_NULL, related_name='+', null=True)

    section_social_title = models.CharField(max_length=200, help_text="title of the social section")
    section_concern_title = models.CharField(max_length=200, help_text="title of the concern section")
    section_concern_icon = models.ForeignKey('wagtailimages.Image',
                                           on_delete=models.SET_NULL, related_name='+', null=True)

    section_article_title = models.CharField(max_length=200, help_text="title of the article section")
    section_article_icon = models.ForeignKey('wagtailimages.Image',
                                           on_delete=models.SET_NULL, related_name='+', null=True)
    section_article_banner = models.ForeignKey('wagtailimages.Image',
                                             on_delete=models.SET_NULL, related_name='+', null=True)

    section_about_title = models.CharField(max_length=200, help_text="title of the about section")
    section_about_icon = models.ForeignKey('wagtailimages.Image',
                                             on_delete=models.SET_NULL, related_name='+', null=True)

    section_about_image = models.ForeignKey('wagtailimages.Image',
                                               on_delete=models.SET_NULL, related_name='+', null=True)

    section_about_descripton = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('section_video_title'),
        ImageChooserPanel('section_video_icon'),
        FieldPanel('section_social_title'),
        FieldPanel('section_concern_title'),
        ImageChooserPanel('section_concern_icon'),
        FieldPanel('section_article_title'),
        ImageChooserPanel('section_article_icon'),
        ImageChooserPanel('section_article_banner'),
        FieldPanel('section_about_title'),
        ImageChooserPanel('section_about_icon'),
        ImageChooserPanel('section_about_image'),
        FieldPanel('section_about_descripton', classname='full'),
    ]

    def get_context(self, request, *args, **kwargs):

        context =  super(HomePage, self).get_context(request)
        context['social'] = SocialPage.objects.all()
        context['videos'] = VideoSection.objects.all()
        concerns = ConcernPage.objects.all()[:4]
        context['services'] = concerns
        faqs = FAQ.objects.filter(featured=True)
        context['faqs'] = faqs
        return context


class GuidelinePage(Page):

    description = RichTextField(blank=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
    ]


class PrivacyPage(Page):
    templates = 'home/privacy_page.html'

    sub_title = models.CharField(max_length=255, blank=True, null=True)
    head_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    head_description = RichTextField(blank=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    footer_title = models.CharField(max_length=255, blank=True, null=True)
    footer_icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    footer_description = RichTextField(blank=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    simplecrousal = StreamField(
        [
            ("simplecrousal", SimpleCrousal()),
            ("AdvanceCrousal", AdvanceCrousal()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        ImageChooserPanel('head_image'),
        FieldPanel('head_description', classname='full'),
        FieldPanel('footer_title'),
        FieldPanel('footer_description', classname='full'),
        ImageChooserPanel('footer_icon'),
        StreamFieldPanel("simplecrousal"),
    ]


class TermPage(Page):
    templates = 'home/term_page.html'

    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    sub_title = models.CharField(max_length=255,null=True,blank=True)
    description = RichTextField(blank=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    icon_caption = models.CharField(max_length=100, blank=True, null=True)
    footer_description = RichTextField(help_text="Add description", blank=True, null=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    cards = StreamField(
        [
            ("termpagecard", TermPageCard()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        ImageChooserPanel('cover_image'),
        ImageChooserPanel('image'),
        ImageChooserPanel('icon'),
        FieldPanel('icon_caption'),
        FieldPanel('description', classname='full'),
        FieldPanel('footer_description', classname='full'),
        StreamFieldPanel("cards"),
    ]


class CommunityGuidline(Page):
    templates = 'home/community_guidline.html'

    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    sub_title = models.CharField(max_length=255,null=True,blank=True)
    description = RichTextField(blank=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    icon_caption = models.CharField(max_length=100, blank=True, null=True)
    footer_description = RichTextField(help_text="Add description", blank=True, null=True, features=[
        'h1','h2', 'h3','h4','h5','h6', 'bold', 'italic',
         'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
           'code', 'blockquote', 'superscript', 'subscript', 'strikethrough'
        ])
    cards = StreamField(
        [
            ("communitypagecard", TermPageCard()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('sub_title'),
        ImageChooserPanel('cover_image'),
        ImageChooserPanel('image'),
        ImageChooserPanel('icon'),
        FieldPanel('icon_caption'),
        FieldPanel('description', classname='full'),
        FieldPanel('footer_description', classname='full'),
        StreamFieldPanel("cards"),
    ]


@register_snippet
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = RichTextField(blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question
