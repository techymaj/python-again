import webbrowser

url = "https://www.majaliwa.tech"
# opens the system's default browser
# webbrowser.open(url)


firefox = webbrowser.get(using="firefox")
firefox.open(url)
