import pandas, smtplib, os
from pandas import DataFrame
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def makeoutput(format_type=None, df_list=None, file_list=None, workbook_name=None, sheet_list=None):
    if format_type==str('csv').lower():
        for i in range(len(df_list)):
            df_list[i].to_csv(str(file_list[i]), encoding='utf-8', index=False)
    elif format_type==str('html_text').lower():
        lists = []
        for i in range(len(df_list)):
            html = df_list[i].to_html(na_rep = "", index = False).replace('<th>','<th bgcolor="#5D7B9D"><font color="#fff">').replace('</th>','</font></th>').replace(' <tr style="text-align: right;">', '<tr style="text-align: center;">')
            lists.append(html)
        return lists
    elif format_type==str('htmlfile').lower():
        for i in range(len(df_list)):
            df_list[i].to_html(str(file_list[i]), index = False)
    elif format_type==str('xlsx').lower():
        writer = pandas.ExcelWriter(workbook_name,engine='xlsxwriter')
        for dataframe, sheet in zip(df_list, sheet_list):
            dataframe.to_excel(writer, sheet_name=sheet, startrow=0 , startcol=0)
        writer.save()
        
def sendmail(mailserver=None, email=None,password = None,to = None,cc = None, bcc = None, subject = None, message = None, messageHTML = None, files = None):
    if mailserver.lower()=='gmail':
        host = 'smtp.gmail.com'
        port = 587
    elif mailserver.lower()=='yahoo':
        host = 'smtp.mail.yahoo.com'
        port = 465
    elif mailserver.lower()=='outlook':
        host = 'smtp.mail.outlook.com'
        port = 587
    msg = MIMEMultipart()
    msg.attach(MIMEText(str(message or ''), 'plain'))
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = ', '.join(to)
    try:
        msg['Cc'] = ', '.join(cc)
    except Exception:
        pass
    try:
        msg['Bcc'] = ', '.join(bcc)
    except Exception:
        pass
    try:
        msg.attach(MIMEText(messageHTML, 'html'))
    except Exception:
        pass
    try:
        for f in files:
            cwd = str(os.getcwd())
            attachment = open(cwd+str('/')+str(f), "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % str(f))
            msg.attach(p)
    except Exception:
        pass
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, to, text)
    server.quit()