# analysis/https_checker.py

import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime

def check_https(url):
    result = {
        "https_supported": False,
        "certificate_valid": False,
        "issuer": None,
        "valid_from": None,
        "valid_to": None,
        "error": None
    }

    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        if not parsed_url.scheme.startswith("https"):
            result["error"] = "URL does not use HTTPS"
            return result

        result["https_supported"] = True

        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                result["certificate_valid"] = True
                result["issuer"] = cert.get("issuer", [[("Unknown", "")]])[0][0][1]
                result["valid_from"] = cert.get("notBefore")
                result["valid_to"] = cert.get("notAfter")

    except Exception as e:
        result["error"] = str(e)

    return result
