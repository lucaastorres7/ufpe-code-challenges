name = input()
music_quantity = int(input())

for i in range(0,music_quantity):
    song = input()
    streams = int(input())
    if(i == 0):
        least_listened = song
        most_streamed = 0
        least_streamed = streams
    
    if(streams > most_streamed):
        most_streamed = streams
        most_listened = song
    if(streams < least_streamed):
        least_streamed = streams
        least_listened = song

if(music_quantity == 0):
    print(f"{name} é team Taylor e não ouviu Kanye West")
elif(music_quantity == 1):
    print(f"A única música que {name} ouviu foi {song} com {streams} streams")
elif(music_quantity > 1):
    if(least_streamed != most_streamed):
        print(f"A música que {name} mais ouviu foi {most_listened} com {most_streamed} streams")
        print(f"A música que {name} menos ouviu foi {least_listened} com {least_streamed} streams")
    else:
        print(f"A música que {name} mais ouviu foi {most_listened} com {most_streamed} streams")