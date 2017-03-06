def app(environ, start_respons):
	start_respons('200 OK',[('Content-Type', 'text/plain')])
	req = environ['QUERY_STRING'].split("&")
	body = [item+"\n" for item in req]
	return
