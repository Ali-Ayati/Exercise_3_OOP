# Exercise_3_OOP

This directory contains **5 Python exercises** focused on object-oriented programming (OOP) principles such as:
- Abstract classes
- Inheritance
- Method overriding
- Static methods
- Dunder methods
- Encapsulation

Each exercise is saved in a separate file in the format: `q<number>_<task-name>.py`

---

## Problem Descriptions

### 🔹 Question 1 – q1_account_base.py _ کلاس حساب بانکی 
*Description:*  

کلاس ی با نام Account بسازید که ب ه عنوان abstract برای سه کلاس دیگر مورد اس تفاده واقع می شود. این کلاس دو مشخ صه balance و number را دارد که به ترتیب نشان دهنده موجودی و شماره حساب می باشند. همچنین این کلاس دارای مشخصه دیگری تحت عنوان_ transactions می باشد که لیست تراکنش های انجام شده را نشان می دهد . برای این کلاس سه متد برای واریز به حساب، برداشت از حساب و نمایش موجودی تعریف کنید . دقت کنید که پس از هر برداشت یا واریز مقدار مبادله شده در لیست تراکنش ها ذخیره شود (مقدار مثبت در صورت واریز و مقدار منفی در صورت برداشت.)

پ.ن: متد __ str __این ک الس را به نحوی تعریف کنید که به صورت number: balance نمایش داده
شود و balance را تا دو رقم اعشار گرد کنید .

This task implements an abstract base class `Account` that provides the foundation for all other account types.  
Includes deposit and withdraw functionality, a transaction history.

---

### 🔹 Question 2 – q2_checking_account.py _ کلاس حساب جاری
*Description:*  

کلاسی با نام CheckingAccount بسازید که از کلاس Accountارث بری می کند .یک مشخصه کالسی برای این کلاس تحت عنوانamount_min تعریف کنید که حداقل مقدار موجودی الزم برای تشکیل حساب را نمایش دهد (به عنوان مثال100000) و بر اساس این مقدار تشکیل حساب جدید انجام شود. همچنین متد __str__آن را به نحوی بنویسید که خروجی آن به شکل زیر باشد :

” Checking Account, Number: number, Balance: balance”

A subclass of `Account` called `CheckingAccount`, which enforces a minimum initial balance (`min_amount = 100000`) during account creation.  
Custom `__str__()` method is implemented to reflect the account type.

---

### 🔹 Question 3 – q3_saving_account.py _ کلاس حساب پس انداز
*Description:*  

کلاسی با نام SavingAccountبسازید که از کلاس Accountارث بری می کند .متدی برای این کلاس پیاده سازی نمایید که برای دارنده حساب نسبت دخل وخرج حساب را محاسبه نماید ( نسبت مجموع واریزها به مجموع برداشت ها ).متد __str__آن را به نحوی بنویسید که خروجی آن به شکل زیر باشد :

”Saving Account, Number: number, Balance: balance“

Implements a `SavingAccount` class that calculates the ratio of total income (deposits) to expenses (withdrawals).  
Optimized with tracking total deposit and withdraw amounts for performance.

---

### 🔹 Question 4 – q4_currency_account.py _ کلاس حساب ارزی
*Description:*  

کلاسی با نامCurrencyAccount بسازید که از کلاس Accountارث بری می کند .یک متد ایستا برای این کلاس طراحی کنید که وظیفه آن تبدیل واحد ریال به دلار باشد به طوری که دارنده حساب ارزی قابلیت مشاهده موجودی خود بر اساس دالر قیمت روز را داشته باشد . متدی برای این کالس طراحی کنیدکه با استفاده از آن دارنده حساب لیست تراکنش های خود براساس دلار را مشاهده نماید . متد __str__آن را به نحوی بنویسید که خروجی آن به شکل زیر باشد :

” Business Account, Number: number, Balance: balance”

Implements a `CurrencyAccount` class with a static method to convert the account balance and transaction history from Rial to USD using an exchange rate.  
Validates the rate and formats the converted output to two decimal places.

---

### 🔹 Question 5 & 6 – q5_6_custumer_ch1_and_ch2.py _ کلاس مشتری – بخش اول , کلاس مشتری – بخش دوم
*Description:*  

بخش اول: 

کلاسی با نامCostumerبسازید که3مشخصه name،ssnوtype_acc را داشته باشدکه type_acc دارای مقادیر مجازC،Sو Bاست. همچنینnameو ssnنیز نمایانگر نام و کدملی مشتری می باشد . سه متد برای افتتاح حساب ایجاد کنیدکه هر یک از متد ها متناظر با انواع حسابی است.که در بالا تعریف شده است. ورودی این سه متد موجودی و شماره حساب میباشد . 

بخش دوم:

برای کلاس Costumerمتدهای زیر را تعریف کنید :

متد :balance_showاین متد موجودی حساب مشتری را با فرمت مناسب نمایش می دهد .

متد :deposit_makeاین متد مقداری را به عنوان ورودی می گیرد وعملیات واریز به حساب را برای مشتری انجام میدهد .

متد :withdraw_makeاین متد مقداری را به عنوان ورودی می گیرد و عملیات برداشت از حساب را برای مشتری انجام میدهد .

متد transfer_make : این متد 3 مقدار حساب مبدا، حساب مقصد و مقدار انتقال را از ورودی متد می گیرد و عملیات انتقال را با استفاده از برداشت و واریز انجام میدهد و در نهایت مقادیر موجودی دو حساب مبدا و مقصد رانمایش میدهد .

پ.ن:.ست کردن مابقی method dunder ها(مانند __add__،__ lt__و ...__eq__و) و استفاده از آنها برای عملیات گفته شده دارای نمره امتیازی می باشد.

Implements a `Customer` class that allows opening multiple accounts (`SavingAccount`, `CheckingAccount`, `CurrencyAccount`).  
Supports deposit, withdraw, and inter-account transfer with proper input validation.  
Accounts are stored in a dictionary for scalability.  
Also includes extended dunder method usage in `Account` for object comparison and arithmetic.

---

## 📝 Notes
- Account types:  
  - `S`: SavingAccount  
  - `B`: CheckingAccount  
  - `C`: CurrencyAccount  

- All accounts inherit from the `Account` base class and override required methods.
- Exception handling and edge case checking are included throughout.
- These exercises were written as part of my learning journey in object-oriented Python 🐍🚀
