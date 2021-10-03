import requests
import sys
import time
import random



# stuff for the request
def main():

    profile_url = input('Enter your NameMC URL >: ') # defining the url
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.53'
    headers = {'user-agent': f'{user_agent}'}

    if profile_url == profile_url:
        r = ProxyRequests(profile_url) 
        r.set_headers(headers)
        r.get_with_headers()
        time.sleep(10)
        print(f'Pinged {profile_url} with proxy {r.get_proxy_used} and status code {r.get_status_code}')

main()

#cls to clr powershell
