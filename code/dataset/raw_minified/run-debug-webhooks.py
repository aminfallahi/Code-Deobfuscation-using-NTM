' Run openaddr.ci.webhooks.app in Flask debug mode.\n'
from openaddr.ci.web import app
if __name__=='__main__':app.run(debug=True)