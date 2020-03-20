string_A = 'toSend_kanji[]'
full_String = "Kanji for ' + fdate + '\n\n' +"

j=0
while j <= 10 :
    full_String + f'toSend_kanji[{j}]'
    j+=1
    
print(full_String)