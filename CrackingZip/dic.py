import zipfile

z = zipfile.ZipFile('secret.zip')

wordlist = open('cain.txt','r').read()
wordlist = wordlist.splitlines()
tries = 0

for password in wordlist:
    try:
        tries+=1
        z.setpassword(password.encode('ascii'))
        z.extract('secret.txt')
        print(f"seuccessfully cracked after {tries} tries! password was: {word}")
        break
    except:
        pass