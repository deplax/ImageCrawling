# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from ghost import Ghost

ghost = Ghost()
page, resources = ghost.open('http://www.naver.com')
ghost.read
