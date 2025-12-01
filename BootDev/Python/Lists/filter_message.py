def filter_messages(message):

    cleanList = []
    dangList = []

    for testMessage in message:
        
        words = testMessage.split()

        badWords = []
        goodWords = []

        for word in words:

            if word == "dang":
               badWords.append(word)

            else:
                goodWords.append(word)
                goodSentence = " ".join(goodWords)

        cleanList.append(goodSentence)
        dangList.append(len(badWords))

    return cleanList, dangList

testMessages = ["dang it bobby!", "look at it go"]

filter_messages(testMessages)