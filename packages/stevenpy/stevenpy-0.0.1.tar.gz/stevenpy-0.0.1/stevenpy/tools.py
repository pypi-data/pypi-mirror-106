# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:46:25 2021

@author: Steven Verwer
"""

import re
import os

from io import StringIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def __check_instance__(variable, reqType):
    if not isinstance(variable, reqType):
        exceptionMessage = [
            'TypeError: ', str( type(variable) ),
            " was given while ", str( type(reqType) ), " was expected."
        ]
        raise Exception( ''.join(exceptionMessage) )
    return

class pdf_class (object):
            def __init__(self, **kwargs):
                self.dat_loc = kwargs.get('dat_loc')
                self.password = ""
                self.maxpages = kwargs.get('maxpages',0)
                self.caching = True
                self.rsrcmgr = PDFResourceManager()
                self.retstr = StringIO()
                self.laparams = LAParams()
                self.device = TextConverter(self.rsrcmgr, self.retstr, laparams=self.laparams)
                self.interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)
                self.pagenos=set()
                return
            
            def __get_pages__(self,file):
                self.fp = open(self.dat_loc / file, 'rb')
                pages = PDFPage.get_pages(self.fp,
                                      self.pagenos,
                                      maxpages=self.maxpages,
                                      password=self.password,
                                      caching=self.caching,
                                      check_extractable=True)
                parser = PDFParser(self.fp)
                self.doc = PDFDocument(parser)
                return pages
            
            def __pagestr__(self,page):
                self.retstr.truncate(0)
                self.retstr.seek(0)
                self.interpreter.process_page(page)
                return self.retstr.getvalue()

            def __inbuild_regex__(self,pages,expression,label):
                data = label + ',' + 'pageNum' + ',' + 'ModDate\n'
                pageNum = 1
                for page in pages:
                    unique_founds_strings = []
                    found_strings = []
                    for line in self.__pagestr__(page).splitlines():                
                        found_strings = re.findall(expression, line)
                        for found_string in found_strings:
                            if found_string not in unique_founds_strings:
                                unique_founds_strings += [found_string]
                    for found_string in unique_founds_strings:
                        data += (found_string + ',' +
                        str(pageNum) + ',' +
                        str(self.doc.info[0]['ModDate'][2:-7],'utf-8') + '\n')
                    pageNum +=1
                return data
            
            def __terminate__(self):
                self.fp.close()
                self.device.close()
                self.retstr.close()
                return None

def listdir_dirs_only(path):
    lst = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(file):
            lst.remove(file)
    return lst