import webbrowser


def OpenOf(link: str)-> None:
    url = link
    path = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
    webbrowser.get('chrome').open(url)

