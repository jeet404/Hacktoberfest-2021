dict1={
        "TCP":"Transsimision Control Protocol",
        "IP":"Internet Protocol",
        "HTTP":"Hyper Text Transfer Protocol",
        "FTP":"File Transfer Protocol",
        "SMTP":"Simple Male Transfer Protocol",
        "POP":"Post Office Protocol",
        "HTML":"Hyper Text Markup Language",
        "CSS":"Cascading Style Sheet",
        "JS":"JavaScript",
        "PHP":"Personal Home Page (HyperText Preprocessor)",
        "JSON":"JavaScript Object Notation",
        "SQL":"Structured Query Language",
        "DB":"Database",
        "RSS":"Really Simple Syndication",
        "XML":"Extensible Markup Language",
        "ASP":"Active Server Pages",
        "AJAX":"Asynchronous JavaScript And XML",
        "J2EE":"Java 2 Platform Enterprise Edition",
      }
print("What do you find : ")
find=input()
if find in dict1:
    print("Full Form is : ",dict1[find])
else:
    print("We are Update soon ,Sorry for that :(")