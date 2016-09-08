#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
from mako.template import Template

mytemplate = Template("hello world!")
print(mytemplate.render())