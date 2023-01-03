import pandas as pd
import requests, smtplib
from email.message import EmailMessage

df= pd.read_csv('filepath/file_name.csv')

for url in df['urls']:
    response = requests.get(url)
    status = response.status_code
    df['Status']=status
    if status == 404:
        print(url)
        df.to_csv('Status_404codes.csv')
        msg404 = EmailMessage()
        msg404.add_attachment()
    if status == 200:
        print(url)
        df.to_csv('Status_200codes.csv')
        msg200 = EmailMessage()
        msg200.add_attachment(df.to)

# Send email
with smtplib.SMTP('localhost') as server:
    server.send_message(msg404)
    server.send_message(msg200)




