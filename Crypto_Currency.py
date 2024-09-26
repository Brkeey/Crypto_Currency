import requests # import modules
from tkinter import *
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys





url = "api.coincap.io/v2/assets" # API Url
API_KEY = "" # API Key (optional)

response = requests.get("https://{}".format(url)).json() 
#  index_mail = "" --> [""]


data_dict = response
data_list = data_dict["data"]



def get_mail():
    # Gmail email sunucusuna bağlanıyoruz
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(mail_entry, pass_entry)

        mesaj = MIMEMultipart()
        mesaj["From"] = "emailkullanicim@gmail.com"           # Gönderen
        mesaj["Subject"] = "Python Smtp ile Mail Gönderme"    # Konusu

        body = """

        Python ile smtp ve email modülünü kullanarak mail gönderiyorum.

        """

        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail başarılı bir şekilde gönderildi.")
        mail.close()

    # Eğer mesaj gönderirken hata olursa, hata mesajını konsole yazdırıyorum.
    except:
        print("Hata:", sys.exc_info()[0])





def get_crypto_info():
    crypto_name_input = crypto_name_entry.get()
    x = mail_entry.get()
    print(x)

    for currency in data_list:
        if crypto_name_input == currency['id']:
            global crypto_name, crypto_price, crypto_symbol, crypto_rank, crypto_volume, crypto_max_supply
            crypto_name = currency['name']
            crypto_price = currency['priceUsd']
            crypto_symbol = currency['symbol']
            crypto_rank = currency['rank']
            crypto_volume = currency['volumeUsd24Hr']
            crypto_max_supply = currency['supply']

            crypto_name_label['text'] = crypto_name
            crypto_symbol_label['text'] = crypto_symbol
            crypto_price_label['text'] = crypto_price
            crypto_rank_label['text'] = crypto_rank
            crypto_volume_label['text'] = crypto_volume
            crypto_max_supply_label['text'] = crypto_max_supply
            return crypto_price, crypto_symbol, crypto_rank, crypto_name, crypto_volume, crypto_max_supply
    



app = Tk()
app.geometry('300x550')
app.title("Crypto Currency")

crypto_name_entry = Entry(app, justify='center')
crypto_name_entry.pack(fill=BOTH, ipady=10, padx=10, pady=5)
crypto_name_entry.focus()

mail_entry = Entry(app)
mail_entry.config(text="Enter Mail:", justify="center")
mail_entry.pack(pady=10)


passEntry = Entry(app)
passEntry.config(text="Enter Mail:", justify="center")
passEntry.pack(pady=10)

searchButton = Button(app, text='Search', font=('Arial', 15), command=get_crypto_info)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

crypto_name_label_1 = Label(app, font=('Arial', 20), text="Name:", fg="red")
crypto_name_label_1.pack()

crypto_name_label = Label(app, font=('Arial', 15))
crypto_name_label.pack()

crypto_symbol_label_1 = Label(app, font=('Arial', 20), text="Symbol:", fg="red")
crypto_symbol_label_1.pack()

crypto_symbol_label = Label(app, font=('Arial', 15))
crypto_symbol_label.pack()

crypto_price_label_1 = Label(app, font=('Arial', 20), text="Price:", fg="red")
crypto_price_label_1.pack()

crypto_price_label = Label(app, font=('Arial', 15))
crypto_price_label.pack()

crypto_rank_label_1 = Label(app, font=('Arial', 20), text="Rank:", fg="red")
crypto_rank_label_1.pack()

crypto_rank_label = Label(app, font=('Arial', 15))
crypto_rank_label.pack()

crypto_volume_label_1 = Label(app, font=('Arial', 20), text="24 Hours Volume:", fg="red")
crypto_volume_label_1.pack()

crypto_volume_label = Label(app, font=('Arial', 15))
crypto_volume_label.pack()

crypto_max_supply_label_1 = Label(app, font=('Arial', 20) ,text="MaxSupply:", fg="red")
crypto_max_supply_label_1.pack()

crypto_max_supply_label = Label(app, font=('Arial', 15))
crypto_max_supply_label.pack()







app.mainloop()

        


            






    







    
        
        
        
        
    



    








































        