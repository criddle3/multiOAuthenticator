from traitlets import List
from jupyterhub.auth import Authenticator
from jupyterhub.utils import url_path_join


class MultiOAuthenticator(Authenticator):
  authenticators = List(help="The subauthenticators to use", config=True)

  def __init__(self, *arg, **kwargs):
    super().__init__(*arg, **kwargs)
    self._authenticators = []
    for authenticator_klass, url_scope, configs in self.authenticators:
      c = self.trait_values()
      c.update(configs)
      self._authenticators.append({"instance": authenticator_klass(**c), "url_scope": url_scope})

  def get_custom_html(self, base_url):
    html = []
    for authenticator in self._authenticators:
      login_service = authenticator["instance"].login_service
      url = url_path_join(base_url, authenticator["url_scope"], "oauth_login")

      html.append(
          f"""
                <div class="service-login">
                  <a role="button" class='btn btn-jupyter btn-lg' href='{url}'>
                    Sign in with {login_service}
                  </a>
                </div>
                """
      )
    return "\n".join(html)

  def get_handlers(self, app):
    routes = []
    for _authenticator in self._authenticators:
      for path, handler in _authenticator["instance"].get_handlers(app):

        class SubHandler(handler):
          authenticator = _authenticator["instance"]

        routes.append((f'{_authenticator["url_scope"]}{path}', SubHandler))
    return routes
