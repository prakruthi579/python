
from abc import ABC,abstractmethod 
class Payment(ABC):
    def __init__(self,payment_id,amount):
        self.payment_id=payment_id
        self.__amount=amount
        self.status="pending"
        self.__l=[]
    @abstractmethod
    def process_payment(self):
        pass
    def get_amount(self):
         return self.__amount
    def set_amount(self,amount):
         if amount>0:
           self.__amount=amount
         else:
              print("Amount should be greater than zero")
    def get_status(self):
         return self.status
    def display_transaction_history(self):
        if not self.__l:
            print("NO transcation history available")
            return
        for item in self.__l:
              print(item)
        
    def add_transhistory(self,method):
         self.__l.append(method)
    def refund_payment(self):
         if (self.status=="Completed"):
              self.status="Refunded"
              refunded_message="payment refunded successfully"
              print(refunded_message)
              self.add_transhistory(refunded_message)
         elif self.status=="Refunded":
              print("payment has already been refunded") 
         else:
              print("payment cannot be refunded before processing")
    def payment_summary(self):
         print(self.payment_id)
         print(self.get_amount())
         print(self.get_status())
         print(len(self.__l))
         
              
class CardPayment(Payment):
    def __init__(self,payment_id,amount,card_number):
        super().__init__(payment_id,amount)
        self.card_number=card_number
    
    def process_payment(self):
        if self.status=="pending":
            
            self.status="Completed"
            card=f"Card payment of {self.get_amount()} processed successfully"
            print(card)
            self.add_transhistory(card)
        else:
             print("Payment has already been completed")

class UPIPayment(Payment):
    def __init__(self,payment_id,amount,upi_id):
            super().__init__(payment_id,amount)
            self.upi_id=upi_id
    def process_payment(self):
            if self.status=="pending":
                self.status="Completed"
                upi=(f"UPI payment of {self.get_amount()} processed successfully")
                print(upi)
                self.add_transhistory(upi)
            else:
                print("Payment has already been completed")
            
class CashPayment(Payment):
     def process_payment(self):
             if self.status=="pending":
                self.status="Completed"
                cash=(f"Cash payment of {self.get_amount()} processed successfully")
                print(cash)
                self.add_transhistory(cash)
             else:
                print("Payment has already been completed")

class main():
     payments=[]
     while(True):
          print("1.create payment")
          print("2.process payment\n3.refund payment\n4.display history\n5.display summary\n6.exit")
          choice=int(input("enter  the choice: "))
          
          match (choice):
               case 1:
                    type=int(input("enter payment type :1.card 2.upi 3.cash"))
                    Payment_id=int(input("enter the payment id: "))
                    found=False
                    for pay in payments:
                        if pay.payment_id==Payment_id:
                            found=True
                            
                            break
                    if found:
                         print("duplicate Id")
                    else:

                        Amount=int(input("enter the amount: "))
                        if type==1:
                            
                                card_number=int(input("enter the card number: "))
                                payment=CardPayment(Payment_id,Amount,card_number)
                                payments.append(payment)
                                
                            
                        
                        elif type==2:
                            
                                upi_id=input("enter the upi_id: ")
                                payment=UPIPayment(Payment_id,Amount,upi_id)
                                payments.append(payment)
                                
                           
                                                    
                        elif type==3:
                            
                                    payment=CashPayment(Payment_id,Amount)
                                    payments.append(payment)
                        else:
                             print("Invalid choice")
               case 2:
                    if not payments:
                         print("No payments Available")
                         break
                    payment_id=int(input("enter the id to process:"))
                    for pay in payments:
                         if pay.payment_id==payment_id:
                           pay.process_payment()
                           break
                    else:
                         print("payment not found")
               case 3:
                    if not payments:
                         print("No payments Available")
                         break
                    payment_id=int(input("enter the id to process:"))
                    for pay in payments:
                         if pay.payment_id==payment_id:
                              pay.refund_payment()
                              break
                    else:
                         print("payment not found")
               case 4:
                    if not payments:
                         print("No payments Available")
                         break
                    payment_id=int(input("enter the id to process:"))
                    for pay in payments:
                         if pay.payment_id==payment_id:
                              pay.display_transaction_history()
                              break
                         else:
                              print("payment not found")
               case 5:
                    if not payments:
                         print("No payments Available")
                         break
                    payment_id=int(input("enter the id to process:"))
                    for pay in payments:
                         if pay.payment_id==payment_id:
                              pay.payment_summary()
                              break
                         else:
                              print("payment not found")
               case 6:
                    print("exited")
                    break
                    




                                    
                            
                                                        
                        






        