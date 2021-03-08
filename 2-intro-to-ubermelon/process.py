
log_file = open("um-server-01.txt")
# open file with data

def sales_reports(log_file):   #define function that takes in file

    for line in log_file:
        line = line.rstrip()   #for each line, remove extra whitespace
        day = line[0:3]     #day = first 3 chars of line
        if day == "Mon":    #if first 3 chars of line are "Mon", print line
            print(line)


sales_reports(log_file)       #call function 