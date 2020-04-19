import webbrowser as wb

def angry():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DX3ND264N08pv")

def sad():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro")

def happy():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DX9XIFQuFvzM4")

def neutral():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DWSiZVO2J6WeI")         #Sleepy

def disgusted():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634")         #Life Sucks

def surprised():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DX1tyCD9QhIWF")         #Walk like a badass

def fear():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DWSRc3WJklgBs")         #Heart Beats

def final(emotion):
    if emotion=="Angry":
        angry()
    elif emotion=="Sad":
        sad()
    elif emotion=="Disgust":
        disgusted()
    elif emotion=="Happy":
        happy()
    elif emotion=="Neutral":
        neutral()
    elif emotion=="Surprise":
        surprised()
    elif emotion=="Fear":
        fear()