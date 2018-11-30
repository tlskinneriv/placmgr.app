class NavItemObject():

    def __init__(self, name, template_name, route, methods=None, handler_function=None):
        self.name = str(name)
        self.template_name = str(template_name)
        self.route = str(route)
        self.methods = methods
        self.handler_function = handler_function

    def __str__(self):
        return '{name:' + str(self.name) + ',template_name:' + str(self.template_name) + ',locations:' + str(self.locations) + '}'

    def template_name_full(self):
        return self.template_name + '.html.j2'
