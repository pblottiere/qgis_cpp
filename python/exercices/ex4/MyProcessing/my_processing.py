# -*- coding: utf-8 -*-

"""
/***************************************************************************
 MyProcessing
                                 A QGIS plugin
 d
                              -------------------
        begin                : 2016-09-12
        copyright            : (C) 2016 by a
        email                : a
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'a'
__date__ = '2016-09-12'
__copyright__ = '(C) 2016 by a'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from processing.core.Processing import Processing
from my_processing_provider import MyProcessingProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class MyProcessingPlugin:

    def __init__(self):
        self.provider = MyProcessingProvider()

    def initGui(self):
        Processing.addProvider(self.provider)

    def unload(self):
        Processing.removeProvider(self.provider)
