import requests

def check_cookies(url):
    result = {
        "cookies_found": False,
        "secure_flag": False,
        "http_only_flag": False,
        "cookies": [],
        "error": None
    }

    try:
        response = requests.get(url)
        cookies = response.cookies

        if cookies:
            result["cookies_found"] = True
            for cookie in cookies:
                cookie_info = {
                    "name": cookie.name,
                    "secure": cookie.secure,
                    "httponly": cookie._rest.get("HttpOnly", False)
                }
                if cookie.secure:
                    result["secure_flag"] = True
                if cookie._rest.get("HttpOnly", False):
                    result["http_only_flag"] = True
                result["cookies"].append(cookie_info)
        else:
            result["error"] = "No cookies found."
    except Exception as e:
        result["error"] = str(e)

    return result
