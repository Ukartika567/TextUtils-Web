#1.CSRF(Cross Site Request Forgery) ye security ke liye hota hai , jaise hmare password update me CSRF token ka 
# use krte h
# 2.Jo ham post request ya get request krte hai to hmare url bar me hmare query or data v show jata hai jisse hmara id 
# hack v ho skta h isliye usi ke protection ke liye CSRF token ka use krte hai 
# 3.post request me csrf token use krne se na to url bar me data dikhta h n hi id hack hoti h
# 4.is csrf token se relate ek xss(cross site scripting) hoti h jisme Javascript me ek aisa event hota h jisse ek kuch type keke submit krne ya 
# ok krne se hmara account hi dele ho jata h yese me hacker is xss se v id hack kr skta h

# Note:- Is session me ham csrf token ka use krke post request krenge apne data ke liye
#  charage return me \n ke sath \r v lgana pdta h jo newlinechar me lgaya h

# Note:-To solve the Exercise-02 we comment the return statement put codition when checkboxes are not 'on' and djtext
# ko analyze ke equal krke override krte h




from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def  analyze(request):
    # Get the  text
    djtext=request.POST.get('text', 'default')

    # Check checkbox values
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    
    # Check which checkbox is on
    if removepunc == 'on' :
        punctuations=''';:""'',./ ?\_- {} [] () @!#$%^&*<>'''
        analyze=""
        for char in djtext:
            if char not in punctuations:
                analyze= analyze + char

        params={'purpose':'Removed Punctuation', 'analyzed_text': analyze}
        djtext=analyze
      
    if fullcaps == 'on':
        analyze=''
        for char in djtext:
            analyze = analyze + char.upper()

        params={'purpose': 'Change to Uppercase', 'analyzed_text': analyze}
        djtext=analyze
      
    if extraspaceremover == 'on':
        analyze=  ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == '' and djtext[index+1] == ''):
                analyze = analyze + char
        
        params={'purpose': 'Change to Uppercase', 'analyzed_text': analyze}
        djtext=analyze
      
    if newlineremover == 'on':
        analyze = ''
        for char in djtext:
            if char !='\n' and char !="\r":
                analyze = analyze + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyze}
  
    if removepunc!='on' and fullcaps!='on' and extraspaceremover!='on' and newlineremover!='on':
        return HttpResponse('Please choose any operation. Try Again!')
    
    return render(request, 'analyze.html', params)        
