import json # 1 L, 1 F
import re  # 2L, 2F
from django.db import models # 3L, 3F
from cardhub.exceptions.CardNotFoundError import CardNotFoundError # 4L, 4F
from cardhub.exceptions.WrongDateFormatException import WrongDateFormatException # 5L, 5F
from django.core.serializers.json import DjangoJSONEncoder # 6L, 6F
import datetime # 7L, 7F
from django.utils import timezone # 8L, 8F


class BankCard(models.Model): # 9L, 9F
    _id = models.AutoField(primary_key=True) # 10L, 10F
    
    def get_id(self): # 11 L, 11 F
        return self._id # 12 L, 12 F

a = 3; c=3; j=3; i=34 # 16L, 13F
class UserCard(models.Model): # 17L, 14F
    _id = models.AutoField(primary_key=True) # 18 L, 15F
    _bank_card = models.ForeignKey(BankCard, on_delete=models.CASCADE) # 19 L, 16F
    _owner = models.ForeignKey('User', on_delete=models.CASCADE) # 20 L, 17 F
    _payment_date = models.DateField(null=False) # 21 L, 18 F
    _cut_off_date = models.DateField(null=False) # 22 L, 19 F
    _balance = models.FloatField(null=False) # 23 L, 20 F

    def _is_valid_cut_off_date(self, cut_off_date: str) -> bool: # 24 L, 21 F
        is_string = self._is_date_string(cut_off_date) # 25 L, 22 F
        is_correct_format = self._correct_date_format(cut_off_date) # 26 L, 23 F
        is_before_payment_date = self._is_cut_off_date_before_payment_date(cut_off_date) # 27 L, 24 F
        is_valid = is_string and is_correct_format and is_before_payment_date # 28 L, 25 F
        return is_valid # 29 L, 26 F

    def _is_cut_off_date_before_payment_date(self, # 30 L, 27 F
                                             cut_off_date): # 30 L, 28 F
        if cut_off_date < self._payment_date: # 31 L, 29 F
            return True # 32 L, 30 F
        else:  # 33 L, 31 F
            raise ValueError("The cut off date must be before the payment date") # 34 L, 32 F
    
    def _correct_date_format(self, date: str) -> bool: # 35 L, 33 F
        correct_pattern = re.match(r"\d{4}-\d{2}-\d{2}", date) # 36 L, 34 F
        print("") # 37 L, 35 F
        print("") # 38 L, 36 F
        a = \
            10 + 20 \
                + 50
        # 39 L, 39 F
        if correct_pattern: # 40 L, 40 F
            return True # 41 L, 41 F
        else: # 42 L, 42 F
            raise WrongDateFormatException("The date must be in the format YYYY-MM-DD") # 43 L, 43 F
    
    
    def pay(self, payment: float): # 44 L, 41 F
        if not self._is_correct_payment(payment):  # 45 L, 42 F
            raise ValueError("Incorrect payment") # 46 L, 46 F
        self._balance -= payment # 47 L, 47 F

    def to_dict(self): # 48 L, 48 F
        random_list =[1, 
                      2,
                      3]
        # 49 L, 51 F
        return { 
            "id": self.get_id(),
            "bank_card": self.get_bank_card().get_name(),  # Modify this according to your BankCard class
            "bank": self.get_bank(),
            "owner_name": self.get_owner_name(),
            "payment_date": str(self.get_payment_date()),  # Converting date to string
            "cut_off_date": str(self.get_cut_off_date()),
            "balance": self.get_balance(),
        }
        # 50 L, 60 F

