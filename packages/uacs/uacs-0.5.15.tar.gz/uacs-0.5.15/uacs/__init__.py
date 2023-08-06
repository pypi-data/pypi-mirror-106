#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------* TO DO *-------------- #

# TODO : ajouter deepl API pour traduire les massages.
# TODO : possibilitée de retirer les services de la liste
# TODO : Optimiser le code :
#  - avec des objets pour le init
#  - optimiser les imports
# TODO : integration dans pip

# --------------* IMPORT *-------------- #

import datetime
import os
import pickle
import smtplib
import ssl
import sys
import threading
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --------------* VARIABLES *-------------- #

service_check = []
services_restored = []
email_restored = []
file_ini_service = "/etc/uacs/service_monitored.conf"
file_ini_email = "/etc/uacs/email.conf"
service_name = "ultimate_auto_check_service"
path_config = "/etc/uacs/"
sender_email, email_password, receiver_email, smtp_server = "", "", "", ""
email_smtp_port = 0
running = True
number_restart = 3

# Colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


# --------------* Functions *-------------- #
def main():
    pass


def enablePrint():
    sys.stdout = sys.__stdout__


def restore(verbose):
    restore_email(verbose)
    restore_service(verbose)


def restore_service(verbose):  # Restauration des services depuis un fichier (file_ini)
    if verbose:
        enablePrint()

    global service_check, services_restored
    print("Service restoration")
    print(f"Searching for the file : {file_ini_service}")
    if os.path.isfile(file_ini_service):
        print("File found !")

        print("Opening the file ...")
        backup_file = open(file_ini_service, "rb")

        print(f"Reading variables in the file : " + file_ini_service)
        try:
            services_restored = pickle.load(backup_file)

        except:
            print("Error file empty")

        backup_file.close()

        print("Adding the backup to the buffer")
        service_check.append(services_restored)

        print(f"The {services_restored} services have been added")

    else:
        # The file does not exist
        print(f"File {file_ini_service} not found")
        os.system(f"sudo mkdir -p /etc/uacs/ && sudo touch {file_ini_service}")
        print(f"Created file {file_ini_service}")


# noinspection PyUnusedLocal
def restore_email(verbose):  # Restauration de l'email / mot de passe depuis le fichier
    if verbose:
        enablePrint()

    global sender_email, email_password, receiver_email, smtp_server, email_smtp_port, email_restored

    print("Restauration of the email address and its password")
    print(f"Searching for the file : {file_ini_email}")
    if os.path.isfile(file_ini_email):
        print("File found !")

        print("Opening the file ...")
        backup_file = open(file_ini_email, "rb")

        print(f"Reading variables in the file : " + file_ini_email)

        try:
            email_restored = pickle.load(backup_file)

            backup_file.close()

            sender_email = email_restored[0]
            email_password = email_restored[1]
            receiver_email = email_restored[2]
            smtp_server = email_restored[3]
            email_smtp_port = email_restored[4]

        except:
            print("Error file empty")

        print(f"The email adresse have been restored")

    else:
        # The file does not exist
        print(f"File {file_ini_email} not found")
        os.system(f"sudo mkdir -p /etc/uacs/ && sudo touch {file_ini_email}")
        print(f"Created file {file_ini_email}")


def append(append_service, verbose):  # Ajoute un service a la liste et l'ajoute également au fichier (file_ini)
    if verbose:
        enablePrint()

    # Verification de l'existence du service et l'enregistre
    print(f"Verification of the existence of the service {append_service} and registration ...")
    print(f""""systemctl list-unit-files | grep "^{append_service}" """)
    exist_service = os.system(f""""systemctl list-unit-files | grep "^{append_service}" """)
    if str(exist_service).find(".service"):
        print("Service exist \nSaving ...")

        print(f"Opening the file {file_ini_service}")
        backup_file = open(file_ini_service, "wb")

        print(f"Appending the service {append_service}")
        pickle.dump(append_service, backup_file)
        backup_file.close()
        service_check.append(append_service)
        print("Saved !")
    else:
        print("Service don't exist")
    print("The following services are monitored" + str(service_check))


