from LabelPrinter import *
import easygui
import time

#Connection to the printer
host = "192.168.1.103"
port = 9100
label_printer=LabelPrinter(host,port)

#Variables
label_dict = {
    "$reagent_type" : "",
    "$full_batch_name" : "",
    "$label_number" : "0"
}

#Messages
query_dict = {
    "$reagent_type" : "Type of reagent",
    "$full_batch_name" : "Full batch name",
    "$label_number" : "Number of labels to print"
}


#Get infos from the user, by printing out desired Messages
for key in label_dict:
    label_dict[key]=easygui.enterbox(msg=query_dict[key])
    #if the user has cancelled, exit
    if label_dict[key]==None:
        exit()


for label_number in range(int(label_dict["$label_number"])):
    label_file = open('reagent_label_template.cmd', 'r')
    label_lines = label_file.readlines()

    for line in label_lines:

        qr_content=label_dict["$full_batch_name"] + "_bottle" + str(label_number+1)

        line = line.replace("$full_batch_name",label_dict["$full_batch_name"])
        line = line.replace("$reagent_type",label_dict["$reagent_type"])
        line = line.replace("$bottle_number",str(label_number+1))
        line = line.replace("$qr_content", qr_content)
        line = line.replace("$qr_length", str(len(qr_content)+1))

        r = label_printer.send(line, 0)
        print(line)

    time.sleep(0.5)
