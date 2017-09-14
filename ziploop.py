names = ['john','jane','jack']

email_domains = ['gmail.com','yahoo.com','hotmail.com']

for name,domain in zip(names,email_domains): #zips two lists together

    print(name + '@' + domain)
