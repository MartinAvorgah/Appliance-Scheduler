def newfriend():
    friends = ['Kofi', 'Ama', 'Yaw',]
    sidechicks = ['Yaa', 'Akosua', 'Emefa']

    today = input('did you get a friend or sidechick today?(f/s) ')
    if today == 'f':
            name = input("what's your new friend's name? ")
            name = name.strip().title()
            friends.append(name)
            print('your updated friends list is 🥁🥁')
            for friends in friends:
                print(friends)
            print('you have %i friends now' % len(friends))
    elif today =='s':
        new_sidechick = input("what's the new babe's name? ")
        new_sidechick = new_sidechick.strip().title()
        sidechicks.append(new_sidechick)
        print("you're a top gee, real player. this is your updated side chicks list 😂🤣")
        for sidechicks in sidechicks:
            print(sidechicks)
        print('you have %i side chicks' % len(sidechicks))
    else:
        print('get out of of your room and go and meet some people!')


newfriend()
