def calc(a,b,what):
    if what == 1:
        return(a+b)
    if what == 2:
        return(a-b)
    if what == 3:
        return(a*b)
    if what == 4:
        return(a/b)

symbols = [1,2,3,4]
words = ['add','sub','mul','div']

apna_jodi = dict(zip(words,symbols))

a,req,b = input("What to do? type like 2 mul 4 : \n").split(" ")
calc(int(a),int(b),int(apna_jodi[req]))
