#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
cgitb.enable()

from mako.template import Template

mytemplate = Template("hello world!")
print(mytemplate.render())