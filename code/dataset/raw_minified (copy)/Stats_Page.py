from bitHopper.Website import app,flask
import btcnet_info,bitHopper.Configuration.Miners
@app.route('/stats',methods=['POST','GET'])
def A():return flask.render_template('stats.html')