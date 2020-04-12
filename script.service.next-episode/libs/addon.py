# coding: utf-8
# (c) 2018, Roman Miroshnychenko <roman1972@gmail.com>
# License: GPL v. 3 <http://www.gnu.org/licenses/gpl-3.0.en.html>

from __future__ import unicode_literals
import os
from kodi_six.xbmcaddon import Addon

__all__ = ['addon', 'addon_id', 'addon_version', 'icon']

addon = Addon()
addon_id = addon.getAddonInfo('id')
addon_version = addon.getAddonInfo('version')
icon = os.path.join(addon.getAddonInfo('path'), 'icon.png')
