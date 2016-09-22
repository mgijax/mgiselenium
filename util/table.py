"""
Helper for working with html tables
Usage:

    from util.table import Table
    
    # find a table WebElement
    table_element = driver.find_element_by_id("#tableId")
    
    #create instance of Table class
    table = Table(table_element)
    
    # all table rows
    rows = table.get_rows()
    
    #find <tr> row by index
    row = table.get_row(1)
    
    #find <tr> row by header name
    row = table.get_row("Row 1")
    
    # all header <th> cells
    cells = table.get_header_cells()
    
    # find a single <td> cell by row, column index
    cell = table.get_cell(1, 2)
    
    # find a single <td> cell by row, column name
    cell = table.get_cell("Row 1", "Column 2")
    
    # find a single <td> cell by either index or name
    cell = table.get_cell(1, "column 2")
    
    # get all cells for a row by index or name
    row_cells = table.get_row_cells(1)
    row_cells = table.get_row_cells("Row 1")
    
"""

class Table(object):
    """
    Represents a table element
    """
    
    def __init__(self, table_web_element):
        self.table_web_element = table_web_element
        
        
    def get_cell(self, row_identifier, col_identifier):
        """
        Retrieve the <td> cell for the given
        row_identifier, col_identifier
            which can be either an index,
             a header (<th>) string,
             or a css selector
        """
        col_index = self._get_col_index(col_identifier)
        row_cells = self.get_row_cells(row_identifier)
        
        cell = row_cells[col_index]
        return cell
        
        
    def get_rows(self):
        return self.table_web_element.find_elements_by_css_selector("tr")
    
    def get_row(self, row_identifier):
        row_index = self._get_row_index(row_identifier)
        rows = self.get_rows()
        return rows[row_index]
    
        
    def get_row_cells(self, row_identifier):
        row = self.get_row(row_identifier)
        return self._get_row_cells(row)
        
        
    def get_header_cells(self):
        return self.get_row_cells(0)
    
    
    def get_header_row(self):
        return self.get_row(0)
    
    def get_column_cells(self, col_identifier):
        col_index = self._get_col_index(col_identifier)
        rows = self.get_rows()
        
        cells = []
        for row in rows:
            cells.append(row[col_index])
    
    
    
        
        
    ### private helper methods  ###
        
    def _get_col_index(self, col_identifier):
        
        # check if index
        if self._is_index(col_identifier):
            return col_identifier
        
        # try column name first
        headers = self.get_header_cells()
        for i in range(len(headers)):
            text = headers[i].text.lower()
            if text == col_identifier.lower():
                return i
                
        raise Exception("could not find column with identifier '%s'" % col_identifier)
    
    
    def _get_row_index(self, row_identifier):
        
        # check if index
        if self._is_index(row_identifier):
            return row_identifier
        
        # try row name first
        rows = self.get_rows()
        for i in range(len(rows)):
            cells = self._get_row_cells(rows[i])
            if cells:
                text = cells[0].text.lower()
                if text == row_identifier.lower():
                    return i
                
        raise Exception("could not find row with identifier '%s'" % row_identifier)
    
    
    def _get_row_cells(self, row_web_element):
        return row_web_element.find_elements_by_css_selector("td, th")
        
        
        
    def _is_index(self, identifier):
        """
        Check if identifier is a numerical index value
        """
        return isinstance(identifier, (int, long))