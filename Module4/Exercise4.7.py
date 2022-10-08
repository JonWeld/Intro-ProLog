def computegrade(score):
    grade = float(score)
    if 0.0 <= score <= 1.0:
        if grade >= 0.9: 
            print ("A")
        elif grade >= 0.8: 
            print ("B")
        elif grade >= 0.7: 
            print ("C")
        elif grade >= 0.6: 
            print ("D")
        elif grade < 0.6:
            print ("F")
    return 'Bad score'


ip_score = input('Enter score: ')
score = 1.0


try:
    score = float(ip_score)
except ValueError:
    print('Bad score')
    quit()









        
        
