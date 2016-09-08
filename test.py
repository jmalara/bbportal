#!/usr/bin/env python

from mako.template import Template
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
mytemplate = Template("hello world!")
print(mytemplate.render())