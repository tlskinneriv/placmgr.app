# contains pages and all rendering/handler funcitons associated with them

from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import Forms
from PlaqComm import PlaqComm

class Page():

    def __init__(self, title, link_name, template_name, route):
        self.title = str(title)
        self.link_name = str(link_name)
        self.template_name = str(template_name)
        self.route = str(route)
        self.methods = None
        self.render_function = None

    def set_methods(self, methods):
        self.methods = list(methods)

    def set_render_function(self, render_function):
        self.render_function = render_function

    def __str__(self):
        return '{name:' + str(self.name) + ',template_name:' + str(self.template_name) + ',locations:' + str(self.locations) + '}'

    def template_name_full(self):
        return self.template_name + '.html.j2'

# declare and define basics of pages
pages = {
    'home' : Page('Plaq Manager', 'Home', 'home', '/'),
    'plaq_settings' : Page('Plaq Settings', 'Plaq Settings', 'plaq_settings', '/plaq-settings')
}

# set navbar pages
navbar_pages = [
    pages['home'], pages['plaq_settings']
]

# set default render function
def default_render_function(temp_name, page_title, **kwargs):
    return render_template(temp_name, navbar_pages=navbar_pages, page_title=page_title, **kwargs)

# set render function and other options for specific pages
def plaq_settings_render(temp_name, page_title):
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
    return default_render_function(temp_name, page_title, form=form)
pages['plaq_settings'].set_methods(['GET', 'POST'])
pages['plaq_settings'].set_render_function(plaq_settings_render)
