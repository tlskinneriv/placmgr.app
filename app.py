from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from NavItemObject import NavItemObject
import Forms
from PlaqComm import PlaqComm

# set up the Flask web app
app = Flask(__name__)
app.debug = True

# define the pages
pages = {
    'home': NavItemObject('Home', 'home', '/'),
    'plaq_settings': NavItemObject('Plaq Settings', 'plaq_settings', '/plaq-settings')
}


# takes care of renering general pages
def page_handler_function(temp_name, nav_items, **kargs):
    return render_template(temp_name, nav_bar_items=nav_items, **kargs)

# set specific handler functions and methods for pages


page = pages['plaq_settings']
page.methods = ['GET', 'POST']


def plaq_settings_handler(temp_name, nav_items):
    form = Forms.PlaqSettingsForm(request.form)
    if request.method == 'POST' and form.validate():
        # setup plaq comm handler
        plaq = PlaqComm('plaq1', 'plaq1') #TODO dynamically get from DB
        plaq.send_data(
            computer_name = form.computer_name.data,
            ip_address = form.ip_address.data,
            subnet_mask = form.subnet_mask.data,
            gateway = form.gateway.data
        )
    return page_handler_function(temp_name, nav_items, form=form)
page.handler_function = plaq_settings_handler

# takes care of showing pages and content
for name, page in pages.items():
    kargs = {}
    if page.methods:
        kargs['methods'] = page.methods
    if page.handler_function:
        func = lambda page=page: page.handler_function(
            page.template_name_full(), pages)
    else:
        func = lambda page=page: page_handler_function(
            page.template_name_full(), pages)
    app.add_url_rule(page.route, endpoint=page.template_name,
                     view_func=func, **kargs)

# revises specific pages

# takes care of submitting data to the queue
# plaq_settings_base = nav_items['plaq_settings'].locations[0]
# @app.route(plaq_settings_base + '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
