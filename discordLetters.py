import os

numword = {'0': ':zero:', '1': ':one:', '2': ':two:', '3': ':three:', '4': ':four:',
           '5': ':five:', '6': ':six:', '7': ':seven:', '8': ':eight:', '9': ':nine:'}

def msgfunc():
    ask = input('Message: ')
    msg = []
    for x in list(ask):
        if x == ' ' or x == ',':
            msg.append('   ')
        elif x == '?':
            msg.append(':question: ')
        elif x == '!':
            msg.append(':exclamation: ')
        elif x == "'":
            pass
        elif x in numword.keys():
            msg.append(numword[x] + ' ')
        else:
            msg.append(':regional_indicator_%s: ' % x.lower())
    nmsg = ''.join(msg)
    os.system("echo %s | clip" % nmsg)
    msgfunc()
msgfunc()
