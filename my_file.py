import json # 1
import re  # 2
from django.db import models # 3
from cardhub.exceptions.CardNotFoundError import CardNotFoundError # 4 
from cardhub.exceptions.WrongDateFormatException import WrongDateFormatException # 5
from django.core.serializers.json import DjangoJSONEncoder # 6
import datetime # 7
from django.utils import timezone # 8


class BankCard(models.Model): # 9 
    _id = models.AutoField(primary_key=True) # 10
    
    def get_id(self): # 11
        return self._id # 12

class UserCard(models.Model): # 13
    _id = models.AutoField(primary_key=True) # 14
    _bank_card = models.ForeignKey(BankCard, on_delete=models.CASCADE) # 15
    _owner = models.ForeignKey('User', on_delete=models.CASCADE) # 16
    _payment_date = models.DateField(null=False) # 17
    _cut_off_date = models.DateField(null=False) # 18
    _balance = models.FloatField(null=False) # 19

    def _is_valid_cut_off_date(self, cut_off_date: str) -> bool: # 20
        is_string = self._is_date_string(cut_off_date) # 21
        is_correct_format = self._correct_date_format(cut_off_date) # 22
        is_before_payment_date = self._is_cut_off_date_before_payment_date(cut_off_date) # 23
        is_valid = is_string and is_correct_format and is_before_payment_date # 24
        return is_valid # 25

    def _is_cut_off_date_before_payment_date(self, cut_off_date): # 26
        if cut_off_date < self._payment_date: # 27
            return True # 28
        else:  # 29
            raise ValueError("The cut off date must be before the payment date") # 30
    
    def _correct_date_format(self, date: str) -> bool: # 31
        correct_pattern = re.match(r"\d{4}-\d{2}-\d{2}", date) # 32
        if correct_pattern: # 33
            return True # 34
        else: # 35
            raise WrongDateFormatException("The date must be in the format YYYY-MM-DD") # 36
    
    
    def pay(self, payment: float): # 37
        if not self._is_correct_payment(payment):  # 38
            raise ValueError("Incorrect payment") # 39
        self._balance -= payment # 40

    def to_dict(self): # 41
        return { # 42
            "id": self.get_id(),
            "bank_card": self.get_bank_card().get_name(),  # Modify this according to your BankCard class
            "bank": self.get_bank(),
            "owner_name": self.get_owner_name(),
            "payment_date": str(self.get_payment_date()),  # Converting date to string
            "cut_off_date": str(self.get_cut_off_date()),
            "balance": self.get_balance(),
        }
