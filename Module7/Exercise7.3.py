fname = input('Enter the file name: ')
try:
    if fname == 'na na boo boo' :
        print ("NA NA BOO BOO, How the turn tables!")
    else:
        fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)