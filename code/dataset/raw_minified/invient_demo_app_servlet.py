from muntjac.terminal.gwt.server.application_servlet import ApplicationServlet as A
class B(A):
	def writeAjaxPageHtmlMuntjacScripts(C,window,themeName,application,page,appUrl,themeUri,appId,request):A=page;A.write('<script type="text/javascript">\n');A.write('//<![CDATA[\n');A.write('document.write("<script language=\'javascript\' src=\'./jquery/jquery-1.4.4.min.js\'><\\/script>");\n');A.write('document.write("<script language=\'javascript\' src=\'./js/highcharts.js\'><\\/script>");\n');A.write('document.write("<script language=\'javascript\' src=\'./js/modules/exporting.js\'><\\/script>");\n');A.write('//]]>\n</script>\n');super(B,C).writeAjaxPageHtmlMuntjacScripts(window,themeName,application,A,appUrl,themeUri,appId,request)