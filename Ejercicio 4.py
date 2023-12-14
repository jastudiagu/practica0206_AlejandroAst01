import urllib.request


def lee_url(url):
    archivo = urllib.request.urlopen(url)
    for line in archivo:
        decoded_line = line.decode("utf-8")
        print(decoded_line)
    return


url = "http://textfiles.com/adventure/aencounter.txt"

lee_url(url)