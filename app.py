from flask import Flask, render_template, request
from analysis.https_checker import check_https
from analysis.cookie_checker import check_cookies
from analysis.hsts_checker import check_hsts

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        url = request.form['url']

        # HTTPS Kontrolü
        https_result = check_https(url)

        # Cookie Güvenliği Kontrolü
        cookie_result = check_cookies(url)

        # HSTS Header Kontrolü
        hsts_result = check_hsts(url)

        # Tüm analiz sonuçlarını tek bir sözlükte birleştiriyoruz
        result = {
            "message": f"Analysis results for {url}",
            **https_result,
            **cookie_result,
            **hsts_result
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
