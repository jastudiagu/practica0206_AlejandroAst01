import urllib.request


def lee_url(url):
    archivo = urllib.request.urlopen(url)
    cont = 0
    for line in archivo:
        decoded_line = line.decode("utf-8")
        cont += 1
        print(decoded_line)
    
    print(cont)
    return


url = "http://textfiles.com/adventure/aencounter.txt"

lee_url(url)

