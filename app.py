from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import Pages

# set up the Flask web app
app = Flask(__name__)
app.debug = True

# takes care of showing pages and content
for name, page in Pages.pages.items():
    kargs = {}
    if page.methods:
        kargs['methods'] = page.methods
    if page.render_function:
        func = lambda page=page: page.render_function(page.template_name_full(), page.title)
    else:
        func = lambda page=page: Pages.default_render_function(page.template_name_full(), page.title)
    app.add_url_rule(page.route, endpoint=page.template_name, view_func=func, **kargs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
