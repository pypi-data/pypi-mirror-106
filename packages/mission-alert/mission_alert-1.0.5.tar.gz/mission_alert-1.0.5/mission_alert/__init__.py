import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(smtp_host, smtp_user, smtp_pwd, smtp_port , subject, body):
    '''
    '''
    smtp_host = smtp_host      # 发送邮件的smtp服务器（从QQ邮箱中取得）
    smtp_user = smtp_user # 用于登录smtp服务器的用户名，也就是发送者的邮箱
    smtp_pwd = smtp_pwd  # 授权码，和用户名user一起，用于登录smtp， 非邮箱密码
    smtp_port = smtp_port       # smtp服务器SSL端口号，默认是465
    sender = smtp_user    # 发送方的邮箱

    content = MIMEText(body, 'html', 'utf-8')
    message = MIMEMultipart('related')
    # message['From'] =formataddr(['string',sender])
    message['From'] = sender
    message['To'] = sender            # 收件人列表
    message['Subject'] = subject                # 邮件标题
    message.attach(content)

    try:
        smtpSSLClient = smtplib.SMTP_SSL(smtp_host, smtp_port)   # 实例化一个SMTP_SSL对象
        loginRes = smtpSSLClient.login(smtp_user, smtp_pwd)      # 登录smtp服务器
        print(f"登录结果：loginRes = {loginRes}")    # loginRes = (235, b'Authentication successful')
        if loginRes and loginRes[0] == 235:
            print(f"登录成功，code = {loginRes[0]}")
            smtpSSLClient.sendmail(sender, sender, message.as_string())
            print(f"mail has been send successfully. message:{message.as_string()}")
        else:
            print(f"登陆失败，code = {loginRes[0]}")
    except Exception as e:
        print(f"发送失败，Exception: e={e}")




