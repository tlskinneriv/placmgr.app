from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import Pages
import HWFuncs

# set up the Flask web app
app = Flask(__name__)
app.debug = True

# set up the hardware
HWFuncs.serial_port = '/dev/ttyS0'

# takes care of showing pages and content
for name, page in Pages.pages.items():
    kargs = {}
    if page.methods:
        kargs['methods'] = page.methods
    if page.render_function:
        func = lambda page=page: page.render_function(page)
    else:
        func = lambda page=page: Pages.default_render_function(page)
    app.add_url_rule(page.route, endpoint=page.template_name, view_func=func, **kargs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
