# -*- coding: utf-8 -*-
import copy
from cStringIO import StringIO

from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from classytags.core import Tag, Options
from classytags.arguments import (
    Argument,
    MultiKeywordArgument,
)
from classytags.blocks import BlockDefinition


register = template.Library()


class Block(object):
    def __init__(self, nodes, context):
        self.nodes = nodes
        self._context = context

    def __unicode__(self):
        buf = StringIO()
        for n in self.nodes:
            buf.write(n.render(self._context))
        return mark_safe(buf.getvalue())

    __str__ = __repr__ = __unicode__


class RenderWith(Tag):
    options = Options(
        Argument('template', resolve=False),
        MultiKeywordArgument('kwargs', required=False, resolve=True),
        blocks=[
            BlockDefinition('nodelist', 'end')
        ]
    )

    def render_tag(self, context, template, kwargs, nodelist):
        context = copy.copy(context)
        context.update(kwargs)
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
