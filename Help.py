def Help_command(extra = False,fileNumber = 0):
    String = ""
    if extra and fileNumber == 0:
        File = open("Helpp0.txt")
    
    elif extra and fileNumber == 1:
        File = open("Helpp1.txt")

    else:
        File = open("Help.txt")
    
    for line in File:
        String = String + line
    File.close
    return String
