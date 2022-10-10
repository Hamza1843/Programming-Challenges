import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def get_tr(html, i):
    open_tr = html.find('<tr>', i)
    close_tr = html.find('</tr', open_tr)
    i = close_tr
    return html[open_tr:close_tr], i

def create_list(html):
    list_tr = []
    i = 0
    for n in range(10):
        tr, i = get_tr(html, i)
        list_tr.append(tr)
    return(list_tr)

def get_title(html):
    lookingfor = '<div class="title">'
    title_i = html.find(lookingfor)
    open_title = html.find('>', title_i+len(lookingfor))
    close_title = html.find('<', open_title)
    return html[open_title+1:close_title]

def get_artist(html):
    lookingfor = '<div class="artist">'
    artist_i = html.find(lookingfor)
    open_artist = html.find('>', artist_i+len(lookingfor))
    close_artist = html.find('<', open_artist)
    return html[open_artist+1:close_artist]

def get_pos(html):
    lookingfor = '<span class="position"'
    pos_i = html.find(lookingfor)
    open_pos = html.find('>', pos_i+len(lookingfor))
    close_pos = html.find('<', open_pos)
    return html[open_pos+1:close_pos]

if __name__ == "__main__":
    html = scrape(url)
    list = create_list(html)
    print(f'{"#":<5}{"Artist":<50}{"Title":<50}')
    for i in list:
        title = (get_title(i))
        artist = (get_artist(i))
        pos = (get_pos(i))
        print(f'{pos:<5}{artist:<50}{title:<50}')
        

        