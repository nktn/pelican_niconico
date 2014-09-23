embed niconico video Plugin For Pelican
==================================

Pelican niconico is a plugin to enabled you to embed niconico videos in your pages
and articles.(unOfficial)


Installation
------------

To enable, ensure that `pelican_niconico.py` is put somewhere that is accessible.
Then use as follows by adding the following to your pelicanconf.py:

    PLUGIN_PATH = 'path/to/pelican-plugins'
    PLUGINS = [
        # ...
        'pelican_niconico',
        # ...
        ]

`PLUGIN_PATH` can be a path relative to your settings file or an absolute path.

Usage
-----
code-block:: md
[niconico:niconicoVideoID]  
  
if you want to resize embed player  
[niconico:niconicoVideoID?w=560&h=315]  
  
Example
-----
[niconico:sm22098259]  