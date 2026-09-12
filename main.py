import json
import datetime
import getpass
from decimal import Decimal,InvalidOperation

#------Load Section----

def load_accounts():
    with open("accounts.json","r")as file:
        return json.load(file)
        
    
def load_transactions():
    with open("transactions.json","r")as file:
        return json.load(file)
        

def load_requests():
    with open ("requests.json","r")as file:
        return json.load(file)
        

def load_admins():
    with open("admin.json","r")as file:
        return json.load(file)
    
def load_notifications():
    with open ("notifications.json","r") as file:
        return json.load(file)
        

############Save Section##########
def save_accounts(account_data):
    with open("accounts.json","w")as file:
        json.dump(account_data,file,indent=4)

def save_transactions(transaction_data):
    with open("transactions.json","w")as file:
        json.dump(transaction_data,file,indent=4)

def save_requests(request_data):
    with open("requests.json","w")as file:
        json.dump(request_data,file,indent=4)

def save_admins(admin_data):
    with open("admin.json","w")as file:
        json.dump(admin_data,file,indent=4)

def save_notifications(notification_data):
    with open("notifications.json","w")as file:
        json.dump(notification_data,file,indent=4)

###################Main Flow#################
class BankSystem:

    #---Data Section----
    def __init__(self,account_data,transaction_data,request_data,admin_data,notification_data):
        self.account_data=account_data
        self.transaction_data=transaction_data
        self.request_data=request_data
        self.admin_data=admin_data
        self.notification_data=notification_data

        # Session Attributes #After User Choose their Current Account
        self.current_customer=None
        self.current_account=None

    # ---Main Menu Section---
    def main_menu(self):
        while True:
            print("="*60)
            print("                     BANK MANAGEMENT SYSTEM")
            print("="*60)
            print()
            print("1. Customer Portal\n\n2. Admin Portal\n\n3. Exit")
            print()
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.customer_portal()
                continue
            elif choice==2:
                self.admin_portal()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")

    # After User Choose Customer Portal

    def customer_portal(self):
        while True:
            self.menu_format("CUSTOMER PORTAL","1. Create New Account\n\n2. Login\n\n3. Search Account\n\n4. Back\n")
        
            customer_portal_choice=self.menu_choice_validations(1,4)
            if customer_portal_choice==1:
                result,account_details=self.create_account()
                print("="*60)
                print()
                if result=="cancelled":
                    print("Account creation cancelled.")
                   
                elif result=="failed":
                    print("Account Creation Failed.")
                elif result=="success":
                    self.display_account_created(account_details)
                else:
                    print("Unexpected account creation status.")
            
            elif customer_portal_choice==2:

                login_result,last_login=self.customer_login()
                if login_result=="failure":
                    continue
                elif login_result=="success":
                    customer_accounts=self.handle_post_login_accounts()
                    if len(customer_accounts)==1 :
                        self.current_account=customer_accounts[0]
                        self.display_login_details(last_login)
                        self.handle_notification_popup()
                        self.account_status_check()
                    elif len(customer_accounts)>1:
                        self.display_customer_accounts(customer_accounts)
                        self.display_login_details(last_login)
                        self.handle_notification_popup()
                        self.account_status_check()
            elif customer_portal_choice==3:
                self.search_accounts_customer_portal()
                continue
            elif customer_portal_choice==4:
                break
            else:
                print("Invalid Choice!")


    # ADmin Portal
    def admin_portal(self):
        while True:
            self.menu_format("ADMIN PORTAL","1. Login\n\n2. Back\n")
            
            admin_portal_choice=self.menu_choice_validations(1,2)
            if admin_portal_choice==1:
                self.login_admin()
                self.admin_dashboard()
                continue
            elif admin_portal_choice==2:
                break
            else:
                print("Invalid Choice!")

    # Customer Dashboard

    def customer_dashboard(self):
        while True:
            self.menu_format("CUSTOMER DASHBOARD","1. View Profile\n\n2. Check Balance\n\n3. Deposit Money\n\n4. Withdraw Money\n\n5. Transfer Money\n\n6. Notifications\n\n7. Transaction History\n\n8. Service Center\n\n9. Change PIN\n\n10. Switch Account\n\n11. Logout")
            customer_dashboard_choice=self.menu_choice_validations(1,11)
            
            if customer_dashboard_choice==1:
                self.view_customer_profile()
                continue

            elif customer_dashboard_choice==2:
                self.check_balance()
                continue
            
            elif customer_dashboard_choice==3:
                result=self.is_account_active()
                if not result:
                    print("This account is currently inactive.")
                    break
                self.deposit_display_Screen()
                self.payment_methods()
                continue
            
            elif customer_dashboard_choice==4:
                result=self.is_account_active()
                if not result:
                    print("This account is currently inactive.")
                    break
                self.withdraw_display_screen()
                self.withdraw_payment_methods()
                continue
            elif customer_dashboard_choice==5:
                self.transfer_money()
                continue
            elif customer_dashboard_choice==6:
                self.notification_menu()
                continue
            elif customer_dashboard_choice==7:
                self.transaction_history_menu()
                continue
            elif customer_dashboard_choice==8:
                self.service_center_screen()
                continue
            elif customer_dashboard_choice==9:
                self.change_pin()
                continue
            elif customer_dashboard_choice==10:
                self.switch_accounts()
                continue
            elif customer_dashboard_choice==11:
                break
            else:
                print("Invalid Choice!")   
                
    # Admin Dashboard

    def admin_dashboard(self):
        while True:
        
            self.menu_format("ADMIN DASHBOARD","1. Admin Profile\n\n2. Request Management ⭐\n\n3. Customer Management\n\n4. Account Management\n\n5. Transaction Management\n\n6. Notifications\n\n7. Change Password\n\n8. Logout\n")
            admin_dashboard_choice=self.menu_choice_validations(1,8)
            if admin_dashboard_choice==1:
                self.profile()
                continue
            elif admin_dashboard_choice==2:
                self.request_management()
                continue
            elif admin_dashboard_choice==3:
                self.customer_management()
                continue
            elif admin_dashboard_choice==4:
                self.account_management()
                continue
            elif admin_dashboard_choice==5:
                self.transaction_management()
                continue
            elif admin_dashboard_choice==6:
                self.notification_management_system()
                continue
            elif admin_dashboard_choice==7:
                self.change_password_admin()
                continue
            elif admin_dashboard_choice==8:
                break
            else:
                print("Invalid Choice!")
        
    #validation Part

    @staticmethod
    def name_validation(new_name):
        if not isinstance(new_name,str):
            return False
        elif not new_name.strip():
            return False
        elif len(new_name)<3 or len(new_name)>50:
            return False
        elif not all(ch.isalpha() or ch.isspace() for ch in new_name) :
            return False
        elif "  " in new_name:
            return False
        else:
            return True

    @staticmethod
    def phone_number_validation(new_number):
        if not isinstance(new_number,str):
            return False
        elif len(new_number)!=10:
            return False
        elif not new_number.isdigit():
            return False
        elif  new_number[0] not in ["6","7","8","9"]:
            return False
        else:
            return True

    @staticmethod
    def email_validation(new_email):
        if not isinstance(new_email,str):
            return False
        if len(new_email)<5 or len(new_email)>100:
            return False
        if any(ch.isspace() for ch in new_email):
            return False
        if new_email.startswith("@") or new_email.startswith("."):
            return False
        if new_email.endswith(".") :
            return False
        domain=new_email.split("@")
        if len(domain)!=2:
            return False
        if not domain[1] or not any (ch=="." for ch in domain[1]) or domain[1][0]==".":
            return False
        
        return True

    @staticmethod
    def address_validation(new_address):
        if not isinstance(new_address,str):
            return False
        clean_address=new_address.strip()
        if not clean_address:
            return False
        if len(clean_address)<5 or len(clean_address)>200:
            return False
        
        return True
        

    @staticmethod
    def amount_validation(new_amount):
        try:
            value=Decimal(str(new_amount))
        except InvalidOperation:
            return False
        if value<=0:
            return False
        
        if value>=100000000:
            return False
        if abs(value.as_tuple().exponent)>2:
            return False
        return True

    @staticmethod
    def pin_validation(new_pin):
        if not isinstance(new_pin,str):
            return False
        if not new_pin.isdigit():
            return False
        if len(new_pin)!=4:
            return False
        return True
    
    @staticmethod            
    def upi_id_validation(new_upi_id):
        if not isinstance(new_upi_id,str):
            return False
        if not new_upi_id.strip():
            return False
        if any(ch.isspace() for ch in new_upi_id):
            return False
        if len(new_upi_id)<5 or len(new_upi_id)>50:
            return False
        upi=new_upi_id.split("@")
        if len(upi)!=2:
            return False
        if upi[0]=="" or upi[1]=="":
            return False
        else:
            return True
        
    @staticmethod
    def cheque_number_validation(new_cheque_number):
        if not isinstance(new_cheque_number,str):
            return False
        if not new_cheque_number.isalnum():
            return False
        if any(ch.isspace() for ch in new_cheque_number):
            return False
        if len(new_cheque_number)<8 or len(new_cheque_number)>30:
            return False
        else:
            return True

    
    #Customer Existing or Not Check

    # 1        
    def Find_Existing_Customer(self,phone_number,email):
       
        for customers in self.account_data["customers"]:
            if phone_number==customers["Phone_Number"] and email==customers["Email"]:
                return customers
        return
    # 2
    def Check_Existing_Account(self,customer,bank_details):
        customer_id=customer["Customer_ID"]
        if  not bank_details:
            return
        bank_name,_,branch_name,_,account_type,_=bank_details #when you need specific thing froma afull of bag
        for accounts in self.account_data["accounts"]:
            if customer_id==accounts["Customer_ID"] and bank_name==accounts["Bank_Name"] and branch_name==accounts["Branch_Name"] and account_type==accounts["Account_Type"]:
                return True
        return False

        
     #---Choice Validation---
    def menu_format(self,menu_heading,message):
        print("="*30,end="")
        print(f" {menu_heading} ",end="")
        print("="*25)
        print()
        print(message)
        print("="*60)

    def menu_choice_validations(self,min_choice,max_choice,message="Enter Your Choice :"):
        while True:
            try:
                choice=int(input(message))
            except ValueError:
                print("Invalid Menu Choice!")
                continue
            if choice >=min_choice and choice<=max_choice:
                return choice
            print("Invalid Menu Choice!")
        
    def bank_menu_format(self,menu_heading):
        print("="*30,end="")
        print(f" {menu_heading} ",end="")
        print("="*25)
        print()

    #masking account number
    def mask_account_number(self,account_number):
        last_4_digit=account_number[-4:]
        number_of_stars=len(account_number)-4
        return number_of_stars*"X"+last_4_digit
    
    #Masking Cheque Number
    def mask_cheque_number(self,cheque_number):
        last_4_digit=cheque_number[-4:]
        number_of_star=len(cheque_number)-4
        return number_of_star*"X"+last_4_digit
    # Chooose Bank , Branch ,Account Type 
    def bank_selection(self):
        self.bank_menu_format(" SELECT BANK ")
        banks=self.account_data["configuration"]["banks"]
        
        bank_names=list(banks.keys())
        bank_name_menu=bank_names+["Back"]

        for number,bank in enumerate(bank_name_menu,start=1):
            print(f"{number}. {bank}\n")
        print("="*60)
        

        bank_choice=self.menu_choice_validations(1,len(bank_name_menu))
        
        if bank_choice==len(bank_name_menu):
            return
        
        bank_name=bank_name_menu[bank_choice-1]

        bank_code=banks[bank_name]["Bank_Code"]

        self.bank_menu_format(" SELECT BRANCH ")

        branches=self.account_data["configuration"]["banks"][bank_name]["branches"]
        branch_names=list(branches.keys())

        branch_name_menu=branch_names+["Back"]
        
        for number,branch in enumerate(branch_name_menu,start=1):
                print(f"{number}. {branch}\n")
        print("="*60)

        bank_branch_choice=self.menu_choice_validations(1,len(branch_name_menu))

        if bank_branch_choice==len(branch_name_menu):
                return
        branch_name=branch_name_menu[bank_branch_choice-1]

        branch_code=branches[branch_name]["Branch_Code"]

        self.bank_menu_format(" ACCOUNT TYPE ")

        account_types=self.account_data["configuration"]["banks"][bank_name]["branches"][branch_name]["account_types"]
        account_types_list=list(account_types.keys())

        account_type_menu=account_types_list+["Back"]

        for number,account_type in enumerate(account_type_menu,start=1):
            print(f"{number}. {account_type}\n")
        print("="*60)

        account_type_choice=self.menu_choice_validations(1,len(account_type_menu))

        if account_type_choice==len(account_type_menu):
            return
        account_type=account_type_menu[account_type_choice-1]

        account_information=account_types[account_type]
        return bank_name,bank_code,branch_name,branch_code,account_type,account_information
             
    
    # Create Account
    def create_account(self):
        bank_details=self.bank_selection()
        if  not bank_details:
            return "cancelled",None
        bank_name,bank_code,branch_name,branch_code,account_type,account_information=bank_details
        created_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") 
        
        while True:
            phone_number=input("Enter Phone Number : ")
            if not self.phone_number_validation(phone_number):
                print("Invalid Phone Number!")
                continue
            break

        while True:
            email=input("Enter Email :")
            if not self.email_validation(email):
                print("Invalid Email ID!")
                continue
            break
        customer=self.Find_Existing_Customer(phone_number,email)
        if customer and self.Check_Existing_Account(customer, bank_details):
            print(f"You already have a {account_type} account in this bank and branch.")
            return "failed",None
            
        if customer:
            customer_code = customer["Customer_ID"]
            
        else:
            while True:
                full_name=input("Enter Full Name:")
                if not self.name_validation(full_name):
                    print("Invalid Full Name!")
                    continue
                break
    
            while True:
                address=input("Enter Address: ")
                if not self.address_validation(address):
                    print("Invalid Address!")
                    continue
                break
            while True:
                
                pin=input("Create 4-digit PIN: ")
                if not self.pin_validation(pin):
                    print("Invalid PIN!")
                    continue
                break
            while True:
                print("(Password input is hidden for security. Type and press Enter.)")
                confirm_pin=getpass.getpass("Please Re Enter The PIN:")
                if confirm_pin!=pin:
                    print("PIN Not Match!")
                    continue
                break

            customer_code="C00000"+str(self.account_data["system"]["next_customer_id"])
            
            customer_details={
            "Customer_ID":customer_code,
            "Full_Name":full_name,
            "Phone_Number":phone_number,
            "Email":email,
            "Address":address,
            "PIN":pin,
            "Created_Date":created_date,
            "Last_Login":"",
            "Account_Status":"ACTIVE"

            }
            self.account_data["customers"].append(customer_details)
            self.account_data["system"]["next_customer_id"]+=1

        while True:
            
            initial_deposit=input("Enter Initial Deposit Amount: ")
            
            if  not self.amount_validation(initial_deposit):
                print("Invalid Initial Deposit Amount!")
                continue
            initial_deposit=Decimal(initial_deposit)
            break
        seq = account_information["Next_Account_Sequence"]
        account_number = f"{bank_code}{branch_code}{account_information['Account_Type_Code']}000{seq}"
        
        
        
        account_details={
            "Customer_ID":customer_code,
            "Bank_Name":bank_name,
            "Branch_Name":branch_name,
            "Account_Type":account_type,
            "Account_Number":account_number,
            "Balance":str(initial_deposit),
            "Created_Date":created_date,
            "Last_Updated":created_date,
            "Account_Status":"ACTIVE"
        }

        
        
        self.account_data["accounts"].append(account_details)
        account_information["Next_Account_Sequence"]+=1
        self.save_account_data()

        
        return "success",account_details
    

    # --------------------Display After ACcount Creation---------------------------
    def display_account_created(self,account_details):
        
        print("="*60)
        print("          ACCOUNT CREATED SUCCESSFULLY")
        print("="*60)
        
        
        print(f"\nCustomer ID    : {account_details['Customer_ID']}\n")
        print(f"Account Number : {self.mask_account_number(account_details['Account_Number'])}")
    
        print(f"Bank           : {account_details['Bank_Name']}")
        print(f"Branch         : {account_details['Branch_Name']}")
        print(f"Account Type   : {account_details['Account_Type']}\n")
        print("-" * 60)
        print("Use your Customer ID and PIN to log in.\n")
        print("⚠ Please save your Customer ID and Account Number carefully.")
        print("✓ Your PIN will never be displayed by the system.")
        print("If you forget your Customer ID or PIN, use the appropriate recovery options")
        print("-" * 60)
            
    #-------------------customer Login--------------
    # 1
    def customer_login(self):
        chances=3
        
        while chances>0:
            print("="*60)
            print("                      CUSTOMER LOGIN")
            print("="*60)
            
            customer_id_verification=input("Customer ID : ")
            print()
            print("(Password input is hidden for security. Type and press Enter.)")

            pin_verification=getpass.getpass("PIN : ")

            print()
            print("-"*60)
            print()
            
            for data in self.account_data["customers"]:
                if customer_id_verification==data["Customer_ID"] and pin_verification==data["PIN"]:
                    print("Login Successful.")
                    self.current_customer=data
                    last_login=self.current_customer["Last_Login"]
                    self.current_customer["Last_Login"]=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                    self.save_account_data()
                    return "success",last_login
            
            print("Invalid Customer ID or PIN.")
            chances-=1
            continue
        
        print("Maximum login attempts reached.")
        return "failure",None
    
    ### ######
    # 2
    def handle_post_login_accounts(self):
        
        customer_accounts=[]
        for accounts in self.account_data["accounts"]:
            if accounts["Customer_ID"]==self.current_customer["Customer_ID"]:
                customer_accounts.append(accounts)
                
        return customer_accounts
        
    # -----------------For Multiple Accounts-------------------
    
    def display_customer_accounts(self,customer_accounts):
        print("="*60)
        print("                  SELECT AN ACCOUNT")
        print("="*60)
        
        for  number,accounts in enumerate(customer_accounts,start=1):
            print()
            print(f"{number}.")
            print(f"Bank           : {accounts['Bank_Name']}")
            print(f"Branch         : {accounts['Branch_Name']}")
            print(f"Account Type   : {accounts['Account_Type']}")
            print(f"Account Number : {self.mask_account_number(accounts['Account_Number'])}")
            print("-"*60)
        choice=self.menu_choice_validations(1,len(customer_accounts))
        selected_account=customer_accounts[choice-1]
        self.current_account=selected_account
        
    # # ------------After Login Display Accounts--------------------
    def display_login_details(self,last_login):
        
        print("="*60)
        print(f"Welcome, {self.current_customer['Full_Name']}\n")
        print(f"Customer ID     : {self.current_customer['Customer_ID']}\n")
        print("-"*60)
        print(f"Bank            : {self.current_account['Bank_Name']}")
        print(f"Branch          : {self.current_account['Branch_Name']}")
        print(f"Account Type    : {self.current_account['Account_Type']}")
        print(f"Account Number  : {self.mask_account_number(self.current_account['Account_Number'])}\n")
        if last_login=="":
            print("Last Login      : First Login\n")
        else:
            print(f"Last Login     : {last_login}\n")
        print("="*60)
    # Check Account is Active or not 

    def account_status_check(self):
        if self.current_account['Account_Status']=="ACTIVE":
            self.customer_dashboard()
        else:
            self.inactive_account_menu()
    # Display Menu For Inactive Accounts
    def inactive_account_menu(self):
        while True:
            print("="*60)
            print("                       ACCOUNT IS INACTIVE")
            print("="*60)
            print("\nThis account is currently inactive.\n")
            print("1. View Profile\n\n2. Switch Account\n\n3. Exit")
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.view_profile()
                continue
            elif choice==2:
                self.switch_accounts()
                continue
            elif choice==3:
                return
        
    # Switch Accounts
    def switch_accounts(self):
        customer_accounts=self.handle_post_login_accounts()
        if len(customer_accounts)==1:
            self.single_user_switch_account_display()
            return 
        else:
            self.display_customer_accounts(customer_accounts)
            print("\nAccount switched successfully.\n")
            self.display_login_details(self.current_customer["Last_Login"])
            self.handle_notification_popup()
            self.account_status_check()
            
    # For Single User account Display
    def single_user_switch_account_display(self):
        print("="*60)
        print("                         SWITCH ACCOUNT")
        print("="*60)
        print("\nYou have only one account.\n")
        print("Account switching is not available.\n")


    #Search Accounts
    def search_accounts_customer_portal(self):
        while True:
            print('='*60)
            print("                            SEARCH ACCOUNT")
            print("="*60)
            print("\n1. Search By Phone Number\n\n2. Search By Account Number\n\n3. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.search_by_phone_number_before_login()
                continue
            elif choice==2:
                self.search_by_account_number_before_login()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
    
    def search_by_phone_number_before_login(self):
        while True:
            phone_number=input("Enter Phone Number : ")
            if not self.phone_number_validation(phone_number):
                print("Invalid Phone Number!")
                continue
            break
        customer_detail=None
        for customer in self.account_data['customers']:
            if phone_number==customer['Phone_Number']:
                customer_detail=customer
                break
        if customer_detail is None:
            print("No customer found.")
            return

        account_list=[]
        
        for accounts in self.account_data['accounts']:
            if customer_detail['Customer_ID']==accounts['Customer_ID']:
                account_list.append(accounts)
        if not account_list:
            print("No account found.")
            return
        
            
        if len(account_list)==1:
            self.display_account_details(customer_detail,account_list[0])
        elif len(account_list)>1:
            print('='*60)
            print("            SELECT ACCOUNT")
            print("="*60)
            print(f"\nCustomer Name     : {customer_detail['Full_Name']}\n")
            for number,found_account in enumerate(account_list,start=1):
                
                print(f"{number}. Account Number : {self.mask_account_number(found_account['Account_Number'])}")
                print(f"Bank                     : {found_account['Bank_Name']}")
                print(f"Account Type             : {found_account['Account_Type']}\n")
            print("="*60)
            print("Select an account to view details:")
            print()
            max_choice=len(account_list)
            choice=self.menu_choice_validations(1,max_choice)
            selected_account=account_list[choice-1]
            self.display_account_details(customer_detail,selected_account)
        
    def display_account_details(self,customer_detail,selected_account):
        print("="*60)
        print("                          ACCOUNT DETAILS")
        print("="*60)
        
        print(f"\nCustomer Name : {customer_detail['Full_Name']}\n")
        print(f"Account Number  : {self.mask_account_number(selected_account['Account_Number'])}")
        print(f"Bank            : {selected_account['Bank_Name']}")
        print(f"Branch          : {selected_account['Branch_Name']}")
        print(f"Account Type    : {selected_account['Account_Type']}")
        print(f"Status          : {selected_account['Account_Status']}")
        print(f"Created Date    : {selected_account['Created_Date']}")
        print('='*60)
    
    
    def search_by_account_number_before_login(self):
        
        account_number=input("Enter Account Number : ").strip()
         
        found=False
        for accounts in self.account_data['accounts']:
            if account_number==accounts['Account_Number']:
                found=True
                
                
                for customers in self.account_data['customers']:
                    if accounts['Customer_ID']==customers['Customer_ID']:
                        self.display_account_details(customers,accounts)
                        return
        if not found:
            print("Account not found!")
            return
    

    #### -------------View Profile-----------------------
    def view_customer_profile(self):
        print("="*60)
        print("                 CUSTOMER PROFILE")
        print("="*60)
        print("\nCustomer Information")
        print("-"*60)
        print(f"Full Name        : {self.current_customer['Full_Name']}")
        print(f"Phone Number     : {self.current_customer['Phone_Number']}")
        print(f"Customer ID      : {self.current_customer['Customer_ID']}")
        print(f"Email            : {self.current_customer['Email']}")
        print(f"Address          : {self.current_customer['Address']}")
        print(f"Created Date     : {self.current_customer['Created_Date']}")
        print(f"Last Login       : {self.current_customer['Last_Login']}")
        print(f"Status           : {self.current_customer['Account_Status']}\n")
        print("-"*60)
        print("\nAccount Information")
        print("-"*60)
        print(f"Bank             : {self.current_account['Bank_Name']}")
        print(f"Branch           : {self.current_account['Branch_Name']}")
        print(f"Account Type     : {self.current_account['Account_Type']}")
        print(f"Account Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Balance          : ₹{self.current_account['Balance']}")
        print(f"Created Date     : {self.current_account['Created_Date']}")
        print(f"Last Updated     : {self.current_account['Last_Updated']}")
        print(f"Account Status   : {self.current_account['Account_Status']}\n")
        print("-"*60)


    # Check Balance    
    def check_balance(self):
        print("="*60)
        print("                       BALANCE DETAILS")
        print("="*60)
        print(f"\nAccount Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank               : {self.current_account['Bank_Name']}")
        print(f"Branch             : {self.current_account['Branch_Name']}")
        print(f"Account Type       : {self.current_account['Account_Type']}\n")
        print("-"*60)
        print(f"Available Balance  : ₹{self.current_account['Balance']}")
        print("-"*60)
        print(f"\nLast Updated     : {self.current_account['Last_Updated']}\n")
        print("="*60)
        
    
    # Deposit Balance  menu screen  
    def deposit_display_Screen(self):
        print("="*60)
        print("                      DEPOSIT MONEY")
        print("="*60)
        print("\nAccount Information")
        print("-"*60)
        print(f"Customer ID    : {self.current_account['Customer_ID']}")
        print(f"Account Number : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank           : {self.current_account['Bank_Name']}")
        print(f"Branch         : {self.current_account['Branch_Name']}")
        print(f"Account Type   : {self.current_account['Account_Type']}")
        
        print(f"Current Balance: ₹{self.current_account['Balance']}")
        last_updated=self.current_account["Last_Updated"]
        print(f"Last Updated   : {last_updated}\n")
        print("="*60)
        
    # Better Security 
    def is_account_active(self):
        return self.current_account["Account_Status"]=="ACTIVE"

    # Deposit Method       
    def payment_methods(self):
        while True:
            print("Select Deposit Method\n"+"="*60+"\n1. Cash\n\n2. UPI\n\n3. Back\n")
            print("="*60)
            print()
        
            payment_method=self.menu_choice_validations(1,3)
            if payment_method==1:
                cash_transaction=self.deposit_methods("cash")
                if cash_transaction is None:
                    continue
                self.display_deposit_result(cash_transaction,"cash")
                break
            elif payment_method==2:
                upi_transaction=self.deposit_methods("upi")
                if upi_transaction is None:
                    continue
                self.display_deposit_result(upi_transaction,"upi")
                break
            elif payment_method==3:
                break
            
    # Store in  Transaction 
    def deposit_methods(self,method_name):
        while True:
            
            amount=input("Enter Deposit Amount :")
            
            if not self.amount_validation(amount):
                print("Invalid Amount!")
                continue
            amount=Decimal(amount)
            break

        while True:
            confirm=input("Confirm Deposit? (Y/N) ").strip().upper()
            if confirm not in ["Y","N"]:
                print("Invalid Confirmation!")
            else:
                if confirm=="Y":
                    transaction_id=f"TXN{self.account_data['system']['next_transaction_id']:06d}"
                    self.current_account["Last_Updated"]=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                    balance=Decimal(self.current_account['Balance'])
                    
                    new_balance=balance+amount 
                    self.current_account['Balance']=str(new_balance)
                

                    transaction={
                        "Transaction_ID" : transaction_id,
                        "Customer_ID"    : self.current_customer['Customer_ID'],
                        "Account_Number" : self.current_account['Account_Number'],
                        "Type"           : "DEPOSIT",
                        "Method"         : method_name.upper(),
                        "Amount"         : str(amount),
                        "Status"         : "SUCCESS" ,
                        "Balance_Before" : str(balance),
                        "Balance_After"  : str(new_balance) ,
                        "Time_Stamp"     : self.current_account['Last_Updated']
                    }
                    mode_data=self.mode_id_validation(method_name,"Deposit")
                    if method_name=='upi':
                        transaction['UPI_ID']=mode_data
                    
                    self.transaction_data["transactions"].append(transaction)
                    self.account_data["system"]["next_transaction_id"]+=1
                    self.save_transaction_data()
                    self.save_account_data()
                    return transaction
                elif confirm=="N":
                    print("Deposit cancelled.")
                    return None
    # Each Method Ask Valid ID
    def mode_id_validation(self,mode_name,method):
        if mode_name=="cash":
            return 
    
        elif mode_name=="upi":
            while True:
                upi_id=input("Enter UPI ID : ")
                if not self.upi_id_validation(upi_id):
                    print("UPI ID is Invalid!")
                    continue
                break
            return upi_id
        else:
            print(f"Invalid {method} Method!")
    # After Deposit Display Deposit Screen
    def display_deposit_result(self,transaction,method_name):
        print("="*60)
        print("                      DEPOSIT SUCCESSFUL")
        print("="*60)
        print(f"\nTransaction ID : {transaction['Transaction_ID']}")
        print(f"Customer ID      : {transaction['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(transaction['Account_Number'])}\n")
        print("-"*60)
        print("\nTransaction Info")
        print("-"*60)
        print(f"Type             : {transaction['Type']}")
        if method_name=="upi":
            print(f"UPI ID       : {transaction['UPI_ID']}")
        elif method_name=="cash":
            pass

        print(f"Method           : {transaction['Method']}\n")
        print(f"Amount Deposited : {transaction['Amount']}")
        print(f"Status           : {transaction['Status']}\n")
        print("-"*60)
        print("Account Snapshot")
        print("-"*60)
        print(f"Previous Balance : {transaction['Balance_Before']}")
        print(f"Current Balance  : {transaction['Balance_After']}")
        print(f"Last Updated     : {transaction['Time_Stamp']}\n")
        print("="*60)
        print("Thank you for banking with us!")
        print("="*60)
        
    

    #####withdraw section
    def withdraw_display_screen(self):
        print("="*60)
        print("                           WITHDRAW MONEY")
        print("="*60)
        print("\nAccount Information")
        print("-"*60)
        print(f"Customer ID       : {self.current_account['Customer_ID']}")
        print(f"Account Number    : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank              : {self.current_account['Bank_Name']}")
        print(f"Branch            : {self.current_account['Branch_Name']}")
        print(f"Account Type      : {self.current_account['Account_Type']}")
        print(f"Available Balance : ₹{self.current_account['Balance']}")
        print(f"Last Updated      : {self.current_account['Last_Updated']}")
        print("="*60)
        print("\n⚠ Minimum account balance must be ₹500")
        print("⚠ Minimum Withdrawl  Amount is ₹100.")
        print("⚠ Daily withdrawl limit ₹20,000")
        print("="*60)

    


    # Withdraw Method       
    def withdraw_payment_methods(self):
        while True:
            print("Select Withdraw Method\n"+"="*60+"\n1. Cash\n\n2. UPI\n\n3. Back\n")
            print("="*60)
            print()
        
            payment_method=self.menu_choice_validations(1,4)
            if payment_method==1:
                result_message,result=self.withdraw_methods("cash")
                if result_message=="cancelled":
                    print("WIthdrawl Cancelled!")
                elif result_message=="failed":
                    print("Withdrawl Failed !")
                elif result_message=="success":
                    self.display_withdraw_result(result,"cash")
                    break
            elif payment_method==2:
                result_message,result=self.withdraw_methods("upi")
                
                if result_message=="cancelled":
                    print("WIthdrawl Cancelled!")
                elif result_message=="failed":
                    print("Withdrawl Failed !")
                elif result_message=="success":
                    self.display_withdraw_result(result,"upi")
                    break
            
            elif payment_method==3:
                break

    # Store in  Transaction 
    def withdraw_methods(self,method_name):
        balance=Decimal(self.current_account['Balance'])
        today=datetime.datetime.now().date()
        while True:
            
            amount=input("Enter Withdrawl Amount: ₹ ")
            
            if not self.amount_validation(amount):
                print("Invalid Amount!")
                continue
            amount=Decimal(amount)
            #minimum withdrawl check
            if amount<100:
                print("Minimum Withdrawl  Amount is ₹100.")
                continue
            if balance-amount<500:
                print("Minimum Balance in your Account Must be ₹500.")
                continue
            today_total=0
            for transaction in self.transaction_data['transactions']:
                date_object=datetime.datetime.strptime(transaction['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
                date=date_object.date()
                if self.current_account['Account_Number']==transaction.get('Account_Number') and today==date and transaction['Type']=="WITHDRAW" and transaction['Status']=="SUCCESS":
                    today_total+=Decimal(transaction['Amount'])
            
            if today_total+amount>20000:
                print("You Reached to your Daily Limit.")
                continue
            break


        while True:
            confirm=input("Confirm Withdrawal? (Y/N) ").strip().upper()
            if confirm not in ["Y","N"]:
                print("Invalid Confirmation!")
                continue
            else:
                if confirm=="N":
                    return "cancelled",None
                elif confirm=="Y":
                    print("="*60)
                    print("                SECURITY VERIFICATION")
                    print("="*60)
                    print("(Password input is hidden for security. Type and press Enter.)")
                    pin_verification=getpass.getpass("Enter Your 4-Digit PIN: ")
                    if pin_verification!=self.current_customer['PIN']:
                        print("Invalid Pin")
                        return "failed",None
                
                    transaction_id=f"TXN{self.account_data['system']['next_transaction_id']:06d}"
                    self.current_account["Last_Updated"]=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                    
                    new_balance=balance-amount
                    self.current_account['Balance']=str(new_balance)

                    transaction={
                        "Transaction_ID" : transaction_id,
                        "Customer_ID"    : self.current_customer['Customer_ID'],
                        "Account_Number" : self.current_account['Account_Number'],
                        "Type"           : "WITHDRAW",
                        "Method"         : method_name.upper(),
                        "Amount"         : str(amount),
                        "Status"         : "SUCCESS" ,
                        "Balance_Before" : str(balance),
                        "Balance_After"  : str(new_balance) ,
                        "Time_Stamp"     : self.current_account['Last_Updated']
                    }
                    mode_data=self.mode_id_validation(method_name,"WiTHDRAW")
                    if method_name=='upi':
                        transaction['UPI_ID']=mode_data
                    
                    self.transaction_data["transactions"].append(transaction)
                    self.account_data["system"]["next_transaction_id"]+=1
                    self.save_transaction_data()
                    self.save_account_data()
                    return "success",transaction
    # After Withdraw Display  Screen
    def display_withdraw_result(self,transaction,method_name):
        print("="*60)
        print("                       WITHDRAW  SUCCESSFUL")
        print("="*60)
        print(f"\nTransaction ID   : {transaction['Transaction_ID']}")
        print(f"Customer ID      : {transaction['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(transaction['Account_Number'])}\n")
        print("-"*60)
        print("\nTransaction Info")
        print("-"*60)
        print(f"Type             : {transaction['Type']}")
        if method_name=="upi":
            print(f"UPI ID          : {transaction['UPI_ID']}")
        
        elif method_name=="cash":
            pass

        print(f"Method           : {transaction['Method']}\n")
        print(f"Amount Withdrawn : {transaction['Amount']}")
        print(f"Status           : {transaction['Status']}\n")
        print("-"*60)
        print("Account Snapshot")
        print("-"*60)
        print(f"Previous Balance : {transaction['Balance_Before']}")
        print(f"Current Balance  : {transaction['Balance_After']}")
        print(f"Last Updated     : {transaction['Time_Stamp']}\n")
        print("="*60)
        print("Thank you for banking with us!")
        print("="*60)
        
                
    # Transfer Money Section

    #1
    def transfer_money(self):
        while True:
            print("="*60)
            print("                      TRANSFER MONEY")
            print("="*60)
            print("\nSender Account\n")
            print(f"Name            : {self.current_customer['Full_Name']}\n")
            print(f"Account Number  : {self.mask_account_number(self.current_account['Account_Number'])}\n")
            print(f"Current Balance : ₹{self.current_account['Balance']}\n")
            print('-'*60)
            accounts,customer=self.get_receiever_account()
            amount=self.get_transfer_amount()
            result=self.confirm_transfer(customer,amount)
            if result=="cancelled":
                print("Transfer Cancelled!")
                print("="*60)
                print("1. Try Again\n\n2. Customer Dashboard")
                choice=self.menu_choice_validations(1,2)
                if choice==1:
                    continue
                elif choice==2:
                    break
            elif result=="success":
                self.process_transfer(amount,accounts)
                transaction=self.save_transfer_transaction(accounts,customer,amount)
                notification1,notification2=self.create_transfer_notification(transaction,accounts)
                again=self.transfer_success_screen(transaction)
                if again==1:
                    continue
                elif again==2:
                    break
    #2
    def get_receiever_account(self):
        while True:
            receiever_account_number=input("Enter Receiver Account Number:").strip()
            receiver_customer=None
            found=False
            for receiver_accounts in self.account_data["accounts"]:
                if receiever_account_number==receiver_accounts['Account_Number']:

                    found=True
                    if receiver_accounts['Account_Number'] == self.current_account['Account_Number']:
                        print("You cannot transfer to your own same account.")
                        break
                    customer_id=receiver_accounts['Customer_ID']
                    for customer in self.account_data['customers']:
                        if customer['Customer_ID']==customer_id:
                            receiver_customer=customer
                            break
                    if receiver_customer is None:
                        print("Receiver customer details not found.")
                        continue
                    print('-'*60)
                    receiver_name=receiver_customer['Full_Name']
                    print("Receiver Details\n")
                    print(f"Receiver Name : {receiver_name}\n")
                    print(f"Bank Name     : {receiver_accounts['Bank_Name']}\n")
                    print(f"Branch Name   : {receiver_accounts['Branch_Name']}\n")
                    print(f"Account Type  : {receiver_accounts['Account_Type']}\n")
                    print('-'*60)
                    
                    return receiver_accounts,receiver_customer
                    
            if not found:
                print("Account not found.")


    #3
    def get_transfer_amount(self):
        while True:
            balance=Decimal(self.current_account['Balance'])
            amount=input("Enter Transfer Amount: ")
            if not self.amount_validation(amount):
                print("Transfer amount is not valid.")
                continue
            amount=Decimal(amount)
            if amount<=0:
                print("Amount must be greater than 0.")
                continue
            remaining_balance=balance-amount
            if remaining_balance<500:
                print("Minimum Balance in your Account Must be ₹500.")
                continue
            break
        return amount
    #4
    def confirm_transfer(self,customer,amount):
        balance=Decimal(self.current_account['Balance'])
        print("="*60)
        print("                         CONFIRM TRANSFER")
        print("="*60)
        print(f"\nSender   : {self.current_customer['Full_Name']}")
        print(f"\nReceiver : {customer['Full_Name']}")
        print(f"\nAmount   : ₹{amount}\n")
        remaining_balance=balance-amount
        print(f"\nRemaining Balance  : ₹{remaining_balance}")
        print('-'*60)
        print("\nThis action cannot be undone.\n")
        while True:
            confirm=input("Confirm Transfer? \n\n(Y/N) ").strip().upper()
            if confirm not in ["Y","N"]:
                print("Invalid Confirmation!")
                continue
            else:
                if confirm=="N":
                    return "cancelled"
                elif confirm=="Y":
                    return "success"
    #5
    def process_transfer(self,amount,accounts):
        balance=Decimal(self.current_account['Balance'])
        new_balance=balance-amount
        self.current_account['Balance']=str(new_balance)
        receiver_balance=Decimal(accounts['Balance'])
        reciever_new_balance=receiver_balance+amount
        accounts['Balance']=str(reciever_new_balance)  
    #6
    def save_transfer_transaction(self,accounts,customer,amount):
        transaction_id=f"TXN{self.account_data['system']['next_transaction_id']:06d}"
        time_stamp=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        self.current_account['Last_Updated']=time_stamp
        accounts['Last_Updated']=time_stamp
        transaction={
            "Transaction_ID" : transaction_id,
            "Sender_Name"         : self.current_customer['Full_Name'],
            "Sender_Account_Number" : self.current_account['Account_Number'],
            "Receiver_Name"       : customer['Full_Name'],
            "Receiver_Account_Number" : accounts['Account_Number'],
            "Amount"         : str(amount),
            "Type"           : "TRANSFER",
            "Status"         : "SUCCESS",
            "Sender_Balance_After_Transfer"     : self.current_account['Balance'],
            "Receiver_Balance_After_Transfer"   : accounts['Balance'],
            "Time_Stamp"     : time_stamp,
            
            
        }

        
        self.transaction_data['transactions'].append(transaction)
        self.account_data["system"]["next_transaction_id"]+=1
        self.save_account_data()
        self.save_transaction_data()
        return transaction
    def create_transfer_notification(self,transaction,accounts):
        notification_id=f"NTF{self.account_data['system']['next_notification_id']:06d}"
        notification1={
            "Notification_ID" : notification_id,
            "Customer_ID"     : self.current_customer['Customer_ID'],
            "Account_Number"  : self.current_account['Account_Number'],
            "Title"           : "Money Sent",
            "Message"         : f"You sent {transaction['Amount']}  to {transaction['Receiver_Name']}.",
            "Type"            : "TRANSFER",
            "Status"          :  "UNREAD",
            "Transaction_ID"  : transaction['Transaction_ID'],
            "Time_Stamp"      : transaction['Time_Stamp']
        }
        self.account_data["system"]["next_notification_id"]+=1
        notification_id=f"NTF{self.account_data['system']['next_notification_id']:06d}"  
        self.account_data["system"]["next_notification_id"]+=1     
        notification2={
            "Notification_ID" : notification_id,
            "Customer_ID"     : self.current_customer['Customer_ID'],
            "Account_Number"  : accounts['Account_Number'],
            "Title"           : "Money Received",
            "Message"         : f"You Received {transaction['Amount']}  from {transaction['Sender_Name']}.",
            "Type"            : "TRANSFER",
            "Status"          :  "UNREAD",
            "Transaction_ID"  : transaction['Transaction_ID'],
            "Time_Stamp"      : transaction['Time_Stamp']
        }       
        self.notification_data['notifications'].append(notification1)
        self.notification_data['notifications'].append(notification2)
        
        self.save_notification_data()
        return notification1,notification2
    #8
    def transfer_success_screen(self,transaction):
        print("="*60)
        print("                       TRANSFER SUCCESSFUL")
        print("="*60)
        print(f"\nTransaction ID : {transaction['Transaction_ID']}\n")
        print(f"\nReceiver Name  : {transaction['Receiver_Name']}\n")
        print(f"\nTransfer Amount: ₹{transaction['Amount']}\n")
        print(f"\nCurrent Balance: ₹{self.current_account['Balance']}\n")
        print(f"\nDate & Time    : {transaction['Time_Stamp']}")
        print("="*60)
        print("\n1. Transfer Again\n\n2. Customer Dashboard")
        choice=self.menu_choice_validations(1,2)
        return choice

    # Notification Section
    def notification_menu(self):
        while True:
            print("="*60)
            print("                           NOTIFICATIONS")
            print("="*60)
            print("\n1. View Notifications\n\n2. Back\n")
            print('='*60)
            choice=self.menu_choice_validations(1,2)
            if choice==1:
                result_message,selected_notification=self.view_notifications()
                if result_message=="cancelled":
                    continue
                elif result_message=="success":
                    self.mark_notification_read(selected_notification)
                    self.view_notification_details(selected_notification)
            elif choice==2:
                break

        
    def view_notifications(self):
        notification_list=[]
        for notifications in self.notification_data['notifications']:
            if self.current_account['Account_Number']==notifications['Account_Number']:
                notification_list.append(notifications)
             
        print("="*60)
        print("               NOTIFICATIONS")
        print("="*60)
        for number,notification in enumerate(notification_list,start=1):
            print(f"\n {number}")
            print(f"Title   : {notification['Title']}")
            print(f"Message : {notification['Message']}")
            print(f"Status  : {notification['Status']}")
            print(f"Time    : {notification['Time_Stamp']}")
            
            print("-"*60)
        if not  notification_list:
            print("No notifications available.")
            print("1. Back")
            choice=self.menu_choice_validations(1)
            if choice==1:
                return "cancelled",None
            
        else:
            max_choice=len(notification_list)+1
            print(f"\n{max_choice}. Back")
            choice=self.menu_choice_validations(1,max_choice)
            if choice==max_choice:
                return "cancelled",None
            else:
                selected_notification=notification_list[choice-1]

        return "success",selected_notification
        

    def mark_notification_read(self,selected_notification):
        if selected_notification['Status']=="UNREAD":
            selected_notification['Status']="READ"
        self.save_notification_data()
    def view_notification_details(self,selected_notification):
        print("="*30,end="")
        print("NOTIFICATION DETAILS",end="")
        print("="*25)
        print(f"\nTitle             : {selected_notification['Title']}\n")
        print(f"Message             : {selected_notification['Message']}\n")
        print(f"Type                : { selected_notification['Type']}\n")
        print(f"Transaction ID      : {selected_notification['Transaction_ID']}\n")
        print(f"Status              : {selected_notification['Status']}\n")
        print(f"Time                : {selected_notification['Time_Stamp']}\n")
        print("-"*60)
        
    #######Pop-Up Notification
    def handle_notification_popup(self):
        
        result_message,unread_notification_list,unread_notification=self.check_unread_notifications()
        if result_message=="not_found":
            return
        elif result_message=="found":
            choice=self.display_notification_popup(unread_notification,unread_notification_list)
            if choice==1:
                self.notification_menu()
            elif choice==2:
                return
        

    def check_unread_notifications(self):
        unread_notification=0
        unread_notification_list=[]
        for notifications in self.notification_data['notifications']:
            if self.current_account['Account_Number']==notifications['Account_Number']:
                if notifications['Status']=="UNREAD":
                    unread_notification_list.append(notifications)
                    unread_notification+=1
        if not unread_notification_list:
            return "not_found",None,None
        else:
            return "found" ,unread_notification_list,unread_notification

        
    
    def display_notification_popup(self,unread_notification,unread_notification_list):
        print("="*30,end="")
        print("NEW NOTIFICATIONS",end="")
        print("="*25)
        print(f"\n🔔 You have {unread_notification} unread notifications.\n")
        for number,notifications in enumerate(unread_notification_list,start=1):
            print(f"{number}.{notifications['Title']}\n  {notifications['Message']}\n")
        print("-"*60)

        print("\n1. View Notifications\n\n2. Continue to Dashboard\n")
        print("="*60)
        choice=self.menu_choice_validations(1,2)
        return choice

    ############Transaction History########################

    def transaction_history_menu(self):
        while True:
            print("="*30,end="")
            print("TRANSACTION HISTORY",end="")
            print("="*25)
            print("\n1. View All Transactions\n\n2. Recent Transactions\n\n3. Transaction Type History\n\n4. Monthly Transaction History\n\n5. Search Transaction \n\n6. Transaction Summary\n\n7. Back")
            print("="*60)
            choice=self.menu_choice_validations(1,7)
            if choice==1:
                self.view_all_transactions()
                continue
            elif choice==2:
                self.view_recent_transactions()
                continue
            elif choice==3:
                self.transaction_type_history()
                continue
            elif choice==4:
                self.monthly_transactions()
                continue
            elif choice==5:
                self.search_transaction()
                continue
            elif choice==6:
                self.transaction_summary()
                continue
            elif choice==7:
                break
            else:
                print("Invalid Choice!")
    
    def view_all_transactions(self):

        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No transactions found.")
            return
        self.get_transaction_list("VIEW ALL TRANSACTIONS","TRANSACTION",transaction_list)
        
    
    def get_account_transactions(self):
        transaction_list=[]
        for transactions in self.transaction_data['transactions']:
            if transactions["Type"]=="DEPOSIT" or transactions["Type"]=="WITHDRAW":
                if self.current_account['Account_Number']== transactions['Account_Number']:
                   transaction_list.append(transactions)
            elif transactions['Type']=="TRANSFER":
                if self.current_account['Account_Number']==transactions['Sender_Account_Number'] or self.current_account['Account_Number']==transactions['Receiver_Account_Number']:
                    transaction_list.append(transactions)
        return transaction_list
    
    def get_transaction_list(self,message,transaction_name,transaction_list):
        withdraw_deposit_list=[]
        transfer_list=[]
        for transaction in transaction_list:
            if transaction['Type']=="DEPOSIT" or transaction['Type']=="WITHDRAW":
                withdraw_deposit_list.append(transaction)
                
            elif transaction['Type']=="TRANSFER":
                transfer_list.append(transaction)
        print("="*30,end="")
        print(f"{message}",end="")       
        print("="*30)       
        if withdraw_deposit_list:
            self.display_deposit_withdraw_transaction(transaction_name,withdraw_deposit_list)
        if transfer_list:
            self.display_transfer_transaction(transaction_name,transfer_list)
    
    
    def display_deposit_withdraw_transaction(self,transaction_name,transaction_list):
        
        for number,transaction in enumerate(transaction_list,start=1):
            
            print(f"\n{transaction_name} {number}\n")
            print("-"*60)
            print(f"Transaction ID :{transaction['Transaction_ID']}")
            print(f"Date & Time    : {transaction['Time_Stamp']}\n")
            print(f"Type           :{transaction['Type']}")
            print(f"Method         :{transaction['Method']}")
            print(f"Amount         :₹{transaction['Amount']}")
            print(f"Status         :{transaction['Status']}\n")
            if transaction['Method']=="UPI":
                print(f"UPI ID                 : {transaction['UPI_ID']}\n")
            
            print(f"Balance Before         : ₹{transaction['Balance_Before']}")
            print(f"Balance After Transaction :₹{transaction['Balance_After']}")
            print('-'*60)
            print()
            print('='*60)

    
    
    def display_transfer_transaction(self,transaction_name,transaction_list):
        
        for number,transaction in enumerate(transaction_list,start=1):
            
            print(f"\n{transaction_name} {number}\n")
            print("-"*60)
            print(f"Transaction ID         : {transaction['Transaction_ID']}")
            print(f"Date & Time            : {transaction['Time_Stamp']} ")
            print(f"Type                   : {transaction['Type']}")
            print(f"Status                 : {transaction['Status']}\n")
            print(f"Sender                 : {transaction['Sender_Name']}")
            print(f"Sender Account         : {self.mask_account_number(transaction['Sender_Account_Number'])}\n")
            print(f"Receiver               : {transaction['Receiver_Name']}")
            print(f"Receiver Account       : {self.mask_account_number(transaction['Receiver_Account_Number'])}\n")
            print(f"Amount                 : ₹{transaction['Amount']}\n")
            if self.current_account['Account_Number']==transaction['Sender_Account_Number']:
                print(f"Balance After Transfer : ₹{transaction['Sender_Balance_After_Transfer']}")
            elif self.current_account['Account_Number']==transaction['Receiver_Account_Number']:
                print(f"Balance After Transfer : ₹{transaction['Receiver_Balance_After_Transfer']}")
            print('-'*60)
            print()
            print('='*60)
        

    def view_recent_transactions(self):
        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No Transactions Found.")
            return
        transaction_list.sort(
        key=lambda transaction: datetime.datetime.strptime(
            transaction["Time_Stamp"],
            "%d-%m-%Y %I:%M:%S %p"
        ),
        reverse=True
        )   
        recent_transaction=transaction_list[:5]
        self.get_transaction_list("RECENT TRANSACTION HISTORY","RECENT TRANSACTION",recent_transaction)
    
    def transaction_type_history(self):
        while True:
            print("="*30,end="")
            print("TRANSACTION TYPE HISTORY",end="")
            print("="*25)
            print("\n1. Deposit History\n\n2. Withdraw History\n\n3. Transfer History\n\n4. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,4)
            
            if choice==1:
                self.deposit_history()
            elif choice==2:
                self.withdraw_history()
            elif choice==3:
                self.transfer_history()
            elif choice==4:
                break
            else:
                print("Invalid Choice!")
    
    

    def deposit_history(self):
        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No Transactions Found")
            return
        deposit_list=[]
        for transaction in transaction_list:
            if transaction['Type']=="DEPOSIT":
                deposit_list.append(transaction)
        if not deposit_list:
            print("No Deposit Transaction Found.")
            return
        print("="*30,end="")
        print("DEPOSIT TRANSACTION HISTORY",end="")
        print("="*30)
        self.display_deposit_withdraw_transaction("DEPOSIT",deposit_list)
    
    def withdraw_history(self):
        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No Transactions Found")
            return
        withdraw_list=[]
        for transaction in transaction_list:
            if transaction['Type']=="WITHDRAW":
                withdraw_list.append(transaction)
        if not withdraw_list:
            print("No Withdraw Transaction Found.")
            return
        print("="*30,end="")
        print("WITHDRAW TRANSACTION HISTORY",end="")
        print("="*30)
        self.display_deposit_withdraw_transaction("WITHDRAW",withdraw_list)

    def transfer_history(self):
        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No Transactions Found")
            return
        transfer_list=[]
        for transactions in transaction_list:
            if transactions['Type']=="TRANSFER":
                transfer_list.append(transactions)
        if not transfer_list:
            print("No Transfer Transaction Found.")
            return
        print("="*30,end="")
        print("TRANSFER TRANSACTION HISTORY",end="")
        print("="*30)
        self.display_transfer_transaction("TRANSFER",transfer_list)


    def year_validation(self,new_year):
        if not isinstance(new_year,str):
            return False
        if not new_year.isdigit():
            return False
        if len(new_year)!=4:
            return False
        if new_year[0]=="0":
            return False
        return True
    def month_validation(self,new_month):
        if not isinstance(new_month,str):
            return False
        if not new_month.isdigit():
            return False
        if new_month[0]=="0":
            return False
        if int(new_month)<=0 or int(new_month)>12:
            return False
        return True

    def monthly_transactions(self):
        transaction_list=self.get_account_transactions()
        if not transaction_list:
            print("No Transactions Found")
            return
        monthly_transaction=[]
        while True:
            user_year=input("Enter Year   : ")
            if not self.year_validation(user_year):
                print("Year is not valid.")
                continue
            break
        while True:
            user_month=input("Enter Month (1-12): ")
            if not self.month_validation(user_month):
                print("Month is not valid!")
                continue
            break
        user_year=int(user_year)
        user_month=int(user_month)
        for transactions in transaction_list:
            date_time=datetime.datetime.strptime(transactions['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
            transaction_year=date_time.year
            transaction_month=date_time.month
            if transaction_year==user_year and transaction_month==user_month:
                monthly_transaction.append(transactions)
        if not monthly_transaction:
            print("No Monthly Transaction Is Available.")
            return
        self.get_transaction_list("MONTHLY TRANSACTION HISTORY","MONTHLY TRANSACTION",monthly_transaction)


    def search_transaction(self):
        while True:
            print("="*30,end="")
            print("SEARCH TRANSACTION",end="")
            print("="*25)
            print("\n1. Search by Transaction ID\n\n2. Search by Specific Date\n\n3. Search by Date Range\n\n4. Filter by Status\n\n5. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,5)
            if choice==1:
                self.search_customer_transaction_id()
                continue
            elif choice==2:
                self.search_by_specific_date()
                continue
            elif choice==3:
                self.search_by_date_range()
                continue
            elif choice==4:
                self.filter_by_status()
                continue
            elif choice==5:
                break
            else:
                print("Invalid Choice!")
    def search_customer_transaction_id(self):
        transaction_id=input("Enter Transaction ID : ")
        print("="*30,end="")
        print("TRANSACTION HISTORY : BY TRANSACTION ID",end="")
        print("="*25)
        print()
        print("-"*60)
        found=False
        transaction_list=self.get_account_transactions()
        for transaction in transaction_list:
            if transaction_id==transaction['Transaction_ID']:
                found=True
                if transaction['Type']=="DEPOSIT" or transaction['Type']=="WITHDRAW":
                    
                    print(f"Transaction ID :{transaction['Transaction_ID']}")
                    print(f"Date & Time    : {transaction['Time_Stamp']}\n")
                    print(f"Type           :{transaction['Type']}")
                    print(f"Method         :{transaction['Method']}")
                    print(f"Amount         :₹{transaction['Amount']}")
                    print(f"Status         :{transaction['Status']}\n")
                    if transaction['Method']=="UPI":
                        print(f"UPI ID                 : {transaction['UPI_ID']}\n")
                    
                    print(f"Balance Before         : ₹{transaction['Balance_Before']}")
                    print(f"Balance After Transaction :₹{transaction['Balance_After']}")
                    print('-'*60)
                    print()
                    print('='*60)
                elif transaction['Type']=="TRANSFER":
                    print(f"Transaction ID         : {transaction['Transaction_ID']}")
                    print(f"Date & Time            : {transaction['Time_Stamp']} ")
                    print(f"Type                   : {transaction['Type']}")
                    print(f"Status                 : {transaction['Status']}\n")
                    print(f"Sender                 : {transaction['Sender_Name']}")
                    print(f"Sender Account         : {self.mask_account_number(transaction['Sender_Account_Number'])}\n")
                    print(f"Receiver               : {transaction['Receiver_Name']}")
                    print(f"Receiver Account       : {self.mask_account_number(transaction['Receiver_Account_Number'])}\n")
                    print(f"Amount                 : ₹{transaction['Amount']}\n")
                    if self.current_account['Account_Number']==transaction['Sender_Account_Number']:
                        print(f"Balance After Transfer : ₹{transaction['Sender_Balance_After_Transfer']}")
                    elif self.current_account['Account_Number']==transaction['Receiver_Account_Number']:
                        print(f"Balance After Transfer : ₹{transaction['Receiver_Balance_After_Transfer']}")
                    print('-'*60)
                    print()
                    print('='*60)
        if not found:
            print("No transaction found.")
    

    def date_validation(self,new_date):
        if not isinstance(new_date,str):
            return False
        try:
            datetime.datetime.strptime(new_date,"%d-%m-%Y")
            return True
        except ValueError:
            return False
    

    def search_by_specific_date(self):
        while True:
            user_date=input("Enter Date (format:DD-MM-YYYY) : ")
            if not self.date_validation(user_date):
                print("Invalid Date!")
                continue
            break
        user_date=datetime.datetime.strptime(user_date,"%d-%m-%Y").date()
        transaction_by_date=[]
        for transactions in self.transaction_data['transactions']:
            date_time=datetime.datetime.strptime(transactions['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
            transaction_date=date_time.date()
            
            if user_date==transaction_date:
                transaction_by_date.append(transactions)
        if not transaction_by_date:
            print("No Transaction Available On This Date.")
            return
        self.get_transaction_list("TRANSACTION HISTORY : SEARCHED BY DATE","TRANSACTION",transaction_by_date)
    

    def search_by_date_range(self):
        while True:
            start_date=input("Enter Start Date (format:DD-MM-YYYY) : ")
            if not self.date_validation(start_date):
                print("Invalid Date!")
                continue
            break
        while True:
            end_date=input("Enter End Date (format:DD-MM-YYYY) : ")
            if not self.date_validation(end_date):
                print("Invalid Date!")
                continue
            break
        start_date=datetime.datetime.strptime(start_date,"%d-%m-%Y").date()
        end_date=datetime.datetime.strptime(end_date,"%d-%m-%Y").date()
        transaction_date_range=[]
        for transactions in self.transaction_data['transactions']:
            date_time=datetime.datetime.strptime(transactions['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
            transaction_date=date_time.date()
            if start_date <= transaction_date <= end_date:
                transaction_date_range.append(transactions)
        if not transaction_date_range:
            print("No transactions happen between this range of date.")
            return
        self.get_transaction_list("TRANSACTION HISTORY : SEARCHED BY DATE RANGE ","TRANSACTION",transaction_date_range)

    def filter_by_status(self):
        while True:
            print("="*30,end="")
            print("FILTER BY STATUS",end="")
            print("="*25)
            print("\n1. Success\n\n2. Failed\n\n3. Pending\n\n4. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,4)
            if choice==1:
                self.success_status_transaction()
                continue
            elif choice==2:
                self.failed_state_transaction()
                continue
            elif choice==3:
                self.pending_state_transaction()
                continue
            elif choice==4:
                break
            else:
                print("Invalid Choice!")
    
    def success_status_transaction(self):
        success_transaction=[]
        transaction_list=self.get_account_transactions()
        for transactions in transaction_list:
            if transactions['Status']=="SUCCESS":
                success_transaction.append(transactions)
        if not success_transaction:
            print("No success transactions are available.")
            return
        self.get_transaction_list("TRANSACTION HISTORY : BASED ON 'SUCCESS' STATE ","TRANSACTION",success_transaction)
    def failed_state_transaction(self):
        failed_transaction=[]
        transaction_list=self.get_account_transactions()
        for transactions in transaction_list:
            if transactions['Status']=="FAILED":
                failed_transaction.append(transactions)
        if not failed_transaction:
            print("No failed transactions are available.")
            return
        self.get_transaction_list("TRANSACTION HISTORY : BASED ON 'FAILED' STATE ","TRANSACTION",failed_transaction)


    def pending_state_transaction(self):
        pending_transaction=[]
        transaction_list=self.get_account_transactions()
        for transactions in transaction_list:
            if transactions['Status']=="PENDING":
                pending_transaction.append(transactions)
        if not pending_transaction:
            print("No pending transactions are available.")
            return
        self.get_transaction_list("TRANSACTION HISTORY : BASED ON 'PENDING' STATE ","TRANSACTION",pending_transaction)


    def transaction_summary(self):
        while True:
            print('='*30,end="")
            print("TRANSACTION SUMMARY",end="")
            print('='*25)
            print("\n1. Overall Summary\n\n2. Monthly Summary\n\n3. Back\n")
            print('='*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.overall_summary()
                continue
            elif choice==2:
                self.monthly_summary()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
    def overall_summary(self):
        total_transaction=0
        deposit_transaction=0
        withdraw_transaction=0
        transfer_transaction=0
        total_deposit_amount=0
        total_withdrawl_amount=0
        total_transfer_amount=0
        for transaction in self.transaction_data['transactions']:
            if transaction['Type']=="DEPOSIT" or transaction['Type']=="WITHDRAW":
                if self.current_account['Account_Number']==transaction['Account_Number']:
                    total_transaction+=1
                    if transaction['Type']=="DEPOSIT":
                        deposit_transaction+=1
                        total_deposit_amount+=Decimal(transaction['Amount'])
                    elif transaction['Type']=="WITHDRAW":
                        withdraw_transaction+=1
                        total_withdrawl_amount+=Decimal(transaction['Amount'])
            
            elif transaction['Type']=="TRANSFER":
                if self.current_account['Account_Number']==transaction['Sender_Account_Number'] or self.current_account['Account_Number']==transaction['Receiver_Account_Number']:
                    total_transaction+=1
                    transfer_transaction+=1
                    total_transfer_amount+=Decimal(transaction['Amount'])
               
        if not total_transaction:
            print("No transactions found.")
            return
        print('='*30,end="")
        print("OVERALL TRANSACTION SUMMARY",end="")
        print("="*25)
        print(f"\nTotal Transactions        : {total_transaction}\n")
        print(f"Deposit Transactions        : {deposit_transaction}")
        print(f"Withdraw Transactions       : {withdraw_transaction}")
        print(f"Transfer Transactions       : {transfer_transaction}\n")
        print(f"Total Deposit Amount        : ₹{total_deposit_amount}")
        print(f"Total Withdraw Amount       : ₹{total_withdrawl_amount}")
        print(f"Total Transfer Amount       : ₹{total_transfer_amount}\n")
        print("="*60)
    
    def monthly_summary(self):
        while True:
            user_year=input("Enter Year : ")
            if not self.year_validation(user_year):
                print("Invalid Year!")
                continue
            break
        while True:
            user_month=input("Enter Month (1-12): ")
            if not self.month_validation(user_month):
                print("Invalid Month!")
                continue
            break

        user_year=int(user_year)
        user_month=int(user_month)

        total_transaction=0
        deposit_transaction=0
        withdraw_transaction=0
        transfer_transaction=0
        total_deposit_amount=0
        total_withdrawl_amount=0
        total_transfer_amount=0
        month=None
        for transactions in self.transaction_data['transactions']:
            if transactions['Type']=="DEPOSIT" or transactions['Type']=="WITHDRAW":
                if self.current_account['Account_Number']==transactions['Account_Number']:
                    
                    date_object=datetime.datetime.strptime(transactions['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
                    transaction_year=date_object.year
                    transaction_month=date_object.month
                    
                    if user_year==transaction_year and user_month==transaction_month:
                        month=date_object.strftime("%B %Y")  #%B=full month name,%b=month name in short like jan,%m=month name in number
                        total_transaction+=1
                        if transactions['Type']=="DEPOSIT":
                            deposit_transaction+=1
                            total_deposit_amount+=Decimal(transactions['Amount'])
                        elif transactions['Type']=="WITHDRAW":
                            withdraw_transaction+=1
                            total_withdrawl_amount+=Decimal(transactions['Amount'])
            elif transactions['Type']=="TRANSFER":
                if self.current_account['Account_Number']==transactions['Sender_Account_Number'] or self.current_account['Account_Number']==transactions['Receiver_Account_Number']:
                    date_object=datetime.datetime.strptime(transactions['Time_Stamp'],"%d-%m-%Y %I:%M:%S %p")
                    transaction_year=date_object.year
                    transaction_month=date_object.month
                    
                    if user_year==transaction_year and user_month==transaction_month:
                        month=date_object.strftime("%B %Y")
                        total_transaction+=1
                        transfer_transaction+=1
                        total_transfer_amount+=Decimal(transactions['Amount'])
        if not total_transaction:
            print("No transactions found.")
            return   
        print('='*30,end="")
        print("MONTHLY TRANSACTION SUMMARY",end="")
        print("="*25)
        print(f"Month : {month}")
        print(f"\nTotal Transactions        : {total_transaction}\n")
        print(f"Deposit Transactions        : {deposit_transaction}")
        print(f"Withdraw Transactions       : {withdraw_transaction}")
        print(f"Transfer Transactions       : {transfer_transaction}\n")
        print(f"Total Deposit Amount        : ₹{total_deposit_amount}")
        print(f"Total Withdraw Amount       : ₹{total_withdrawl_amount}")
        print(f"Total Transfer Amount       : ₹{total_transfer_amount}\n")
        print("="*60)

#####customer change pin section##########
    def change_pin(self):
        print("="*60)
        print("               CHANGE ACCOUNT PIN")
        print("="*60)
        print(f"Account Number : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank           : {self.current_account['Bank_Name']}")
        print(f"Branch         : {self.current_account['Branch_Name']}")
        print(f"Account Type   : {self.current_account['Account_Type']}\n")
        print("-"*60)
        while True:
            current_pin=getpass.getpass("Current PIN : ")
            if current_pin!=self.current_customer['PIN']:
                print("Current PIN is incorrect.")
                continue
            break
        while True:
            new_pin=getpass.getpass("Enter New PIN : ")
            if not self.pin_validation(new_pin):
                print("Invalid Pin!")
                continue
            
            
            if new_pin==current_pin:
                print("New PIN cannot be the same as the current PIN.")
                continue
            break
        while True:
            confirm_pin=getpass.getpass("Confirm PIN : ")
            if new_pin!=confirm_pin:
                print("New PIN and Confirm PIN do not match.")
                continue
            break
        
        self.current_customer['PIN']=new_pin
        self.save_account_data()
        print('-'*60)
        print("\nPIN updated successfully.\n")
        print("="*60)

    ##### Service Center ####################
    def service_center_screen(self):
        while True:
            print("="*60)
            print("                       SERVICE CENTER")
            print("="*60)
            print("\n1. Cheque Deposit Request\n\n2. Cheque Withdrawal Request\n\n3. Phone Number Change Request\n\n4. Address Change Request\n\n5. Account Closure Request\n\n6. View My Requests\n\n7. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,7)
            if choice==1:
                self.cheque_deposit_request()
                continue
            elif choice==2:
                self.cheque_withdraw_request()
                continue
            elif choice==3:
                self.phone_number_change()
                continue
            elif choice==4:
                self.change_address_request()
                continue
            elif choice==5:
                self.account_closure_request()
                continue
            elif choice==6:
                self.view_my_request()
                continue
            elif choice==7:
                break
            else:
                print("Invalid Choice!")
    def cheque_deposit_request(self):
        print("="*60)
        print("                              CHEQUE DEPOSIT REQUEST")
        print("="*60)
        print("\nAccount Information\n")
        print('-'*60)
        print()
        self.get_account_details()
        request=self.collect_cheque_request_details("deposit","CHEQUE_DEPOSIT")
        if request:
            self.display_request_submission(request)

    def get_account_details(self):
        
        print(f"Customer ID      : {self.current_account['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank             : {self.current_account['Bank_Name']}")
        print(f"Branch           : {self.current_account['Branch_Name']}")
        print(f"Account Type     : {self.current_account['Account_Type']}")
        print(f"Current Balance  : ₹{self.current_account['Balance']}\n")
        print("="*60)
    def collect_cheque_request_details(self,method,request_type):
        print("="*60)
        print('                                ENTER CHEQUE DETAILS')
        print("="*60)
        print()
        while True:
            cheque_number=input("Cheque Number : ")
            if not self.cheque_number_validation(cheque_number):
                print("Invalid Cheque Number!")
                continue
            break
        while True:
            Cheque_amount=input("Cheque Amount : ")
            if not self.amount_validation(Cheque_amount):
                print("Invalid Cheque Amount!")
                continue
            break
        Cheque_amount=Decimal(Cheque_amount)

        while True:
            cheque_date=input("Cheque Date (format:DD-MM-YYYY)  : ")
            if not self.date_validation(cheque_date):
                print("Invalid Date Format!")
                continue
            break

        print()
        print("="*60)
        

        print("="*60)
        print("                                    CONFIRM REQUEST")
        print("="*60)
        print(f"\nAccount Number : {self.mask_account_number(self.current_account['Account_Number'])}\n")
        print(f"Cheque Number  : {self.mask_cheque_number(cheque_number)}\n")
        print(f"Cheque Amount  : ₹{Cheque_amount}\n")
        print(f"Cheque Date    : {cheque_date}\n")
        print("-"*60)
        print()
        
        while True:
            response=input(f"Confirm cheque {method} request? (Y/N)").strip().upper()
            if response  not in ["Y","N"]:
                print("Invalid Request Response.")
                continue
            break
        
        if response=="Y":
            request_id=f"REQ{self.account_data['system']['next_request_id']:06d}"
            request_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            request={
                "Request_ID"   : request_id,
                "Customer_ID"  : self.current_account['Customer_ID'],
                "Account_Number"  : self.current_account['Account_Number'],
                "Request_Type"  :  request_type,
                "Cheque_Number"  : cheque_number,
                "Amount"  : str(Cheque_amount),
                "Cheque_Date"  : cheque_date,
                "Request_Date" : request_date,
                "Status"       : "PENDING",
                "Admin_Remark"  :"",
                "Completed_Date"  :""
            }
            self.request_data['requests'].append(request)
            self.account_data['system']['next_request_id']+=1
            self.save_request_data()
            self.save_account_data()
            return request
        elif response=="N":
            print(f"Cheque {method} request cancelled.!")
            return None
    def display_request_submission(self,request):

        print("="*60)   
        print("                       REQUEST SUBMITTED SUCCESSFULLY")     
        print("="*60)  
        print(f"Request ID      : {request['Request_ID']}\n")
        print(f"Request Type    : {request['Request_Type']}\n") 
        print(f"Status          : {request['Status']}\n")
        print("Your request has been sent to the bank for verification\n\nYou will receive a notification once the request is processed.\n") 

        print("="*60)        


    def cheque_withdraw_request(self):
        print("="*60)
        print("                              CHEQUE WITHDRAW REQUEST")
        print("="*60)
        print("\nAccount Information\n")
        print('-'*60)
        print()
        self.get_account_details()
        request=self.collect_cheque_request_details("withdraw","CHEQUE_WITHDRAW")
        if request:
            self.display_request_submission(request)

        
    def phone_number_change(self):
        self.display_phone_change_screen()
        result=self.collect_new_phone_number()
        if result:
            self.display_request_submission(result)
    

    def display_phone_change_screen(self):
        print("="*60)
        print("                           PHONE NUMBER CHANGE REQUEST")
        print("="*60)
        print("\nAccount Information\n")
        print("-"*60)
        print(f"\nCustomer ID    : {self.current_account['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank             : {self.current_account['Bank_Name']}")
        print(f"Branch           : {self.current_account['Branch_Name']}")
        print(f"Account Type     : {self.current_account['Account_Type']}\n")
        print("-"*60)
        print(f"\nCurrent Phone Number : {self.current_customer['Phone_Number']}\n")

        print("="*60)

    def collect_new_phone_number(self):
        print("="*60)
        print("                        ENTER NEW PHONE NUMBER")
        print("="*60)
        print()
        while True:
            new_number= input("New Phone Number :")
            if not self.phone_number_validation(new_number):
                print("New Phone Number Is Not Valid !")
                continue
            
            if new_number==self.current_customer['Phone_Number']:
                print("Please enter a new phone number.")
                continue
            
        
            
            found = False

            for customer in self.account_data['customers']:
                if new_number == customer['Phone_Number']:
                    found = True
                    break

            if found:
                print("Duplicate phone numbers are not allowed.")
                continue

            break  
            

        print("="*60)
        print("                                       CONFIRM REQUEST")
        print("="*60)
        print(f"\nCurrent Phone Number : {self.current_customer['Phone_Number']}")
        print(f"\nNew Phone Number     : {new_number}\n")
        print('-'*60)
        while True:
            response=input("Submit phone number change request?  (Y/N) : ").strip().upper()
            if response not in ["Y","N"]:
                print("Invalid Response!")
                continue
            break
        print("="*60)
        if response=="Y":
            
            request_id=f"REQ{self.account_data['system']['next_request_id']:06d}"
            request_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            request_phone={
                "Request_ID"        : request_id,
                "Customer_ID"       : self.current_account['Customer_ID'],
                "Account_Number"    : self.current_account['Account_Number'],
                "Request_Type"      : "PHONE_NUMBER_CHANGE",
                "Current_Phone"     : self.current_customer['Phone_Number'],
                "New_Phone"         : new_number,
                "Request_Date"      : request_date,
                "Status"            : "PENDING",
                "Admin_Remark"      : "",
                "Completed_Date"    : ""
            }
            self.request_data['requests'].append(request_phone)
            self.account_data['system']['next_request_id']+=1
            self.save_request_data()
            self.save_account_data()
            return request_phone
        elif response=="N":
            print(f" Phone number change  request cancelled.!")
            return None

    def change_address_request(self):
        self.display_change_address_screen()
        result=self.collect_new_address()
        if result:
            self.display_request_submission(result)
    def display_change_address_screen(self):
        print('='*60)
        print('                            ADDRESS CHANGE REQUEST')
        print('='*60)
        print('\nAccount Information\n')
        print('-'*60)
        print(f"\nCustomer ID    : {self.current_account['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank             : {self.current_account['Bank_Name']}")
        print(f"Branch           : {self.current_account['Branch_Name']}")
        print(f"Account Type     : {self.current_account['Account_Type']}\n")
        print('-'*60)
        print(f"\nCurrent Address : {self.current_customer['Address']}\n")
        print('='*60)
    def collect_new_address(self):
        print("="*60)
        print("                ENTER NEW ADDRESS")
        print("="*60)
        print()
        while True:
            new_address=input("New Address : ").strip()
            if not self.address_validation(new_address):
                print("Address is invalid!")
                continue
            if new_address==self.current_customer['Address']:
                print("Please enter a new address.")
                continue
            break

        print('='*60)
        print('                                      CONFIRM REQUEST')
        print('='*60)
        print(f"\nCurrent Address : {self.current_customer['Address']}\n")
        print(f"New Address :  {new_address}\n")
        print('-'*60)
        while True:
            request=input("Submit address change request? (Y/N) ").strip().upper()
            if request not in ["Y","N"]:
                print("Invalid Response!")
                continue
            break

        print('='*60)
        if request=="Y":
            request_id=f"REQ{self.account_data['system']['next_request_id']:06d}"
            request_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            request_address={
                "Request_ID"      : request_id,
                "Customer_ID"     : self.current_account['Customer_ID'],
                "Account_Number"  : self.current_account['Account_Number'],
                "Request_Type"    : "ADDRESS_CHANGE",
                "Current_Address" : self.current_customer['Address'],
                "New_Address"     : new_address,
                "Request_Date"    : request_date,
                "Status"          : "PENDING",
                "Admin_Remark"    : "",
                "Completed_Date"  : ""
            }
            self.request_data['requests'].append(request_address)
            self.account_data['system']['next_request_id']+=1
            self.save_request_data()
            self.save_account_data()
            return request_address
        elif request=="N":
            print(f" Address change request cancelled.")
            return None
    
    
    def account_closure_request(self):
        self.account_closure_screen()
        self.imp_notice()
        result=self.reason_for_closure()
        if result:
            self.display_request_submission(result)
    def account_closure_screen(self):
        print("="*60)
        print("                        ACCOUNT CLOSURE REQUEST")
        print("="*60)
        print("\nAccount Information\n")
        print('-'*60)
        print(f"Customer ID      : {self.current_account['Customer_ID']}")
        print(f"Account Number   : {self.mask_account_number(self.current_account['Account_Number'])}")
        print(f"Bank             : {self.current_account['Bank_Name']}")
        print(f"Branch           : {self.current_account['Branch_Name']}")
        print(f"Account Type     : {self.current_account['Account_Type']}")
        print(f"Current Balance  : {self.current_account['Balance']}\n")
        print("="*60)
    def imp_notice(self):
        print("                 IMPORTANT NOTICE")
        print("\n• Account closure requires bank approval.\n")
        print("• The remaining account balance will be settled before account closure.\n")
        print("• Once approved, this account will become inactive.\n")
        print("="*60)
    def reason_for_closure(self):
        print("="*60)
        print("                                        ENTER CLOSURE DETAILS")
        print("="*60)
        print()
        while True:
            reason=input("Reason for Closing Account : ").strip()
            if not self.address_validation(reason):
                print("Invalid Reason Format!")
                continue
            break
        print("_"*60)
        print("="*60)
        print("="*60)
        print("                                CONFIRM REQUEST")
        print("="*60)
        print(f"\nAccount Number : {self.mask_account_number(self.current_account['Account_Number'])}\n")
        print(f"Reason : {reason}\n")
        print('-'*60)
        while True:
            request=input("Submit account closure request?  (Y/N) ").strip().upper()
            if request not in ['Y','N']:
                print("Invalid response!")
                continue
            break

        print("="*60)
        if request=="Y":
            request_id=f"REQ{self.account_data['system']['next_request_id']:06d}"
            request_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            request_account_closure={
                "Request_ID"      : request_id,
                "Customer_ID"     : self.current_account['Customer_ID'],
                "Account_Number"  : self.current_account['Account_Number'],
                "Request_Type"    : "ACCOUNT_CLOSURE",
                "Reason"          : reason,
                
                "Request_Date"    : request_date,
                "Status"          : "PENDING",
                "Admin_Remark"    : "",
                "Completed_Date"  : ""
            }
            self.request_data['requests'].append(request_account_closure)
            self.account_data['system']['next_request_id']+=1
            self.save_request_data()
            self.save_account_data()
            return request_account_closure
        elif request=="N":
            print(f" Account closure   request cancelled.!")
            return None

    def view_my_request(self):
        self.view_request_screen()
        message,data=self.all_request()
        if message=="cancelled":
            print("View request cancelled!")
            return
        elif message=="failed":
            print("No view requests are there! ")
            return
        elif message=='success':
            self.display_selected_request(data)
    def view_request_screen(self):
        print('='*60)
        print("                       MY REQUESTS")
        print('='*60)
        print(f"\nCustomer ID    : {self.current_account['Customer_ID']}\n")
        print(f"Account Number : {self.mask_account_number(self.current_account['Account_Number'])}\n")
        print('-'*60)
        
    def all_request(self):
        request_list=[]
        for requests in self.request_data['requests']:
            if self.current_account['Account_Number']==requests['Account_Number']:
                request_list.append(requests)
        if request_list:
            for number,request in enumerate(request_list,start=1):
                print(f"\n{number}. {request['Request_ID']}\n")
                print(f"Request Type : {request['Request_Type']}\n")
                print(f"Status       : {request['Status']}\n")
                print('-'*60)
            index=len(request_list)+1
            print(f"{index}. Back")
            option=self.menu_choice_validations(1,index)
            if option==index:
                return "cancelled",None
            request_detail=request_list[option-1]
        elif not request_list:
            print("No requests found for this account.")
            return "failed",None
        return "success",request_detail
    def display_selected_request(self,request_detail):
        print("="*60)
        print("                     REQUEST DETAILS")
        print("="*60)
        print(f"Request ID      : {request_detail['Request_ID']}\n")
        print(f"Request Type    : {request_detail['Request_Type']}\n")
        print(f"Status          : {request_detail['Status']}\n")
        print(f"Request Date    : {request_detail['Request_Date']}\n")
        print(f"Completed Date  : {request_detail['Completed_Date']}\n")
        print('-'*60)
        print("\n(Admin Remark)\n")
        if request_detail["Admin_Remark"]:
            print(request_detail["Admin_Remark"])
        else:
            print("Pending for bank verification.")
        print("="*60)
        print("Request Specific Information\n")
        print('-'*60)
        print()
        if request_detail['Request_Type']=="CHEQUE_DEPOSIT":
            print(f"Cheque Number : {self.mask_cheque_number(request_detail['Cheque_Number'])}\n")
            print(f"Amount        : ₹{request_detail['Amount']}\n")
            print(f"Cheque Date   : {request_detail['Cheque_Date']}")
        elif request_detail['Request_Type']=="CHEQUE_WITHDRAW":
            print(f"Cheque Number : {self.mask_cheque_number(request_detail['Cheque_Number'])}\n")
            print(f"Amount        : ₹{request_detail['Amount']}\n")
            print(f"Cheque Date   : {request_detail['Cheque_Date']}")
        elif request_detail['Request_Type']=="PHONE_NUMBER_CHANGE":
            print(f"Current Phone : {request_detail['Current_Phone']}\n")
            print(f"New Phone     : {request_detail['New_Phone']}")
        elif request_detail['Request_Type']=="ADDRESS_CHANGE":
            print(f"Current Address : {request_detail['Current_Address']}\n")
            print('-'*60)
            print(f"New Address : {request_detail['New_Address']}")
        elif request_detail['Request_Type']=="ACCOUNT_CLOSURE":
            print(f"Reason : {request_detail['Reason']}")
        print("="*60)

###############################Admin Dashboard################
    def customer_management(self):
        while True:
            print("="*60)
            print("                            CUSTOMER MANAGEMENT")
            print("="*60)
            print("\n1. View All Customers\n\n2. Search Customer\n\n3. Back")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.view_all_customers()
            elif choice==2:
                self.search_customer()
            elif choice==3:
                break
            else:
                print("Invalid Choice!")

    def search_customer(self):
        while True:
            print("="*60)
            print("                       SEARCH CUSTOMER")
            print("="*60)
            print("\nSearch Customer By:\n\n1. Customer ID\n\n2. Phone Number\n\n3. Email\n\n4. Back\n")
            choice=self.menu_choice_validations(1,4)
            if choice==1:
                self.search_customer_by_customer_id()
                continue
            elif choice==2:
                self.search_customer_by_phone_number()
                continue
            elif choice==3:
                self.search_customer_by_email()
                continue
            elif choice==4:
                break
            else:
                print("Invalid Choice!")
            print("="*60)

    def search_customer_by_customer_id(self):
        print("="*60)
        print("                    SEARCH CUSTOMER BY ID")
        print("="*60)
        print()
        customer_id=input("Enter Customer ID : ")
        print()
        found=False
        for customer in self.account_data['customers']:
            if customer_id==customer['Customer_ID']:
               found=True
               self.customer_detail_after_search(customer)
               break
        if not found:
            print("Customer not found.")
            return
    def search_customer_by_phone_number(self):
        print("="*60)
        print("                    SEARCH CUSTOMER BY PHONE NUMBER")
        print("="*60)
        print()
        phone=input("Enter Phone Number : ")
        print()
        found=False
        for customer in self.account_data['customers']:
            if phone==customer['Phone_Number']:
                found=True
                self.customer_detail_after_search(customer)
                break
        if not found:
            print("Customer not found.")
            return
    def search_customer_by_email(self):
        print("="*60)
        print("                    SEARCH CUSTOMER BY EMAIL")
        print("="*60)
        print()
        email=input('Enter Email : ')
        print()
        found=False
        for customer in self.account_data['customers']:
            if email==customer['Email']:
                found=True
                self.customer_detail_after_search(customer)
                break
        if not found:
            print("Customer not found.")
            return
    def view_all_customers(self):
        print("="*60)
        print("              VIEW ALL CUSTOMER")          
        print("="*60)
        all_customer=[]
        for customer in self.account_data['customers']:
            all_customer.append(customer)
        if not all_customer:
            print("No customer found!")
            return
        for number,customers in enumerate(all_customer,start=1):
            print(f"Customer {number}\n")
            print(f"\nCustomer ID   : {customers['Customer_ID']}")
            print(f"Name            : {customers['Full_Name']}")
            print(f"Phone Number    : {customers['Phone_Number']}")
            print(f"Email           : {customers['Email']}")
            print(f"Address         : {customers['Address']}")
            print(f"Created Date    : {customers['Created_Date']}")
            print(f"Status          : {customers['Account_Status']}\n")
            print("-"*60)

        print("="*60)          
        
    def customer_detail_after_search(self,customer):
        print("="*60)
        print("               CUSTOMER DETAILS")
        print("="*60)
        print(f"\nCustomer ID   : {customer['Customer_ID']}")
        print(f"Name            : {customer['Full_Name']}")
        print(f"Phone Number    : {customer['Phone_Number']}")
        print(f"Email           : {customer['Email']}")
        print(f"Address         : {customer['Address']}")
        print(f"Created Date    : {customer['Created_Date']}")
        print(f"Status          : {customer['Account_Status']}\n")
        print("="*60)


    
    ######## Request Management ###########

    def request_management(self):
        while True:
            print('='*60)
            print("                        REQUEST MANAGEMENT")
            print('='*60)
            print("\n1. View Pending Requests\n\n2. Request History\n\n3. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                message,result=self.view_pending_request()
                if message=="cancelled":
                    print("View pending request cancelled!")
                    break
                elif message=="failed":
                    print("No pending requests are there.")
                    break
                elif message=="success":
                    self.request_detail(result)

            elif choice==2:
                self.request_history()
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
    def view_pending_request(self):
        request_pending_list=[]
        for request in self.request_data['requests']:
            if request['Status']=="PENDING":
                request_pending_list.append(request)
        print("="*60)
        print("                              PENDING REQUESTS")
        print("="*60)
        if request_pending_list:
            index=len(request_pending_list)+1
            
            for number,requests in enumerate(request_pending_list,start=1):
                print(f"\n{number}. {requests['Request_ID']}\n")
                print(f"{requests['Request_Type']}\n")
                print(f"{requests['Customer_ID']}\n")
                print(f"Account Number : {self.mask_account_number(requests['Account_Number'])}\n")
                print(f"{requests['Status']}\n")
                print('-'*60)
            print(f"{index}. Back")
            choice=self.menu_choice_validations(1,index)

            if choice==index:
                return "cancelled",None
            request=request_pending_list[choice-1]
        elif not request_pending_list:
            return "failed",None
        return "success",request
    
    def request_detail(self,request):
        print("="*60)
        print("                                   REQUEST DETAILS")
        print("="*60)
        print(f"Request ID      : {request['Request_ID']}\n")
        print('-'*60)
        print(f"Customer ID     : {request['Customer_ID']}\n")
        print(f"Account Number  : {self.mask_account_number(request['Account_Number'])}\n")
        print('-'*60)
        print(f"Request Type    : {request['Request_Type']}\n")
        print('-'*60)
        if request['Request_Type']=="CHEQUE_DEPOSIT":
            print(f"Cheque Number : {self.mask_cheque_number(request['Cheque_Number'])}\n")
            print(f"Amount        : ₹{request['Amount']}\n")
            print(f"Cheque Date   : {request['Cheque_Date']}")
        elif request['Request_Type']=="CHEQUE_WITHDRAW":
            print(f"Cheque Number : {self.mask_cheque_number(request['Cheque_Number'])}\n")
            print(f"Amount        : ₹{request['Amount']}\n")
            print(f"Cheque Date   : {request['Cheque_Date']}")
        elif request['Request_Type']=="PHONE_NUMBER_CHANGE":
            print(f"Current Phone : {request['Current_Phone']}\n")
            print(f"New Phone     : {request['New_Phone']}")
        elif request['Request_Type']=="ADDRESS_CHANGE":
            print(f"Current Address : {request['Current_Address']}\n")
            print('-'*60)
            print(f"New Address : {request['New_Address']}")
        elif request['Request_Type']=="ACCOUNT_CLOSURE":
            print(f"Reason : {request['Reason']}")
        print('-'*60)
        print(f"\nRequest Date : {request['Request_Date']}\n")
        print(f"Status : {request['Status']}\n")
        print("="*60)
        print("\n1. Approve\n\n2. Reject\n\n3. Back")
        choice=self.menu_choice_validations(1,3)
        if choice==1:
            self.approve_request(request)
        elif choice==2:
            self.reject_request(request)
        elif choice==3:
            return
    def approve_request(self,request):
        if request['Request_Type']=="CHEQUE_DEPOSIT":
            self.approve_cheque_deposit(request)
        elif request['Request_Type']=="CHEQUE_WITHDRAW":
            self.approve_cheque_withdraw(request)
        elif request['Request_Type']=="PHONE_NUMBER_CHANGE":
            self.approve_phone_number_change(request)
        elif request['Request_Type']=="ADDRESS_CHANGE":
            self.approve_address_change(request)
        elif request['Request_Type']=="ACCOUNT_CLOSURE":
            self.approve_account_closure(request)

    def approve_request_status(self,request):
        current_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        if request['Status']!="PENDING":
            return
        request['Status']="APPROVED"
        request['Completed_Date']=current_date
        request['Admin_Remark']="Approved"
        self.save_request_data()

    def approve_notification(self,request):
        
        if request['Request_Type']=="CHEQUE_DEPOSIT":
            Title=  "Cheque Deposit Approved"
            Message= f"Your cheque deposit request has been approved.\n₹{request['Amount']} has been credited to your account."
        elif request['Request_Type']=="CHEQUE_WITHDRAW":
            Title="Cheque Withdrawal Approved"
            Message=f"Your cheque withdrawal request has been approved.\n₹{request['Amount']} has been debited from your account."
        elif request['Request_Type']=="PHONE_NUMBER_CHANGE":
            Title="Phone Number Updated"
            Message="Your phone number change request has been approved successfully."
        elif request['Request_Type']=="ADDRESS_CHANGE":
            Title="Address Updated"
            Message="Your address has been updated successfully."
        elif request['Request_Type']=="ACCOUNT_CLOSURE":
            Title="Account Closed"
            Message="Your account closure request has been approved.\nYour account has been closed successfully."
        else:
           Title="Request Approved"
           Message="Your request has been approved successfully."
        notification_id=f"NTF{self.account_data['system']['next_notification_id']:06d}"
        notification={
            "Notification_ID" : notification_id,
            "Customer_ID" : request['Customer_ID'],
            "Account_Number" : request['Account_Number'],
            "Title" : Title,
            "Message" : Message,
            "Status" : "UNREAD",
            "Time_Stamp":datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        }
        self.notification_data['notifications'].append(notification)
        self.account_data['system']['next_notification_id']+=1
        self.save_account_data()
        self.save_notification_data()


    #############
    def approve_cheque_deposit(self,request):
        result=self.cheque_deposit(request)
        if not result:
            return 
        amount,current_time,balance_before,balance_after=result
        self.save_cheque_approve(request,amount,current_time,balance_before,balance_after,"DEPOSIT")
        self.approve_request_status(request)
        self.approve_notification(request)
    def save_cheque_approve(self,request,amount,current_time,balance_before,balance_after,transaction_type):
        transaction_id=f"TXN{self.account_data['system']['next_transaction_id']:06d}"
        transaction={
            "Transaction_ID" : transaction_id,
            "Customer_ID"    : request['Customer_ID'],
            "Account_Number"  : request['Account_Number'],
            "Type"           : transaction_type,
            "Method"         : "CHEQUE",
            "Amount"         : str(amount),
            "Status"         : "SUCCESS",
            "Balance_Before" : str(balance_before),
            "Balance_After"  : str(balance_after),
            "Time_Stamp"     : current_time
        }
        self.transaction_data['transactions'].append(transaction)
        self.account_data["system"]["next_transaction_id"]+=1
        self.save_account_data()
        self.save_transaction_data()
        return transaction
    
    def cheque_deposit(self,request):
        amount=Decimal(request['Amount'])
        
        current_time=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        found=False
        for account in self.account_data['accounts']:
            if request['Account_Number']==account['Account_Number']:
                found=True
                balance_before=Decimal(account['Balance'])
                balance_after=balance_before+amount
                account['Balance']=str(balance_after)
                account['Last_Updated'] = current_time
                break
        if not found:
            return
        return amount,current_time,balance_before,balance_after
    
    ###############
    def approve_cheque_withdraw(self,request):
        result=self.cheque_withdraw(request)
        if not result  :
            return
        amount,current_time,balance_before,balance_after=result
        self.save_cheque_approve(request,amount,current_time,balance_before,balance_after,"WITHDRAW")
        self.approve_request_status(request)
        self.approve_notification(request)
    def cheque_withdraw(self,request):   
        amount=Decimal(request['Amount'])
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        
        
        for account in self.account_data['accounts']:
            if request['Account_Number']==account['Account_Number']:
                found=True
                balance_before=Decimal(account['Balance'])
                
                if balance_before-amount<500:
                    print("Minimum account balance must be 500.")
                    return
                current_time=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")      
                balance_after=balance_before-amount
                account['Balance']=str(balance_after)
                account['Last_Updated'] = current_time
                
                return amount,current_time,balance_before,balance_after
        return
    ################    
    def approve_phone_number_change(self,request):
        found=False
        for customer in self.account_data['customers']:
            if request['Customer_ID']==customer['Customer_ID']:
                found=True
                customer['Phone_Number']=request['New_Phone']
                
                break
        if not found:
            return
        
        self.save_account_data()
        self.approve_request_status(request)
        self.approve_notification(request)
        print("="*60)
        print("                         PHONE NUMBER UPDATED SUCCESSFULLY")
        print("="*60)
        print(f"\nCustomer ID     : {request['Customer_ID']}\n")
        print(f"Account Number    : {self.mask_account_number(request['Account_Number'])}\n")
        print(f"Old Phone         : {request['Current_Phone']}\n")
        print(f"New Phone         : {request['New_Phone']}\n")
        print(f"Request Status    : APPROVED\n")
        print("="*60)

    ###################
    def approve_address_change(self,request):
        found=False
        for customer in self.account_data['customers']:
            if request['Customer_ID']==customer['Customer_ID']:
                found=True
                customer['Address']=request['New_Address']
                break
        if not found:
            return
        self.save_account_data()
        self.approve_request_status(request)
        self.approve_notification(request)
        print("="*60)
        print("                         ADDRESS UPDATED SUCCESSFULLY")
        print("="*60)
        print(f"\nCustomer ID     : {request['Customer_ID']}\n")
        print(f"Account Number    : {self.mask_account_number(request['Account_Number'])}\n")
        print(f"Old Address         : {request['Current_Address']}\n")
        print(f"New Address         : {request['New_Address']}\n")
        print(f"Request Status    : APPROVED\n")
        print("="*60)
    ##################
    def approve_account_closure(self,request):
        current_time=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        find=False
        for account in self.account_data['accounts']:
            if request['Account_Number']==account['Account_Number']:
                find=True
                if Decimal(account['Balance'])>0:

                    self.closure_rejection_message()
                    return False
                if account['Status']!="ACTIVE":
                    print("Account is already closed or inactive.")
                    return False
                account['Status']="CLOSED"
                account['Last_Updated']=current_time
               
                break 
        if not find:
            return False
        self.save_account_data()
        self.approve_request_status(request)
        self.approve_notification(request)
        print("="*60)
        print("                                       ACCOUNT CLOSED SUCCESSFULLY")
        print("="*60)
        print(f"\nCustomer ID   : {request['Customer_ID']}\n")
        print(f"Account Number  : {self.mask_account_number(request['Account_Number'])}\n")
        print(f"Account Status  : CLOSED\n")
        
        print("="*60)
        return True
    def closure_rejection_message(self):
        print("="*60)
        print("                              ACCOUNT CANNOT BE CLOSED")
        print("="*60)
        print("\nReason :\n")
        print("Your account balance is not zero.\n\nPlease withdraw or transfer the remaining balance before submitting an account closure request.\n")
        print("="*60)

    def reject_request(self,request):
        if request['Request_Type']=="CHEQUE_DEPOSIT":
            self.reject_cheque_deposit(request)
        elif request['Request_Type']=="CHEQUE_WITHDRAW":
            self.reject_cheque_withdraw(request)
        elif request['Request_Type']=="PHONE_NUMBER_CHANGE":
            self.reject_phone_number_change(request)
        elif request['Request_Type']=="ADDRESS_CHANGE":
            self.reject_address_change(request)
        elif request['Request_Type']=="ACCOUNT_CLOSURE":
            self.reject_account_closure(request)

    def reject_cheque_deposit(self, request):

        result=self.reject_request_status(request)

        if result:
            self.reject_notification(request)
            print("Cheque deposit request rejected successfully.")
        else:
            print("Request is already completed.")

    def reject_cheque_withdraw(self, request):

        result=self.reject_request_status(request)
        if result:
            self.reject_notification(request)
            print("Cheque withdraw request rejected successfully.")
        else:
            print("Request is already completed.")
    def reject_phone_number_change(self, request):

        result=self.reject_request_status(request)
        if result:
            self.reject_notification(request)
            print("Phone number change request rejected successfully.")
        else:
            print("Request is already completed.")

    def reject_address_change(self, request):

        result=self.reject_request_status(request)
        if result:
            self.reject_notification(request)
            print("Address change request rejected successfully.")
        else:
            print("Request is already completed.")

        


    def reject_account_closure(self, request):

        result=self.reject_request_status(request)
        if result:
            self.reject_notification(request)
            print("Account closure request rejected successfully.")
        else:
            print("Request is already completed.")

        

    def reject_request_status(self,request):

        if request['Status'] != "PENDING":
            return False

        current_date=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        request['Status']="REJECTED"
        request['Completed_Date']=current_date
        request['Admin_Remark']="Rejected"

        self.save_request_data()

        return True
    def reject_notification(self,request):
        
        if request['Request_Type']=="CHEQUE_DEPOSIT":
            Title=  "Cheque Deposit Rejected"
            Message= f"Your cheque deposit request has been rejected.\n₹{request['Amount']} has not been  credited to your account."
        elif request['Request_Type']=="CHEQUE_WITHDRAW":
            Title="Cheque Withdrawal Rejected"
            Message=f"Your cheque withdrawal request has been Rejected.\n₹{request['Amount']} has not been debited from your account."
        elif request['Request_Type']=="PHONE_NUMBER_CHANGE":
            Title="Phone Number Change Rejected"
            Message="Your phone number change request has been Rejected .\nYour existing phone number remains unchanged."
        elif request['Request_Type']=="ADDRESS_CHANGE":
            Title="Address Update Rejected"
            Message="Your address update request has been  Rejected.\nYour existing address remains unchanged."
        elif request['Request_Type']=="ACCOUNT_CLOSURE":
            Title="Account Closure Rejected"
            Message="Your account closure request has been rejected.\nYour account remains active."
        else:
           Title="Request Rejected"
           Message="Your request has been Rejected."
        notification_id=f"NTF{self.account_data['system']['next_notification_id']:06d}"
        notification={
            "Notification_ID" : notification_id,
            "Customer_ID" : request['Customer_ID'],
            "Account_Number" : request['Account_Number'],
            "Title" : Title,
            "Message" : Message,
            "Status" : "UNREAD",
            "Time_Stamp":datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        }
        self.notification_data['notifications'].append(notification)
        self.account_data['system']['next_notification_id']+=1
        self.save_account_data()
        self.save_notification_data()

    def request_history(self):
        while True:
            print('='*60)
            print("               REQUEST HISTORY")
            print('='*60)
            print("\n1. View All Requests\n\n2. View Approved Requests\n\n3. View Rejected Requests\n\n4. Back\n")
            print('='*60)
            choice=self.menu_choice_validations(1,4)
            if choice==1:
                result_list=self.view_all_requests()
                if not result_list:
                    print("="*60)
                    print("No requests available.")
                    print("="*60)
                    continue

                
                self.display_requests(result_list,"ALL REQUEST")
                    
            elif choice==2:
                result_list=self.view_all_requests()
                if not result_list:
                    print("="*60)
                    print("No requests available.")
                    print("="*60)
                    continue

                
                result=self.approved_requests(result_list)
                if result:
                    self.display_requests(result,"APPROVED REQUEST")
                else:
                    print("="*60)
                    print("No approved requests available.")
                    print("="*60)

                continue
            elif choice==3:
                result_list=self.view_all_requests()
                if not result_list:
                    print("="*60)
                    print("No requests available.")
                    print("="*60)
                    continue

                
                reject_list=self.rejected_requests(result_list)
                if reject_list:
                    self.display_requests(reject_list,"REJECTED REQUEST")
                else:
                    print("="*60)
                    print("No rejected requests available.")
                    print("="*60)

                continue
            elif choice==4:
                break
            else:
                print("Invalid Choice!")

    def view_all_requests(self):
        request_history_list=[]
        for requests in self.request_data['requests']:
            request_history_list.append(requests)
        if not request_history_list:
            return
        return request_history_list
    def display_requests(self,requests,message):
        print("="*60)
        print(f"                                 {message} HISTORY")
        print("="*60)
        for number,request in enumerate(requests,start=1):
            print(f"\n{number}. Request ID : {request['Request_ID']}\n")
            print(f"Customer ID      : {request['Customer_ID']}")
            print(f"Account Number   : {self.mask_account_number(request['Account_Number'])}")
            print(f"Request Type     : {request['Request_Type']}")
            print(f"Status           : {request['Status']}")
            print(f"Request Date     : {request['Request_Date']}")
            print(f"Completed Date   : {request['Completed_Date']}")
            print(f"Admin Remark     : {request['Admin_Remark']}\n")
            print("-"*60)

        print("="*60)
        
        print("="*60)
        while True :
            back=input("Want to Back (enter b) :").strip().upper()
            if back not in ["B"]:
                print("Invalid Response!")
                continue
            break
        if back=="B":
            return
        
    def approved_requests(self,requests):
        approved_request_list=[]
        for request in requests:
            if request['Status']=="APPROVED":
                approved_request_list.append(request)
        if not approved_request_list:
            return
        return approved_request_list
    def  rejected_requests(self,requests):
        rejected_request_list=[]
        for request in requests:
            if request['Status']=="REJECTED":
                rejected_request_list.append(request)
        if not rejected_request_list:
            return
        return rejected_request_list
      
    #############Notification Management##############
    def notification_management_system(self):
        while True:
            print("="*60)  
            print("                                NOTIFICATION MANAGEMENT") 
            print("="*60)
            print("\n1. View Unread Notifications\n\n2. View All Notifications\n\n3. Back\n")   
            print("="*60)   
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                result=self.all_notification()
                if result:
                    selected_result=self.view_unread_notification(result)
                    if selected_result:
                        specific_notification=self.select_notification(selected_result,"UNREAD")
                        if specific_notification:
                            self.display_selected_notification(specific_notification)
                            continue
            elif choice==2:
                result=self.all_notification()
                if result:
                    specific_notification=self.select_notification(result,"ALL")
                    if specific_notification:
                        self.display_selected_notification(specific_notification)
                        continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")

    def all_notification(self):
        notification_list=[]
        for notifications in self.notification_data['notifications']:
            
            notification_list.append(notifications)
        if not notification_list:
            print("No notifications available.")
            return
        return notification_list
    def view_unread_notification(self,notification_list):
        unread_notification=[]
        
        for notifications in notification_list:
            if notifications["Status"] == "UNREAD":
                unread_notification.append(notifications)
                
        
            
        if not unread_notification:
            print("No unread notifications available.")
            return
        return unread_notification
    def select_notification(self,unread_notification,message):
        print("="*60)
        print(f"       {message} NOTIFICATIONS")
        print("="*60)
        for number,notification in enumerate(unread_notification,start=1):
            print(f"\n{number}. {notification['Notification_ID']}\n")
            print(f"{notification['Title']}\n")
            print(f"{notification['Time_Stamp']}\n")
            print('-'*60)
        
        index=len(unread_notification)+1
        print(f"{index}. Back")
        print("="*60)
        choice=self.menu_choice_validations(1,index)
        if choice==index:
            return
        selected_notification=unread_notification[choice-1]
        return selected_notification
    def display_selected_notification(self,selected_notification):
        print("="*60)
        print("                                          NOTIFICATION DETAILS")
        print("="*60)
        print(f"\nNotification ID : {selected_notification['Notification_ID']}\n")
        print(f"Customer_ID  : {selected_notification['Customer_ID']}")
        print(f"Account Number  :  {self.mask_account_number(self.select_notification['Account_Number'])}\n")
        print(f"Title           : {selected_notification['Title']}\n")
        print("-"*60)
        print(f"Message : {selected_notification['Message']}\n")
        print('-'*60)
        print(f"\nDate & Time : {selected_notification['Time_Stamp']}\n")
        selected_notification['Status']="READ"
        print(f"Status  : {selected_notification['Status']}")
        print("="*60)
        self.save_notification_data()
        
        
    #### Transaction Management ##############
    def transaction_management(self):
        while True:
            print("="*60)
            print("                                   TRANSACTION MANAGEMENT")
            print("="*60)
            print(f"\n1. View All Transactions\n\n2. Search Transaction\n\n3. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                result=self.view_all_transaction()
                if result:
                    self.select_transaction(result)
            elif choice==2:
                self.search_transaction_admin()
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
    def view_all_transaction(self):
        all_transaction=[]
        for transaction in self.transaction_data['transactions']:
            all_transaction.append(transaction)
        if not all_transaction:
            print("No transactions are available. ")
            return
        return all_transaction
               
    def select_transaction(self,all_transaction):
        print("="*60)
        print("                            ALL TRANSACTIONS")
        print("="*60)
        print("="*60)
        for transaction in all_transaction:
            if transaction['Type']=="WITHDRAW" or transaction['Type']=="DEPOSIT":
               self.deposit_withdraw_transaction_type(transaction)
            elif transaction['Type']=="TRANSFER":
               self.transfer_type(transaction)
        
    def deposit_withdraw_transaction_type(self,transaction):
        
        print(f"Transaction ID : {transaction['Transaction_ID']}")
        print(f"Account Number : {self.mask_account_number(transaction['Account_Number'])}")
        print(f"Type           : {transaction['Type']}")
        print(f"Amount         : ₹{transaction['Amount']}")
        print(f"Method           : {transaction['Method']}")
        print(f"Status         : {transaction['Status']}")
        print(f"Date & Time    : {transaction['Time_Stamp']}")
        print("-"*60)
    def transfer_type(self,transaction):
        print(f"Transaction ID : {transaction['Transaction_ID']}")
        print(f"Sender Account Number        : {self.mask_account_number(transaction['Sender_Account_Number'])}")
        print(f"Receiver Account Number     : {self.mask_account_number(transaction['Receiver_Account_Number'])}")
        print(f"Type           : {transaction['Type']}")
        print(f"Amount         : ₹{transaction['Amount']}")
        print(f"Status         : {transaction['Status']}")
        print(f"Date & Time    : {transaction['Time_Stamp']}")
        print("-"*60)

    def search_transaction_admin(self):
        while True:
            print("="*60)
            print("SEARCH TRANSACTION")
            print("="*60)
            print("\nSearch By:\n")
            print(f"1. Transaction ID\n\n2. Account Number\n\n3. Back")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            print("-"*60)
            if choice==1:
                self.search_by_transaction_id()
                continue
            elif choice==2:
                self.search_by_account_number()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")

            print("="*60)
    def search_by_transaction_id(self):
        transaction_id=input("Enter Transaction ID : ").strip()
        found=False
        for transaction in self.transaction_data['transactions']:
            if transaction_id==transaction['Transaction_ID']:
                found=True
                if transaction['Type'] in ["WITHDRAW", "DEPOSIT"]:
                    print('='*60)
                    self.deposit_withdraw_transaction_type(transaction)
                elif transaction['Type']=="TRANSFER":
                    print('='*60)
                    self.transfer_type(transaction)
        if not found:
            print("No Transactions are available in this transaction id.")
            return
    def search_by_account_number(self):
        
        account_number=input("Enter Account Number : ").strip()
        found=False
        for transaction in self.transaction_data['transactions']:
            
            if transaction['Type'] in ["WITHDRAW", "DEPOSIT"]:
                if account_number==transaction['Account_Number']:
                    found=True
                    print('='*60)
                    self.deposit_withdraw_transaction_type(transaction)
            elif transaction['Type']=="TRANSFER":
                if account_number==transaction['Sender_Account_Number'] or account_number==transaction['Receiver_Account_Number']:
                    found=True
                    print('='*60)
                    self.transfer_type(transaction)
        if not found:
            print("No Transactions are available in this account number.")
            return
    ###### Account_Management#######
    def account_management(self):
        while True:
            print("="*60)
            print("                     ACCOUNT MANAGEMENT")
            print("="*60)
            print("\n1. View All Accounts\n\n2. Search Account\n\n3. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.view_all_accounts()
                continue
            elif choice==2:
                self.search_account()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
    def view_all_accounts(self):
        print("="*60)
        print("                                  VIEW ALL ACCOUNTS")
        print("="*60)
        all_accounts=[]
        for accounts in self.account_data['accounts']:
            all_accounts.append(accounts)
        if not all_accounts:
            print("No account found!")
            return 
        for number,account in enumerate(all_accounts,start=1):
            print(f"\nAccount{number}\n")
            self.display(account)
    def display(self,account):
        print(f"Account Number : {self.mask_account_number(account['Account_Number'])}")
        print(f"Customer ID    : {account['Customer_ID']}")
        print(f"Bank Name      : {account['Bank_Name']}")
        print(f"Branch Name    : {account['Branch_Name']}")
        print(f"Account Type   : {account['Account_Type']}")
        print(f"Balance        : ₹{account['Balance']}")
        print(f"Status         : {account['Account_Status']}")
        print(f"Created Date   : {account['Created_Date']}")

    def search_account(self):
        while True:
            print("="*60)
            print("                                    SEARCH ACCOUNT")
            print("="*60)
            print("\nSearch By:\n")
            print("1. Account Number\n\n2. Customer ID\n\n3. Back\n")
            print("="*60)
            choice=self.menu_choice_validations(1,3)
            if choice==1:
                self.search_account_by_account_number()
                continue
            elif choice==2:
                self.search_account_by_customer_id()
                continue
            elif choice==3:
                break
            else:
                print("Invalid Choice!")
            
    def search_account_by_account_number(self):
        print("="*60)
        print("                                 ACCOUNT DETAILS")
        print("="*60)
        found=False
        account_number=input("Enter account number : ").strip()
        for accounts in self.account_data['accounts']:
            if account_number==accounts['Account_Number']:
                found=True
                self.display(accounts)
        if not found:
            print("No account details are available in this account number.")
            return
        print("="*60)
    def search_account_by_customer_id(self):
        print("="*60)
        print("                                 ACCOUNT DETAILS")
        print("="*60)
        accounts_list=[]
        customer_id=input("Enter Customer ID : ").strip()
        for accounts in self.account_data['accounts']:
            if customer_id==accounts['Customer_ID']:
                accounts_list.append(accounts)
        if not accounts_list:
            print("No accounts are found.")
            return
        if len(accounts_list)>1:
            for number,account in enumerate(accounts_list,start=1):
                print(f"\nAccount{number}\n")
                self.display(account)
       
        elif len(accounts_list)==1:
            self.display(accounts_list[0])
    ##### profile #########
    def profile(self):
        print("="*60)
        print("           ADMIN PROFILE")
        print("="*60)
        for data in self.admin_data['admins']:
            print(f"Name            : {data['Full_Name']}\n")
            print(f"Role            : {data['Role']}\n")
            print(f"Email           : {data['Email']}\n")
            print(f"Phone Number    : {data['Phone_Number']}\n")
            print(f"Status          : {data['Status']}\n")

        print("="*60)
    def login_admin(self):
        print("="*60)
        print("                              ADMIN LOGIN")
        print("="*60)
        while True:
            id=input("Enter System ID : ").strip()
            if id!=self.admin_data["System_ID"]:
                print("System ID is incorreect!")
                continue
            break
        while True:
            password=input("Enter Password  : ").strip()
            if password!=self.admin_data['Password']:
                print("Password is incorrect!")
                continue
            break
    
        for admin in self.admin_data['admins']:
            if admin['Status']=="ACTIVE":
                print("Login Successfull.")
                admin['Last_Login']=datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                break
        self.save_admin_data()


    def change_password_admin(self):
        print("="*60)
        print("                            CHANGE SYSTEM PASSWORD")
        print("="*60)
        while True:
            current_password=input("Enter Current Password : ")
            if current_password!=self.admin_data["Password"]:
                print("Enter Correct Password.")
                continue
            break
        while True:
            new_password=input("Enter New Password : ")
            confirm_password=input("Confirm New Password : ")
            if new_password!=confirm_password:
                print("Password not match!")
                continue
            if new_password==current_password:
                print("Enter a new password!")
                continue
            break
        print("Password changed successfully.")
        self.admin_data['Password']=new_password
        self.save_admin_data()
        print("="*60)

       
    # ---Save all data---
    def save_account_data(self):
        save_accounts(self.account_data)
    def save_transaction_data(self):
        save_transactions(self.transaction_data)
    def save_request_data(self):
        save_requests(self.request_data)
    def save_admin_data(self):
        save_admins(self.admin_data)
    def save_notification_data(self):
        save_notifications(self.notification_data)

#load all data inside Class
account_data=load_accounts()
transaction_data=load_transactions()
request_data=load_requests()
admin_data=load_admins()
notification_data=load_notifications()


manager=BankSystem(account_data,transaction_data,request_data,admin_data,notification_data)

manager.main_menu()







