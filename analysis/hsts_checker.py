import requests

def check_hsts(url):
    result = {
        "hsts_enabled": False,
        "header": None,
        "error": None
    }

    try:
        response = requests.get(url)
        hsts_header = response.headers.get("Strict-Transport-Security")

        if hsts_header:
            result["hsts_enabled"] = True
            result["header"] = hsts_header
        else:
            result["error"] = "HSTS header not found."

    except Exception as e:
        result["error"] = str(e)

    return result
