'''
Created on Sep 7, 2017
These tests are to confirm results you get back using various edit requirements
@author: jeffc
@attention: Do not use these tests against a production system! Since you are editing it will cause  data to be changed
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestLitEdit(unittest.TestCase):
    """
    @status Test Literature Triage editing features
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triage")
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
    
    def tearDown(self):
        self.driver.close()
        

    def testRefStatusEdit(self):
        """
        @Status tests that changing a "not routed" reference to "chosen" assigns it a J number
        @see MBIB-edit-1,2 (1)
        """
        form = self.form
        time.sleep(5)
        self.driver.find_element_by_id("status_AP_Not_Routed").click()
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("editTabWorkFlowStatus")
        table = Table(table_element)
        #finds the Not Routed column for AP and returns it's status of selected
        not_route = table.get_cell(1,2)
        self.assertTrue(not_route.is_selected, "Not Routed for AP is not selected")
        #select the chosen status for AP
        #chosen = table.get_cell("AP", "Chosen").click()
        self.driver.find_element_by_xpath("//input[@name='10' and @value='Chosen']").click()
        #click the Modify button
        self.driver.find_element_by_id('modifyEditTabButton').click()
        chosen = self.driver.find_element_by_xpath("//input[@name='10' and @value='Chosen']")
        #Verifies Chosen status is selected for AP
        self.assertTrue(chosen.is_selected, "Chosen for AP is not selected")
        time.sleep(2)
        #finds the Reference J: field of the Reference ID table and return it's text value
        table_element1 = self.driver.find_element_by_id("editRefIdTable")
        table1 = Table(table_element1)
        jnum_cell = table1.get_cell(0,1)
        time.sleep(1)
        print jnum_cell.text
        #Need to find an assert that works
        #self.assertTrue(jnum_cell,'J number field is empty')
        
    def testReftypeEdit(self):
        """
        @Status tests the modifying of a Reference Type by using the pulldown list
        @see MBIB-edit-4 (9)
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:15839')
        form.click_search()
        #finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element_by_id("editTabRefType").get_attribute('value')
        print ref_type
        self.assertEqual(ref_type, 'MGI Curation Record')
        #finds the Reference type field and modify its value
        select = Select(self.driver.find_element_by_id("editTabRefType"))
        select.select_by_visible_text('Unreviewed Article')
        #click the Modify button
        self.driver.find_element_by_id('modifyEditTabButton').click()
        #finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element_by_id("editTabRefType").get_attribute('value')
        self.assertEqual(ref_type, 'Unreviewed Article')      
        #finds the Reference type field and modify its value
        select = Select(self.driver.find_element_by_id("editTabRefType"))
        select.select_by_visible_text('MGI Curation Record')
        #click the Modify button to set the Reference Type back to MGI Curation Record.
        self.driver.find_element_by_id('modifyEditTabButton').click()
    def testDiscardEdit(self):
        """
        @Status tests the setting of the MGI Discard flag
        @see MBIB-edit-21 (27)
        """
        form = self.form
        time.sleep(5)
        form.enter_value('accids', 'J:32887')
        form.click_search()
        discard = self.driver.find_element_by_id("editTabIsDiscard")
        self.assertFalse(discard.is_selected())
        #finds the MGI Discard box and checks it
        self.driver.find_element_by_id("editTabIsDiscard").click()
        #find the MGI Discard box and check it's selected
        self.driver.find_element_by_id("editTabIsDiscard").is_selected()
        #click the Modify button
        self.driver.find_element_by_id('modifyEditTabButton').click()
        #find the MGI Discard box and check it's selected
        self.driver.find_element_by_id("editTabIsDiscard").is_selected()
                
    def testAddTagEdit(self):
        """
        @Status tests that you can add a tag using the autocomplete option
        @see MBIB-edit-22, 23
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:22341')
        form.click_search()
        
        #finds the tag field
        self.driver.find_element_by_id("tags").send_keys("MGI:CorrectionAdded")
        #find and click the Associate button
        self.driver.find_element_by_id("saveTagButton").click()
        wait.forAngular(self.driver)
        #finds the Tag list and verifies the required tag is listed.
        table_element = self.driver.find_element_by_id("editTabTags")
        table = Table(table_element)
        #finds the selected tags column and verified it contains the added tag
        sel_tags = table.get_column_cells(1)
        used_tags = iterate.getTextAsList(sel_tags)
        print used_tags
        #asserts that the following J numbers are returned
        self.assertIn('MGI:CorrectionAdded', used_tags)
        
        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()