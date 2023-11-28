import google.generativeai as palm
import os
API_KEY="AIzaSyDGf9gyCmw3dKLzg49DIpIu-mMJN9AyGYQ"
palm.configure(api_key=API_KEY)

response =palm.chat(messages="Hi")
print(response.last)
reply =" "
l=[]

while True:
    reply=input("Your reply:")
    new_res="Give response in short points"+reply
    if reply.upper()=='Q':
        break
    response=response.reply(new_res)
    l.append(response.last)
    print(response.last)
print(len(l))
