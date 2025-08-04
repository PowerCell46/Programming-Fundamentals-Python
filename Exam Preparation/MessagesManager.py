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


#----------------------------------------------------#

class Command:
    def execute(self, data, recordLines, maxCapacity):
        raise NotImplementedError


class AddCommand(Command):
    def execute(self, data, recordLines, maxCapacity):
        name, sent, received = data[1], int(data[2]), int(data[3])

        if name not in recordLines:
            recordLines[name] = [sent, received]


class MessageCommand(Command):
    def execute(self, data, recordLines, maxCapacity):
        sender, receiver = data[1], data[2]

        if sender in recordLines and receiver in recordLines:
            CAPACITY_REACHED_MESSAGE = "{} reached the capacity!"

            if (sum(recordLines[sender]) + 1) >= maxCapacity:
                del recordLines[sender]
                print(CAPACITY_REACHED_MESSAGE.format(sender))
            else:
                recordLines[sender][0] += 1

            if (sum(recordLines[receiver]) + 1) >= maxCapacity:
                del recordLines[receiver]
                print(CAPACITY_REACHED_MESSAGE.format(receiver))
            else:
                recordLines[receiver][1] += 1


class EmptyCommand(Command):
    def execute(self, data, recordLines, maxCapacity):
        DELETE_ALL_OPTION = "All"

        if data[1] == DELETE_ALL_OPTION:
            recordLines.clear()
        else:
            del recordLines[data[1]]


commandMapper = {
    "Add": AddCommand(),
    "Message": MessageCommand(),
    "Empty": EmptyCommand()
}


END_OF_INPUT_STR = "Statistics"
MAX_RECEIVED_SENT_MESSAGES_PER_PERSON = int(input())

recordLines = {}

while True:
    currentReadInput = input()

    if currentReadInput == END_OF_INPUT_STR:
        break

    SPLIT_SYMBOL = "="
    currentInputArray = currentReadInput.split(SPLIT_SYMBOL)

    commandName = currentInputArray[0]
    commandExecutor = commandMapper.get(commandName)
    if commandExecutor:
        commandExecutor.execute(currentInputArray, recordLines, MAX_RECEIVED_SENT_MESSAGES_PER_PERSON)


print(f'Users count: {len(recordLines)}')

for name in recordLines:
    print(f'{name} - {sum(recordLines[name])}')

 
