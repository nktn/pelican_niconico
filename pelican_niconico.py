# -*- coding: utf-8 -*-
"""
niconico video embedding plugin for Pelican
=================================

This plugin allows you to embed `niconico video`_ into your posts.

.. _niconico: http://www.nicovideo.jp/video_top/

"""
from __future__ import unicode_literals
import os
import re

niconico_regex = re.compile(
    r'(<p>\[niconico:([0-9a-zA-Z=\+\?]+)(,file\=([^\]]+))?\]</p>)')
niconico_template = """<div class="niconico">
    <script type="text/javascript" src="{{ niconico_url }}"></script>
    </div>
    """


def niconico_url(niconico_id):
    url = "http://ext.nicovideo.jp/thumb_watch/{}".format(niconico_id)
    return url


def replace_niconico_tags(generator):
    from jinja2 import Template
    template = Template(niconico_template)
    
    for article in generator.articles:
        for match in niconico_regex.findall(article._content):
            niconico_id = match[1]
            context = generator.context.copy()
            context.update({
                'niconico_url': niconico_url(niconico_id),
            })
            replacement = template.render(context)
            article._content = article._content.replace(match[0], replacement)


def register():
    from pelican import signals
    signals.article_generator_finalized.connect(replace_niconico_tags)