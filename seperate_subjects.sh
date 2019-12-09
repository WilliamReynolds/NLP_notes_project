#!/bin/bash

# checks if file exists and that not zero size.
if [ -z "$1" ] || [ ! -e "$1" ]; then
    echo -e "\nNeed file input for files to work on"
    exit
fi


#set lines for loop through input file
lineNumber=1
totalLines=$(cat "$1" | wc -l)

#make original patient counter
patientNumber=0

until [ "$lineNumber" -gt "$totalLines" ]; do

    #get fileName and first line
    fileName=$(sed -n "$lineNumber"p "$1")
    if [ -e "$fileName" ]; then 
        firstLine=$(head "$fileName" -n 1)
        firstLineLength=$(echo "$firstLine" | wc -c)  
        echo "File Name: $fileName, Line number: $lineNumber"
    else
        echo -e "Missing File Name: $fileName, Line number: $lineNumber"
        echo -e "Moving onto next file.\n"
        let lineNumber++
        continue 
    fi

    # just so it doesn't run wild, check after every 100 iterations. 
    if [ $(( "$lineNumber" % 100 )) -eq 0 ]; then
        echo -e "Currently at linenumber "$lineNumber""
        echo -e "Press enter to continue."
        read
    fi

    # only goes through files with correct header info. 
    if [ "$firstLineLength" -gt 50 ]; then

        #define variabless
        rID=$(echo "$firstLine" | awk -F "|" '{print $2}' | sed 's/ *$* //g')
        medipac=$(echo "$firstLine" | awk -F "|" '{print $3}' | sed 's/ *$* //g')
        entryDate=$(echo "$firstLine" | awk -F "|" '{print $4}' | sed 's/ *$* //g')
        eventDate=$(echo "$firstLine" | awk -F "|" '{print $5}' | sed 's/ *$* //g')
        hospitalID=$(echo "$firstLine" | awk -F "|" '{print $6}' | sed 's/ *$* //g')
        reportSubtype=$(echo "$firstLine" | awk -F "|" '{print $7}' | sed 's/ *$* //g')
        noteStatus=$(echo "$firstLine" | awk -F "|" '{print $8}' | sed 's/ *$* //g')

        if [ -d "$medipac" ]; then
            mv "$fileName" ./"$medipac"/
            echo -e "Folder present, moving file.\n"
        else
            mkdir "$medipac"
            mv "$fileName" ./"$medipac"/
            echo -e "Folder not created. Creating folder and moving file.\n"
            let patientNumber++
        fi

    fi
    

    #read

    #increment line number
    let lineNumber++
done

echo -e "\n\tThere are "$patientNumber" distinct patients.\n"

