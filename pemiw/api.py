from __future__ import unicode_literals
import  frappe
from frappe.utils import money_in_words
from frappe import _

def get_amount_in_words(self,method):
    self.paid_amount_inwords_cf =''
    self.total_allocated_amount_inwords_cf=''
    self.unallocated_amount_inwords_cf=''
    self.difference_amount_inword_cf=''
    if self.paid_amount:
        self.paid_amount_inwords_cf = money_in_words(self.paid_amount)
    if self.total_allocated_amount:
        self.total_allocated_amount_inwords_cf = money_in_words(self.total_allocated_amount)
    if self.unallocated_amount:
        self.unallocated_amount_inwords_cf = money_in_words(self.unallocated_amount)
    if self.difference_amount:
        self.difference_amount_inword_cf = money_in_words(self.difference_amount)                    