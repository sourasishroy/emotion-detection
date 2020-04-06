import webbrowser as wb
emotion=input("Enter emotion")

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

def calm():
    wb.open("https://open.spotify.com/playlist/37i9dQZF1DWSRc3WJklgBs")         #Heart Beats

if emotion=="angry":
    angry()
elif emotion=="sad":
    sad()
elif emotion=="disgusted":
    disgusted()
elif emotion=="happy":
    happy()
elif emotion=="neutral":
    neutral()
elif emotion=="surprised":
    surprised()
elif emotion=="calm":
    calm()