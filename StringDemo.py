Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String => anything inside '',"", ''' '''
x = "welcome to python"
type(x)
<class 'str'>
x = 'welcome to python'
type(x)
<class 'str'>
x = '''Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
'''
type(x)
<class 'str'>
x = "lets LEARN pYthon"
x.lower()
'lets learn python'
x.upper()
'LETS LEARN PYTHON'
x.swapcase()
'LETS learn PyTHON'
x.capitalize()#pure string ka first letter capital
'Lets learn python'
x.title()
'Lets Learn Python'
x
'lets LEARN pYthon'
len(x)
17
x = "python is a high level language"
"python" in x
True
"X" in x
False
#indexing
x = "Python Programming"
x[0]
'P'
x[2]
't'
x[-1]
'g'
x.find("g")
10
x.rfind("g")
17
x
'Python Programming'
x = "hello welcome to arth institute"
x.find("o")
4
x.rfind("o")
15
x.find("o",5)
10
x.find("Z")#it will return -1(value not found)
-1
x.index("o",5)
10
x.index("Z")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x.index("Z")
ValueError: substring not found
x
'hello welcome to arth institute'
x.count("o")
3
x.count(" ")
4
