# 发送邮件
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import time
from loguru import logger
from sqlalchemy.orm import sessionmaker
from config.config import get_settings
from py_practice.model.student_model import t1
from utlis.rabbitmq_util import RabbitMQ

setting = get_settings()


def send_email(msg_title, msg_content, receive_email_list):
    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = setting.mail_host
    # 163用户名
    mail_user = setting.mail_user
    # 密码(部分邮箱为授权码)
    mail_pass = setting.mail_pass
    # 邮件发送方邮箱地址
    sender = setting.sender

    message = init_message(msg_title, msg_content, receive_email_list, sender=sender)
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    # receivers = json.loads(email_setting.get('receivers'))
    return send_message(receive_email_list, message=message, mail_host=mail_host, mail_user=mail_user, mail_pass=mail_pass, sender=sender)


def init_message(msg_title, msg_content, receive_email_list, sender):
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


def send_message(receive_email_list, message, sender, mail_host, mail_user, mail_pass):
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


def generate_data(model, num):
    data_list = []
    for i in range(num):
        entity = model()
        entity.m_id = i
        entity.name = f"lance_{i}"
        entity.identity_no = f"no_{i}"
        entity.address = f"address_{i}"
        data_list.append(entity)
    return data_list


def batch_insert_data(engine: sessionmaker, insert_list):

    t0 = datetime.now()
    engine.bulk_save_objects(insert_list)
    # engine.execute(
    #     entity.__table__.insert(),
    #     insert_list
    # )  # ==> engine.execute('insert into ttable (name) values ("NAME"), ("NAME2")')
    print(
        f"SQLAlchemy Core: Total time for {len(insert_list)} records  {str(datetime.now() - t0)} secs")


def on_message(channel, method, properties, body):
    print(body)


def rabbitmq_produce(params: dict):
    try:
        # Create the RabbitMQ object
        rmq = RabbitMQ(
            host=setting.rabbit_mq_host,
            port=setting.rabbit_mq_port,
            vhost=setting.rabbit_mq_vhost,
            username=setting.rabbit_mq_user,
            password=setting.rabbit_mq_psw
        )
        exchange = 'exchange_hello'
        queue = 'queue_hello'
        key = 'key_hello'
        rmq.bind_queue_exchange(queue=queue, exchange=exchange, routing_key=key)
        for item in params.get("msg"):
            rmq.public_msg(
                exchange=exchange,
                routing_key=key,
                json=item
            )
    except Exception as e:
        logger.error(f"error:{e}")
    finally:
        rmq.close()
