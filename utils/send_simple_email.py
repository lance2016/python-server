import json
import smtplib
from email.mime.text import MIMEText

from config.config_parser import get_settings
email_setting = get_settings(("email",))
# 设置服务器所需信息
# 163邮箱服务器地址
mail_host = email_setting.get("mail_host")
# 163用户名
mail_user = email_setting.get("mail_user")
# 密码(部分邮箱为授权码)
mail_pass = email_setting.get("mail_pass")
# 邮件发送方邮箱地址
sender = email_setting.get('sender')
# 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
# receivers = json.loads(email_setting.get('receivers'))


# 发送邮件
def send_email(msg_title, msg_content, receive_email_list):
    return send_message(receive_email_list, message=init_message(msg_title, msg_content, receive_email_list))
    

def init_message(msg_title, msg_content, receive_email_list):
  # 设置email信息
    # 邮件内容设置
    # message = MIMEText('邮件发送内容', 'plain', 'utf-8')
    message = MIMEText(f'{msg_content}', 'plain', 'utf-8')
    # 邮件主题
    # message['Subject'] = '测试发送邮件'
    message['Subject'] = f'{msg_title}'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    # message['To'] = receive_email_list[0]
    print(message)
    return message


def send_message(receive_email_list, message):
    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receive_email_list, message.as_string())
        # 退出
        smtpObj.quit()
        return 'success'
    except smtplib.SMTPException as e:
        return f'error,{e}'  # 打印错误


# print(send_email('test_a','test_b',))