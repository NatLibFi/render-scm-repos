import importlib

#Instantiate all services
#Call .get on each service
#Merge results
#render

def run():
  importlib.import_module('render_scm_repos.service')
