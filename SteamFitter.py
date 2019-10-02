# SteamFitter
# @Bryspeelm
# Description: 
# Goal: Identify extra pipes and what line they occur in a .tsv file.
# Ver 1.0

# Main Method
def main():
    numOfPipes = 23 # !!do not change unless number fields change!!
    lineNum = 1 # start at one to take header into account

#Find pipes out of range in community_users.tsv file
    try:
        #Open file
        infile = open('community_users.tsv', 'r')
        #read lines and count number of pipes
        for line in infile:
            count = 0 # reset pipe counter for each new line
            for char in line:
                if char == '|':
                    count+=1
            #print line that has too many pipes along with the number of pipes
            if count > numOfPipes:
                print(count - numOfPipes), " extra pipes @ line ", lineNum 
                within(line) # call within function
            lineNum+=1 # move line counter to next line
    except IOError:
        print("Cannot find file")

# find index of pipe inside quotes
def within(ln):
    charNum = 0; #var that keeps track of char place
    flag =0;
    qtCt = 0; # track quote count
    #Look for quotes in line and switch flag on/off
    for char in ln:
        charNum+=1; #incriment char place
        # Alternate Flag
        if char == '\"':
            qtCt+=1
            if flag == 0:
                flag = 1
            else: 
                flag = 0
        if char == '|' and flag == 1 and qtCt % 2 != 0:
            print("Pipe in quotes at char #: ", charNum)
#call main function
main()