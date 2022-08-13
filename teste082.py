for i, music_queue in enumerate(list_queue_music):
        root.update()
        print(i, music_queue)
        if music == 'nothing':
            pygame.mixer.music.load(music_queue)
            pygame.mixer.music.play()
            label_music_playing['text'] = basename(music_queue)
            if i == c:
                c += 1
                while True:
                    root.update()
                    state_music_queue = pygame.mixer.music.get_busy()
                    if state_music_queue == False:
                        break        
        else:
            continue