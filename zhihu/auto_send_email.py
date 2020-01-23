"""
发送邮件 授权码：hhggbb477910  问题：图片是作为附件发送的，且后缀名为bin TODO
"""
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

# SMTP服务器,这里使用163邮箱
mail_host = "smtp.163.com"
# 发件人邮箱
mail_sender = "13112361595@163.com"
# 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
mail_license = "hhggbb477910"
# 收件人邮箱，可以为多个收件人，逗号分隔
# mail_receivers = ["248165337@qq.com", "627034718@qq.com"]
mail_receivers = ["248165337@qq.com"]
# 构建MIMEMultipart对象代表邮件本身
mm = MIMEMultipart('related')

# 邮件主题（标题）
subject_content = """Python邮件测试"""
# 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
mm["From"] = "hgb<13112361595@163.com>"
# 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
# mm["To"] = "receiver_1_name<248165337@qq.com>,receiver_2_name<627034718@qq.com>"
mm["To"] = "hgb<248165337@qq.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content, 'utf-8')
# 邮件正文内容
body_content = """测试邮件"""
# 构造文本,参数 1：正文内容；2：文本格式；3：编码方式
message_text = MIMEText(body_content, "plain", "utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)

# 二进制读取图片
image_data = open('a.jpg', 'rb')
# 设置读取获取的二进制数据
message_image = MIMEImage(image_data.read())
# 关闭刚才打开的文件
image_data.close()
# 添加图片文件到邮件信息当中去
mm.attach(message_image)

# 构造附件
atta = MIMEText(open('a.xlsx', 'rb').read(), 'base64', 'utf-8')
# 设置附件信息 Disposition:排列 attachment：附件
atta["Content-Disposition"] = 'attachment; filename="a.xlsx"'
# 添加附件到邮件信息当中去
mm.attach(atta)

# 发送邮件
# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，参数 1：邮箱地址；2：邮箱授权码
stp.login(mail_sender, mail_license)
# 发送邮件，参数 1：发件人邮箱地址；2：收件人邮箱地址；3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()
