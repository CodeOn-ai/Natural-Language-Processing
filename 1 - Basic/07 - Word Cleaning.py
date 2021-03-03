

with open("Resources/emotions.txt", "r") as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'","").strip()
        word, emotion = clear_line.split(":")
        
        print(word)
        print(emotion)
        