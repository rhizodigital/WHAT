from wagtail import blocks


class StoryBlock(blocks.StreamBlock):
    richtext = blocks.RichTextBlock()

    class Meta:
        template = 'blog/blocks/story_block.html'