END_OF_INPUT_STR = "Statistics"
MAX_RECEIVED_SENT_MESSAGES_PER_PERSON = int(input())
 
recordLines = {}
 
def handleIteration(inputArray):
    COMMANDS = {
        "ADD": "Add", 
        "MESSAGE": "Message", 
        "EMPTY": "Empty"
    }
 
    if inputArray[0] == COMMANDS["ADD"] and inputArray[1] not in recordLines:
        recordLines[inputArray[1]] = [int(inputArray[2]), int(inputArray[3])]
 
    if inputArray[0] == COMMANDS["MESSAGE"] and inputArray[1] in recordLines and inputArray[2] in recordLines:
        if sum(recordLines[inputArray[1]]) + 1 >= MAX_RECEIVED_SENT_MESSAGES_PER_PERSON:
            del recordLines[inputArray[1]]
            print(f'{inputArray[1]} reached the capacity!')
        else:
            recordLines[inputArray[1]][0] += 1
 
        if sum(recordLines[inputArray[2]]) + 1 >= MAX_RECEIVED_SENT_MESSAGES_PER_PERSON:
            del recordLines[inputArray[2]]
            print(f'{inputArray[2]} reached the capacity!')
        else:
            recordLines[inputArray[2]][1] += 1
 
    if inputArray[0] == COMMANDS["EMPTY"]:
        DELETE_ALL_OPTION = "All"
 
        if inputArray[1] == DELETE_ALL_OPTION:
            recordLines.clear()
        else:
            del recordLines[inputArray[1]]
 
 
while True:
    currentReadInput = input()
    
    if currentReadInput == END_OF_INPUT_STR:
        break
    
    currentInputArray = currentReadInput.split("=")
 
    handleIteration(currentInputArray)
 
 
print(f'Users count: {len(recordLines)}')
 
for name in recordLines:
    print(f'{name} - {sum(recordLines[name])}')
 