import urllib2

class GithubService(Service):

  def __init__(self, options={}):
    if 'url' not in options or ('user' not in options or 'organization' not in options or 'token' not in options):
      raise Exception('Invalid options')
    else:
      
      self.url = options.url + ('/users/' + options.user if 'user' in options else '/orgs/' + options.organization) + '/repos'
      self.token = options.token      

  def getRepos(self):

    def iterate(url, repos=[]):

      def parse(data):
        None
      
      response = urllib2.urlopen(urllib2.Request(self.url, headers={
        'OATH_TOKEN': self.token
      }))
      headers = response.info()

      if (headers.getparam('Status') not eq 200):
        raise Exception('Failed listing repositories: ' + headers.getparam('Status') + ' ' + response.read())
      else:
        #parse response
        #continue iteration if the are any more links to next page of results

    return iterate(self.url)
