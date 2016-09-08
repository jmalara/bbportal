import cgitb
cgitb.enable()
from mako.template import Template

mytemplate = Template("hello world!")
print(mytemplate.render())