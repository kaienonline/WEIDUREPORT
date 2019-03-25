# -*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
# 发件人地址，通过控制台创建的发件人地址
from WeiDuAdmin import settings

username = 'noreply@email.exuetech.com'
# 发件人密码，通过控制台创建的发件人密码
password = 'ex1234ABcd'
# 自定义的回复地址
replyto = 'mengzhaoying@exuetech.com'
# 收件人地址或是地址列表，支持多个收件人，最多30个
#rcptto = ['***', '***']
# rcptto = '***'


class EmailUtils(object):

    def __init__(self):
        pass

    def __send_email(self, subject, nickname, content, receive_emails, is_text=True):
        # 构建alternative结构
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(subject).encode()
        msg['From'] = '%s <%s>' % (Header(nickname).encode(), username)
        msg['To'] = receive_emails
        msg['Reply-to'] = receive_emails
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()
        if is_text:
            # 构建alternative的text/plain部分
            textplain = MIMEText(content, _subtype='plain', _charset='UTF-8')
            msg.attach(textplain)
        else:
            # 构建alternative的text/html部分
            texthtml = MIMEText(content, _subtype='html', _charset='UTF-8')
            msg.attach(texthtml)
            # 发送邮件
        # 发送邮件
        try:
            client = smtplib.SMTP()
            # python 2.7以上版本，若需要使用SSL，可以这样创建client
            client = smtplib.SMTP_SSL()
            # SMTP普通端口为25或80
            client.connect('smtpdm.aliyun.com', 465)
            # 开启DEBUG模式
            client.set_debuglevel(0)
            client.login(username, password)
            # 发件人和认证地址必须一致
            # 备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
            #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
            client.sendmail(username, receive_emails, msg.as_string())
            client.quit()
            print '邮件发送成功！'
        except smtplib.SMTPConnectError, e:
            print '邮件发送失败，连接失败:', e.smtp_code, e.smtp_error
        except smtplib.SMTPAuthenticationError, e:
            print '邮件发送失败，认证错误:', e.smtp_code, e.smtp_error
        except smtplib.SMTPSenderRefused, e:
            print '邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error
        except smtplib.SMTPRecipientsRefused, e:
            print '邮件发送失败，收件人被拒绝:', e.recipients
        except smtplib.SMTPDataError, e:
            print '邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error
        except smtplib.SMTPException, e:
            print '邮件发送失败, ', e.message
        except Exception, e:
            print '邮件发送异常, ', str(e)

    def send_active_code(self, code, receive_email):
        subject = u"格略维度平台激活码"
        context = u'''
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    您好，
</p>
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    感谢您使用格略维度平台，您的激活码是: %s.
    测评平台地址是：%s
</p> 
''' % (code, settings.CLIENT_HOST)
        self.__send_email(subject, u"维度平台", context, receive_email, False)

    def send_general_code(self, code, receive_email):
        subject = u"格略维度平台验证码"
        context = u'''
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    您好，
</p>
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    感谢您使用格略维度平台，您的验证码是: %s.
</p> 
''' % code
        self.__send_email(subject, u"维度平台", context, receive_email, False)

    def send_general_survey_notice(self, survey_name, receive_email):
        subject = u"格略维度平台测验通知"
        context = u'''
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    您好，
</p>
<p data-spm-anchor-id="5176.2020520150.112.i5.5a237528qmyTsk">
    您收到一份测验问卷：%s
</p> 
''' % survey_name
        self.__send_email(subject, u"维度平台", context, receive_email, False)