#opens the text log and assigns it to log_file
log_file = open("um-server-01.txt")

#create a function with a parameter of the log named log_file
def generate_sales_reports(log_file):
    #the for loop checks every line in the log
    for line in log_file:
        #.rstrip() will remove all white spaces at the end of the line
        line = line.rstrip()
        #day is asign to the first three characters for each line
        day = line[0:3]
        #checks for "monday" with the 3 characters
        if day == "Mon":
            #prints the line for monday only
            print(line)

#calls the function with an argument whic is the log
generate_sales_reports(log_file)
