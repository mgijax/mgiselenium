'''
Created on Nov 1, 2016

@author: jeffc
'''
from io import StringIO
class Report (object):
    _report_string=None
    
    def __init__(self):
        self._report_string=""
        #Write Report header
    def WriteReportHeader (self):
        self._report_string+="<html><header><title>Test Result Report</title></header><body>"
        self._report_string+="<table border=\"2\">"
        self._report_string+="<tr>"
        self._report_string+="<td>TestID</td>"
        self._report_string+="<td>TestCase</td>"
        self._report_string+="<td>Action</td>"
        self._report_string+="<td>ExpectedResult</td>"
        self._report_string+="<td>ActualResult</td>"
        self._report_string+="<td>Pass/Fail</td>"
        self._report_string+="<td>TestNote</td>"
        self._report_string+="</tr>"
        #Append To REPORT
    def AppendToReport (self,test_id,test_case_name,action,expected_result,actual_result,pass_fail,test_note):
        if(pass_fail.lower()=='pass'):
            self._report_string+="<tr style=\"background-color:#33cc33\">"
        else:
            self._report_string+="<tr style=\"background-color:#ffff00\">"
        self._report_string+="<td>"+ test_id +"</td>"
        self._report_string+="<td>"+ test_case_name +"</td>"
        self._report_string+="<td>"+ action +"</td>"
        self._report_string+="<td>"+ expected_result +"</td>"
        self._report_string+="<td>"+ actual_result +"</td>"
        self._report_string+="<td>"+ pass_fail +"</td>"
        self._report_string+="<td>"+ test_note +"</td>"
        self._report_string+="</tr>"
        #write Footer
    def WriteReportFooter (self):
        self._report_string+="</table></body></html>"
    def WriteToFile (self,filename):
        #convert final string object to string
        final_string=self._report_string
        report_file=open(filename, 'w')
        report_file.write(final_string)
        report_file.close()
        