import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 設定寄件者和收件者
sender_email = "danield880527@gmail.com"
receiver_email = "收件者@gmail.com"

# 建立郵件物件
msg = MIMEMultipart()

# 設定主旨
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "這是一封測試郵件"

# 郵件內容
body = "這是一封測試郵件。"
msg.attach(MIMEText(body, 'plain'))

# 設定 SMTP 伺服器
smtp_server = "smtp.gmail.com"
smtp_port = 587

# 登入郵件帳號
username = "你的寄件者@gmail.com"
password = "你的郵件密碼"

# 建立 SMTP 連線
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("郵件已成功寄出！")
except Exception as e:
    print(f"發生錯誤：{e}")
