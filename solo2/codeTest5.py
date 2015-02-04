# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

dirname = '한글'
if not os.path.isdir(dirname):
    os.mkdir(unicode(dirname))
