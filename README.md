# SQL-BeGone
A program to eliminate the need to make sql statements in favor of creating sentences for AI to convert into SQL queries.
This program will take your input and turn it into a sql statement. The inputs and outputs can be any format of basic english or SQL operations. If you wish for output on a specific engine, the bot will be able to do that for you, as long as there is publicly available information on it up until September of 2021.
Each message stream can have up to 4096 tokens each, with the token count being used increasing in every interaction within the same message stream. If an interaction requires over 4096 tokens, it will not go through. A token counter is provided to help avoid this issue.

USAGE:
Type your input. After your input, pressing "Enter" twice will submit your message to the chat bot, so it can respond with an answer.
Type "done" on any reply of the chatbot, or at the beginning of the program, to terminate the running program.