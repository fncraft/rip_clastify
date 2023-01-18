from mitmproxy import http
def response(flow: http.HTTPFlow) -> None:
    if flow.request.path.endswith("can-view"):
        flow.response.status_code = 200
        flow.response.text = "ok"
