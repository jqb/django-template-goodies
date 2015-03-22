# -*- coding: utf-8 -*-
import copy

from django import template
from django.template.loader import render_to_string

from classytags.core import Tag, Options
from classytags.arguments import (
    Argument,
    MultiKeywordArgument,
)
from classytags.blocks import BlockDefinition


register = template.Library()


class Block(object):
    def __init__(self, nodes, context, name=None):
        self.name = name
        self.nodes = nodes
        self._context = context

    def __unicode__(self):
        return self.nodes.render(self._context)

    __str__ = __repr__ = __unicode__


class DefBlock(Tag):
    options = Options(
        Argument('name', resolve=True),
        MultiKeywordArgument('kwargs', required=False, resolve=True),
        blocks=[
            BlockDefinition('nodelist', 'end')
        ]
    )

    def render_tag(self, context, name, kwargs, nodelist):
        def_block = context.get('def_block', {})
        context['def_block'] = def_block
        context = copy.copy(context)
        context.update(kwargs)

        for n in nodelist:
            if isinstance(n, DefBlock):
                n.render(context)

        def_block[name] = Block(nodelist, context, name=name)
        return ''


register.tag(DefBlock)


class UseBlock(Tag):
    options = Options(
        Argument('name', resolve=True),
        MultiKeywordArgument('kwargs', required=False, resolve=True),
    )

    def render_tag(self, context, name, kwargs):
        def_block = context.get('def_block', {})
        context['def_block'] = def_block

        block = def_block[name]
        ctx = copy.copy(block._context)
        ctx.update(context)
        ctx.update(kwargs)

        return block.nodes.render(ctx)


register.tag(UseBlock)


class RenderWith(Tag):
    options = Options(
        Argument('template', resolve=True),
        MultiKeywordArgument('kwargs', required=False, resolve=True),
        blocks=[
            BlockDefinition('nodelist', 'end')
        ]
    )

    def render_tag(self, context, template, kwargs, nodelist):
        context = copy.copy(context)
        context.update(kwargs)

        for n in nodelist:
            if isinstance(n, DefBlock):
                n.render(context)

        context['block'] = Block(nodelist, context)
        return render_to_string(template, context)


register.tag(RenderWith)


class Dict(Tag):
    options = Options(
        Argument('name', resolve=False),
        MultiKeywordArgument('kwargs', resolve=True),
    )

    def render_tag(self, context, name, kwargs):
        data = context.get(name) or {}
        data.update(kwargs)
        context[name] = data
        return ''


register.tag(Dict)
