# contains pages and all rendering/handler funcitons associated with them

from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
import Forms
from PlacComm import PlacComm
import time

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
    'home' : Page('Plac Manager', 'Home', 'home', '/'),
    'plac_settings' : Page('Plac Settings', 'Plac Settings', 'plac_settings', '/plac-settings')
}

# set navbar pages
navbar_pages = [
    pages['home'], pages['plac_settings']
]

# set default render function
def default_render_function(page, **kwargs):
    return render_template(page.template_name_full(), navbar_pages=navbar_pages, page_title=page.title, **kwargs)

# set render function and other options for specific pages
def plac_settings_render(page):
    form = Forms.PlacSettingsForm(request.form)
    if request.method == 'POST' and form.validate():
        # setup plac comm handler
        plac = PlacComm('A1', 'plac') #TODO dynamically get from DB
        result = plac.send_data(
            computer_name = form.computer_name.data,
            ip_address = form.ip_address.data,
            subnet_mask = form.subnet_mask.data,
            gateway = form.gateway.data,
            network = form.network.data
        )
        if result == True:
            message='<p class="message-good">Sent settings successfully.</p>'
        else:
            message = '<p class="message-bad">Failed to send settings:<br/>' + str(result).replace('\n', '<br/>') + '</p>'
            print(str(result))
        return default_render_function(page, form=form, message=message)
    return default_render_function(page, form=form)
pages['plac_settings'].set_methods(['GET', 'POST'])
pages['plac_settings'].set_render_function(plac_settings_render)
