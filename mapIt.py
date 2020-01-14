import webbrowser, sys, pyperclip

#webbrowser is...
#sys is for the command line argument...

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    print(address)
else:
    #get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)