#
lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

#1-50
lst1=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst1)

#1-30 even aanenki  numberum ,even     odd aanenki number, odd
lst3=[(i,'even') if i%2==0 else (i,'odd') for i  in range(1,31)]
print(lst3)

#number even aanenki sqr num 5divisible aanenki 0 allenki aa numb
lst4=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,31)]
print(lst4)

#
name='luminartechnolab'
vowels='aeiou'
lst=[i for i in name if i in vowels]
print(lst)

#iterate character vowel allenki'y' allenki 'n'
name='luminartechnolab'
vowels='aeiou'
lst=['y'if i in vowels else 'n' for i in name]
print(lst)