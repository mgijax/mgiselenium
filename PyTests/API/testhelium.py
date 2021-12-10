'''
Created on Sep 23, 2021
just a simple test for helium-python API
Tested and passed 09/23/2021
@author: jeffc
'''
from helium import *
helium.start_firefox("google.com")
helium.write('helium selenium github')
helium.press(ENTER)
helium.click('Selenium-python but lighter: Helium - GitHub')
helium.go_to('github.com/login')
helium.write('username', into='Username')
helium.write('password', into='Password')
helium.click('Sign in')
helium.kill_browser()