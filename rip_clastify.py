from mitmproxy import http
def response(flow: http.HTTPFlow) -> None:
    if flow.request.path.endswith("can-view"):
        flow.response.text = "ok"