def check_service(verbose):
    if verbose:
        enablePrint()

    # Surveille les services 1 par 1
    for i in range(len(service_check)):
        print(f"systemctl status {service_check[i]} | grep active")
        active = os.system(f"systemctl status {service_check[i]} | grep active")
        if str(active).find("inactive"):
            print(f"Service is inactive \nLaunch of the restart of the services {service_check[i]}")
            service_down(service_check[i], verbose)

        elif str(running).find("active"):
            print("Service is active")


def service_down(service, verbose):
    global active, number_restart
    if verbose:
        enablePrint()

    # Essaye de relancer 3x le service
    # et envoie un mail si il ne redémarre pas
    for i in range(number_restart):
        print(f"Relaunching n°{i}/{number_restart}")
        active = os.system(f"systemctl status {service}")
        if str(active).find("inactive"):
            os.system(f"systemctl restart {service}")
            continue
        elif str(active).find("running"):
            print(f"Successful restarting service {service}")
        else:
            print("Error, we do not know the status of this service")
            continue

    if str(active).find("inactive"):  # send mail
        print(f"Failed to restart the {service} service request to send the email")
        send_mail(service, verbose)
    else:
        pass


def send_mail(subject, verbose):
    global sender_email, email_password, smtp_server, email_smtp_port, receiver_email
    if verbose:
        enablePrint()

    # Envoie un mail
    now = datetime.datetime.now()
    cpu_usage = """grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}' """

    cpu_temp = "cat /sys/class/thermal/thermal_zone*/temp"
    cpu_temp = int(os.popen(cpu_temp).read())
    cpu_temp = "{:,}".format(cpu_temp)

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    text = ""
    html = """\
    <meta content="width=device-width" name="viewport">
    <!--[if !mso]><!-->
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <!--<![endif]-->
    <title></title>
    <!--[if !mso]><!-->
    <!--<![endif]-->
    <style type="text/css">
    		body {
    			margin: 0;
    			padding: 0;
    		}

    		table,
    		td,
    		tr {
    			vertical-align: top;
    			border-collapse: collapse;
    		}

    		* {
    			line-height: inherit;
    		}

    		a[x-apple-data-detectors=true] {
    			color: inherit !important;
    			text-decoration: none !important;
    		}
    	</style>
    <style id="media-query" type="text/css">
    		@media (max-width: 660px) {

    			.block-grid,
    			.col {
    				min-width: 320px !important;
    				max-width: 100% !important;
    				display: block !important;
    			}

    			.block-grid {
    				width: 100% !important;
    			}

    			.col {
    				width: 100% !important;
    			}

    			.col_cont {
    				margin: 0 auto;
    			}

    			img.fullwidth,
    			img.fullwidthOnMobile {
    				max-width: 100% !important;
    			}

    			.no-stack .col {
    				min-width: 0 !important;
    				display: table-cell !important;
    			}

    			.no-stack.two-up .col {
    				width: 50% !important;
    			}

    			.no-stack .col.num2 {
    				width: 16.6% !important;
    			}

    			.no-stack .col.num3 {
    				width: 25% !important;
    			}

    			.no-stack .col.num4 {
    				width: 33% !important;
    			}

    			.no-stack .col.num5 {
    				width: 41.6% !important;
    			}

    			.no-stack .col.num6 {
    				width: 50% !important;
    			}

    			.no-stack .col.num7 {
    				width: 58.3% !important;
    			}

    			.no-stack .col.num8 {
    				width: 66.6% !important;
    			}

    			.no-stack .col.num9 {
    				width: 75% !important;
    			}

    			.no-stack .col.num10 {
    				width: 83.3% !important;
    			}

    			.video-block {
    				max-width: none !important;
    			}

    			.mobile_hide {
    				min-height: 0px;
    				max-height: 0px;
    				max-width: 0px;
    				display: none;
    				overflow: hidden;
    				font-size: 0px;
    			}

    			.desktop_hide {
    				display: block !important;
    				max-height: none !important;
    			}
    		}
    	</style>
    <style id="icon-media-query" type="text/css">
    		@media (max-width: 660px) {
    			.icons-inner {
    				text-align: center;
    			}

    			.icons-inner td { margin: 0 auto; } } </style> </head> <body class="clean-body" style="margin: 0; padding: 
    			0; -webkit-text-size-adjust: 100%; background-color: #f3f2f3;"> <!--[if IE]><div class="ie-browser"><![
    			endif]--> <table bgcolor="#f3f2f3" cellpadding="0" cellspacing="0" class="nl-container" 
    			role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; border-spacing: 0; 
    			border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f3f2f3; width: 
    			100%;" valign="top" width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td 
    			style="word-break: break-word; vertical-align: top;" valign="top"> <!--[if (mso)|(IE)]><table width="100%" 
    			cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#f3f2f3"><![
    			endif]--> <div style="background-color:transparent;"> <div class="block-grid" style="min-width: 320px; 
    			max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 
    			auto; background-color: transparent;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:transparent;"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table 
    			cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:transparent"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="640" 
    			style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]--> <div class="col num12" 
    			style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 
    			0px;"> <!--<![endif]--> <div class="mobile_hide"> <table border="0" cellpadding="0" cellspacing="0" 
    			class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; 
    			border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; 
    			-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr 
    			style="vertical-align: top;" valign="top"> <td class="divider_inner" style="word-break: break-word; 
    			vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; 
    			padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top"> <table 
    			align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" 
    			style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; 
    			mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 30px solid #F3F2F3; width: 100%;" valign="top" 
    			width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td style="word-break: break-word; 
    			vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> <!--[if (
    			!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> </div> <!--[if (mso)|(IE)]></td></tr></table><![
    			endif]--> <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--> </div> </div> </div> <div 
    			style="background-color:transparent;"> <div class="block-grid" style="min-width: 320px; max-width: 640px; 
    			overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; 
    			background-color: transparent;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:transparent;background-image:url(
    			&#39;images/png-clipart-desktop-display-resolution-geometric-miscellaneous-texture.png&#39;);background
    			-position:top center;background-repeat:no-repeat"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table 
    			cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:transparent"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="640" 
    			style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:25px; padding-bottom:0px;"><![endif]--> <div class="col num12" 
    			style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:25px; padding-bottom:0px; padding-right: 0px; 
    			padding-left: 0px;"> <!--<![endif]--> <div class="mobile_hide"> <table border="0" cellpadding="0" 
    			cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; 
    			border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 
    			100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr 
    			style="vertical-align: top;" valign="top"> <td class="divider_inner" style="word-break: break-word; 
    			vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; 
    			padding-top: 50px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top"> <table 
    			align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" 
    			style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; 
    			mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid #BBBBBB; width: 100%;" valign="top" 
    			width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td style="word-break: break-word; 
    			vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; 
    			padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#393d47;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;"> 
    			<div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #393d47; font-family: 
    			Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			14px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 17px; margin-top: 
    			0; margin-bottom: 0;">Bad News…</p> </div> </div> <!--[if mso]></td></tr></table><![endif]--> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; 
    			padding-left: 0px; padding-top: 20px; padding-bottom: 28px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#555555;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:20px;padding-right:0px;padding-bottom:28px;padding-left:0px;"> <div 
    			class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; font-family: Helvetica Neue, 
    			Helvetica, Arial, sans-serif; color: #555555; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			42px; line-height: 1.2; word-break: break-word; text-align: center; font-family: Helvetica Neue, 
    			Helvetica, Arial, sans-serif; mso-line-height-alt: 50px; margin-top: 0; margin-bottom: 0;"><span 
    			style="font-size: 42px;"><strong>ONE SERVICE WAS DOWN</strong></span></p> </div> </div> <!--[if 
    			mso]></td></tr></table><![endif]--> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> </div> 
    			<!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(
    			IE)]></td></tr></table></td></tr></table><![endif]--> </div> </div> </div> <div 
    			style="background-color:transparent;"> <div class="block-grid two-up" style="min-width: 320px; max-width: 
    			640px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; 
    			background-color: #ffffff;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:#ffffff;"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" 
    			border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" 
    			cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:#ffffff"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="320" 
    			style="background-color:#ffffff;width:320px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			32px; padding-left: 32px; padding-top:60px; padding-bottom:60px;"><![endif]--> <div class="col num6" 
    			style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 318px; width: 320px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:60px; padding-bottom:60px; padding-right: 32px; 
    			padding-left: 32px;"> <!--<![endif]--> <div align="center" class="img-container center autowidth" 
    			style="padding-right: 0px;padding-left: 0px;"> <!--[if mso]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" 
    			align="center"><![endif]--><img align="center" alt="I&#39;m an image" border="0" class="center autowidth" 
    			src="./imported-from-beefreeio_files/22a5f685-42f3-4b76-9df4-08138a832c89.png" style="text-decoration: 
    			none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 100px; display: 
    			block;" title="I&#39;m an image" width="100"> <!--[if mso]></td></tr></table><![endif]--> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; 
    			padding-left: 10px; padding-top: 18px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#000000;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:18px;padding-right:10px;padding-bottom:10px;padding-left:10px;"> 
    			<div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #000000; font-family: 
    			Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			20px; line-height: 1.2; text-align: center; word-break: break-word; mso-line-height-alt: 24px; margin-top: 
    			0; margin-bottom: 0;"><span style="font-size: 20px; color: #2a272b;"><strong>""", now.day, "/", now.month, "/", now.year, " à,", now.hour, ":", now.minute, """</strong></span></p> </div> </div> <!--[if mso]></td></tr></table><![endif]--> <table border="0" 
    			cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; 
    			vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; 
    			mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top" width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td 
    			class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; 
    			-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 42px; padding-right: 0px; 
    			padding-bottom: 0px; padding-left: 0px;" valign="top"> <table align="center" border="0" cellpadding="0" 
    			cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: 
    			top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; 
    			border-top: 0px solid #BBBBBB; width: 100%;" valign="top" width="100%"> <tbody> <tr style="vertical-align: 
    			top;" valign="top"> <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; 
    			-webkit-text-size-adjust: 100%;" valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> 
    			</tbody> </table> <div align="center" class="img-container center autowidth" style="padding-right: 
    			0px;padding-left: 0px;"> <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr 
    			style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img 
    			align="center" alt="I&#39;m an image" border="0" class="center autowidth" 
    			src="./imported-from-beefreeio_files/ffe16f2a-4b7e-4bf7-982b-f45f8e096280.png" style="text-decoration: 
    			none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 100px; display: 
    			block;" title="I&#39;m an image" width="100"> <!--[if mso]></td></tr></table><![endif]--> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; 
    			padding-left: 10px; padding-top: 18px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#555555;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:18px;padding-right:10px;padding-bottom:10px;padding-left:10px;"> 
    			<div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #555555; font-family: 
    			Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			20px; line-height: 1.2; text-align: center; word-break: break-word; mso-line-height-alt: 24px; margin-top: 
    			0; margin-bottom: 0;"><span style="font-size: 20px; color: #2a272b;"><strong>""", subject, """</strong></span></p> 
    			</div> </div> <!--[if mso]></td></tr></table><![endif]--> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![
    			endif]--> </div> </div> <!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(IE)]></td><td 
    			align="center" width="320" style="background-color:#ffffff;width:320px; border-top: 0px solid transparent; 
    			border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid 
    			transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td 
    			style="padding-right: 32px; padding-left: 32px; padding-top:60px; padding-bottom:60px;"><![endif]--> <div 
    			class="col num6" style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 318px; 
    			width: 320px;"> <div class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div 
    			style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid 
    			transparent; border-right:0px solid transparent; padding-top:60px; padding-bottom:60px; padding-right: 
    			32px; padding-left: 32px;"> <!--<![endif]--> <div align="center" class="img-container center autowidth" 
    			style="padding-right: 0px;padding-left: 0px;"> <!--[if mso]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" 
    			align="center"><![endif]--><img align="center" alt="I&#39;m an image" border="0" class="center autowidth" 
    			src="./imported-from-beefreeio_files/9a9b8eb5-74f4-419f-9d55-2709c8d4ba97.png" style="text-decoration: 
    			none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 100px; display: 
    			block;" title="I&#39;m an image" width="100"> <!--[if mso]></td></tr></table><![endif]--> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; 
    			padding-left: 10px; padding-top: 18px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#000000;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:18px;padding-right:10px;padding-bottom:10px;padding-left:10px;"> 
    			<div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #000000; font-family: 
    			Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			20px; line-height: 1.2; text-align: center; word-break: break-word; mso-line-height-alt: 24px; margin-top: 
    			0; margin-bottom: 0;"><span style="font-size: 20px; color: #2a272b;"><strong>""", cpu_temp, """°C</strong></span></p> 
    			</div> </div> <!--[if mso]></td></tr></table><![endif]--> <table border="0" cellpadding="0" 
    			cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; 
    			border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 
    			100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr 
    			style="vertical-align: top;" valign="top"> <td class="divider_inner" style="word-break: break-word; 
    			vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; 
    			padding-top: 42px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px;" valign="top"> <table 
    			align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" 
    			style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; 
    			mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid #BBBBBB; width: 100%;" valign="top" 
    			width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td style="word-break: break-word; 
    			vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <div align="center" 
    			class="img-container center autowidth" style="padding-right: 0px;padding-left: 0px;"> <!--[if mso]><table 
    			width="100%" cellpadding="0" cellspacing="0" border="0"><tr style="line-height:0px"><td 
    			style="padding-right: 0px;padding-left: 0px;" align="center"><![endif]--><img align="center" alt="I&#39;m 
    			an image" border="0" class="center autowidth" 
    			src="./imported-from-beefreeio_files/45220c14-891d-4532-acd3-6cbb3ca13e5e.png" style="text-decoration: 
    			none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; max-width: 100px; display: 
    			block;" title="I&#39;m an image" width="100"> <!--[if mso]></td></tr></table><![endif]--> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; 
    			padding-left: 10px; padding-top: 18px; padding-bottom: 10px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#555555;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.2;padding-top:18px;padding-right:10px;padding-bottom:10px;padding-left:10px;"> 
    			<div class="txtTinyMce-wrapper" style="line-height: 1.2; font-size: 12px; color: #555555; font-family: 
    			Helvetica Neue, Helvetica, Arial, sans-serif; mso-line-height-alt: 14px;"> <p style="margin: 0; font-size: 
    			20px; line-height: 1.2; text-align: center; word-break: break-word; mso-line-height-alt: 24px; margin-top: 
    			0; margin-bottom: 0;"><span style="font-size: 20px; color: #2a272b;"><strong>""", os.popen(
        cpu_usage).read(), """</strong></span></p> 
    			</div> </div> <!--[if mso]></td></tr></table><![endif]--> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![
    			endif]--> </div> </div> <!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(
    			IE)]></td></tr></table></td></tr></table><![endif]--> </div> </div> </div> <div 
    			style="background-color:transparent;"> <div class="block-grid" style="min-width: 320px; max-width: 640px; 
    			overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; 
    			background-color: transparent;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:transparent;background-image:url(
    			&#39;images/guides-bg.png&#39;);background-position:top left;background-repeat:repeat"> <!--[if (mso)|(
    			IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" 
    			style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" 
    			border="0" style="width:640px"><tr class="layout-full-width" style="background-color:transparent"><![
    			endif]--> <!--[if (mso)|(IE)]><td align="center" width="640" 
    			style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]--> <div class="col num12" 
    			style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 
    			0px;"> <!--<![endif]--> <table border="0" cellpadding="0" cellspacing="0" class="divider" 
    			role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: 
    			collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; 
    			-webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr style="vertical-align: top;" 
    			valign="top"> <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 
    			100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 30px; padding-right: 10px; 
    			padding-bottom: 25px; padding-left: 10px;" valign="top"> <table align="center" border="0" cellpadding="0" 
    			cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: 
    			top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; 
    			border-top: 0px solid #BBBBBB; width: 100%;" valign="top" width="100%"> <tbody> <tr style="vertical-align: 
    			top;" valign="top"> <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; 
    			-webkit-text-size-adjust: 100%;" valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> 
    			</tbody> </table> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> </div> <!--[if (mso)|(
    			IE)]></td></tr></table><![endif]--> <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--> 
    			</div> </div> </div> <div style="background-color:transparent;"> <div class="block-grid three-up" 
    			style="min-width: 320px; max-width: 640px; overflow-wrap: break-word; word-wrap: break-word; word-break: 
    			break-word; Margin: 0 auto; background-color: #ffffff;"> <div style="border-collapse: collapse;display: 
    			table;width: 100%;background-color:#ffffff;"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table 
    			cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:#ffffff"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="213" 
    			style="background-color:#ffffff;width:213px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 48px; padding-top:33px; padding-bottom:0px;"><![endif]--> <div class="col num4" 
    			style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 212px; width: 213px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:33px; padding-bottom:0px; padding-right: 0px; 
    			padding-left: 48px;"> <!--<![endif]--> <div align="left" class="img-container left autowidth" 
    			style="padding-right: 0px;padding-left: 0px;"> <!--[if mso]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0"><tr style="line-height:0px"><td style="padding-right: 0px;padding-left: 0px;" 
    			align="left"><![endif]--><a href="https://github.com/FLAFLALEBG/Ultimate_Auto_Check_Services" 
    			style="outline:none" tabindex="-1" target="_blank"><img alt="I&#39;m an image" border="0" class="left 
    			autowidth" src="./imported-from-beefreeio_files/687e14e5-5035-4692-9558-1a8b02a8a873.png" 
    			style="text-decoration: none; -ms-interpolation-mode: bicubic; height: auto; border: 0; width: 100%; 
    			max-width: 34px; display: block;" title="I&#39;m an image" width="34"></a> <!--[if 
    			mso]></td></tr></table><![endif]--> </div> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> 
    			</div> <!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(IE)]></td><td align="center" 
    			width="213" style="background-color:#ffffff;width:213px; border-top: 0px solid transparent; border-left: 
    			0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]--> <div class="col num4" 
    			style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 212px; width: 213px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 
    			0px;"> <!--<![endif]--> <div></div> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> </div> 
    			<!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(IE)]></td><td align="center" width="213" 
    			style="background-color:#ffffff;width:213px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 48px; padding-top:5px; padding-bottom:5px;"><![endif]--> <div class="col num4" 
    			style="display: table-cell; vertical-align: top; max-width: 320px; min-width: 212px; width: 213px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 
    			48px;"> <!--<![endif]--> <div class="mobile_hide"> <table border="0" cellpadding="0" cellspacing="0" 
    			class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; 
    			border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; 
    			-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr 
    			style="vertical-align: top;" valign="top"> <td class="divider_inner" style="word-break: break-word; 
    			vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; 
    			padding-top: 30px; padding-right: 10px; padding-bottom: 0px; padding-left: 10px;" valign="top"> <table 
    			align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" 
    			style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; 
    			mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid #BBBBBB; width: 100%;" valign="top" 
    			width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td style="word-break: break-word; 
    			vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> <!--[if 
    			mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 48px; 
    			padding-left: 0px; padding-top: 0px; padding-bottom: 28px; font-family: Arial, sans-serif"><![endif]--> 
    			<div style="color:#555555;font-family:Helvetica Neue, Helvetica, Arial, 
    			sans-serif;line-height:1.5;padding-top:0px;padding-right:48px;padding-bottom:28px;padding-left:0px;"> <div 
    			class="txtTinyMce-wrapper" style="line-height: 1.5; font-size: 12px; font-family: Helvetica Neue, 
    			Helvetica, Arial, sans-serif; color: #555555; mso-line-height-alt: 18px;"> <p style="margin: 0; font-size: 
    			14px; line-height: 1.5; word-break: break-word; text-align: left; font-family: Helvetica Neue, Helvetica, 
    			Arial, sans-serif; mso-line-height-alt: 21px; margin-top: 0; margin-bottom: 0;">Copyright © 2021</p> 
    			</div> </div> <!--[if mso]></td></tr></table><![endif]--> <!--[if (!mso)&(!IE)]><!--> </div> <!--<![
    			endif]--> </div> </div> <!--[if (mso)|(IE)]></td></tr></table><![endif]--> <!--[if (mso)|(
    			IE)]></td></tr></table></td></tr></table><![endif]--> </div> </div> </div> <div 
    			style="background-color:transparent;"> <div class="block-grid" style="min-width: 320px; max-width: 640px; 
    			overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; 
    			background-color: transparent;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:transparent;"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table 
    			cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:transparent"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="640" 
    			style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]--> <div class="col num12" 
    			style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> <div style="border-top:0px 
    			solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; 
    			border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 
    			0px;"> <!--<![endif]--> <div class="mobile_hide"> <table border="0" cellpadding="0" cellspacing="0" 
    			class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; 
    			border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; 
    			-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%"> <tbody> <tr 
    			style="vertical-align: top;" valign="top"> <td class="divider_inner" style="word-break: break-word; 
    			vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; 
    			padding-top: 15px; padding-right: 10px; padding-bottom: 15px; padding-left: 10px;" valign="top"> <table 
    			align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" 
    			style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; 
    			mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid #BBBBBB; width: 100%;" valign="top" 
    			width="100%"> <tbody> <tr style="vertical-align: top;" valign="top"> <td style="word-break: break-word; 
    			vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" 
    			valign="top"><span></span></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> <!--[if (
    			!mso)&(!IE)]><!--> </div> <!--<![endif]--> </div> </div> <!--[if (mso)|(IE)]></td></tr></table><![
    			endif]--> <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]--> </div> </div> </div> <div 
    			style="background-color:transparent;"> <div class="block-grid" style="min-width: 320px; max-width: 640px; 
    			overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; Margin: 0 auto; 
    			background-color: transparent;"> <div style="border-collapse: collapse;display: table;width: 
    			100%;background-color:transparent;"> <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" 
    			cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table 
    			cellpadding="0" cellspacing="0" border="0" style="width:640px"><tr class="layout-full-width" 
    			style="background-color:transparent"><![endif]--> <!--[if (mso)|(IE)]><td align="center" width="640" 
    			style="background-color:transparent;width:640px; border-top: 0px solid transparent; border-left: 0px solid 
    			transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" 
    			valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 
    			0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]--> <div class="col num12" 
    			style="min-width: 320px; max-width: 640px; display: table-cell; vertical-align: top; width: 640px;"> <div 
    			class="col_cont" style="width:100% !important;"> <!--[if (!mso)&(!IE)]><!--> 

    <!--<![endif]-->
    </div>
    </div>
    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
    </div>
    </div>
    </div>
    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
    </tr>
    </tbody>
    </table>
    <!--[if (IE)]></div><![endif]-->

    </body></html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, email_smtp_port, context=context) as server:
            server.login(sender_email, email_password)
            server.sendmail(
                sender_email, receiver_email, message.as_string().encode("utf8")
            )

            print("Successful sending mail")

    except:
        print(f"Sending error please check the sender's email ({sender_email}) and password or the receiver's "
              f"({receiver_email})")


def daemon():
    print("Starting...")
    restore(True)
    print("Started !")
    while running:
        time.sleep(30)
        print("New Verification")
        check_service(True)

    print("Stopped")


def run_daemon():
    threading.Thread(target=daemon()).start()


def init():
    print(f"{WARNING}This will guide you through the setup of the Ultimate Automatic Check Services.{ENDC}\n"
          f"{OKGREEN}If you wish to quit at any point, press Ctrl+C.{ENDC}")

    def config_email():
        print(f"{OKBLUE}Config email{ENDC}...")

        receiver_email = input(f"Enter your email address to which you will {BOLD}receive alerts{ENDC} : ")
        sender_email = input(f"Enter your sender address to which we will {BOLD}send alerts{ENDC} : ")
        email_password = input(f"Enter the {BOLD}password {ENDC}of the {BOLD}sender{ENDC}'s email address : ")
        smtp_server = input("List of the most famous SMTP server https://domar.com/smtp_pop3_server\n"
                            "Enter the address of your smtp server : ")
        try:
            email_smtp_port = int(
                input("Enter now the port of your SMTP server of preference the secure one (SSL)\nIt is more "
                      "commonly the port '465' : "))
        except:
            email_smtp_port = int(input(f"{FAIL}Please enter a numerical value{ENDC} : "))

        # Enregistrement des variables dans le fichier
        variables = [sender_email, email_password, receiver_email, smtp_server, email_smtp_port]
        backup_file = open(file_ini_email, "wb")
        pickle.dump(variables, backup_file)
        print("Saved !")
        time.sleep(1)

        def test_email():
            answer = input("Do you want to perform an email test ? [y/n]: ")

            if answer == "yes" or "y" or "Y":
                # Send mail
                try:
                    with smtplib.SMTP_SSL(smtp_server, email_smtp_port, context=ssl.create_default_context()) as server:
                        server.login(sender_email, email_password)

                        server.sendmail(sender_email, receiver_email,
                                        "Subject: You are done\n\nWell done you succeeded "
                                        "you will now receive alerts from your services on "
                                        "this email.")

                        print("Successful sending mail")

                        def checkup():
                            answer = input("Did you receive the email correctly ? [y/n]: ")
                            if answer == "yes" or "y" or "Y":
                                pass

                            elif answer == "no" or "n" or "N":
                                answer = input(
                                    f"Do you want to retry the test email [{OKCYAN}1{ENDC}] or do you want to "
                                    f"edit your email [{OKCYAN}2{ENDC}] ?: ")
                                if answer == "1":
                                    test_email()
                                elif answer == "2":
                                    init()
                                else:
                                    print("Error, please enter a correct value")

                            else:
                                print("Error, please enter a correct value")
                                checkup()

                        checkup()

                except:
                    print(
                        "Sending error please check the sender's email and password or the receiver's\nRelaunch of the "
                        "script"
                        f"{FAIL}Verify if less secure apps is been enable to sender address ({sender_email}) check here"
                        f": https://support.google.com/accounts/answer/6010255?hl=en {ENDC}")
                    init()

            elif answer == "no" or "n" or "N":
                pass

            else:
                print("Error, please enter a correct value")
                test_email()

        test_email()

    config_email()
    print(f"{WARNING}Successfully config email{ENDC}")

    print(f"Verification of the packages make sure that no task are active with the {BOLD}APT{ENDC} command ...")
    try:
        os.system("sudo apt install -y systemd sysstat")
        print("Verification and installation completed.")
    except:
        print("Installation failed retry another time with the command 'sudo apt install -y systemd'.")

    def config_service():
        print(f"{OKBLUE}Config service{ENDC} :")

        answer = input("Do you want to activate the autostart ? [y/n]: ")

        if answer == "yes" or "y" or "Y":
            print("")
            service = open(f"/lib/systemd/system/{service_name}.service", "w")
            service.write(f"[Unit]\n"
                          f"Description = Ultimate Auto Check Service\n"
                          f"[Service]\n"
                          f"ExecStart = /usr/local/bin/uacs -v start\n"
                          f"[Install]\n"
                          f"WantedBy = default.target\n")
            service.close()

        elif answer == "no" or "n" or "N":
            pass

        else:
            print("Error, please enter a correct value")
            config_service()

        def start_service():
            answer = input("Do you want to start the service now ? [y/n]: ")
            if answer == "yes" or "y" or "Y":
                commande = ["sudo systemctl daemon-reload", f"sudo systemctl enable {service_name}"]
                for i in range(len(commande)):
                    print(commande[i])
                    os.system(commande[i])

            elif answer == "no" or "n" or "N":
                pass

            else:
                print("Error, please enter a correct value")
                start_service()

        start_service()

        print("Configuration successful, add new service with : uacs -a 'service.service'")
        exit()

    config_service()


if __name__ == '__main__':
    main()
