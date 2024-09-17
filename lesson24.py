message = input("Type your message: ")
separate_words = message.split(' ')
print(separate_words)
emoji = {
	":)" : "",
	":(" : ""
}
output = ""
for word in separate_words:
	output += emoji.get(word, word) + " "
print(output)
