import pygame


def toggle_to_fullscreen(device_size, flag):
    pygame.display.set_mode(device_size, flag)
    pygame.display.toggle_fullscreen()


def minimize_window(window_resolution, flag):
    pygame.display.toggle_fullscreen()
    pygame.display.set_mode(window_resolution, flag)


def main():
    pygame.init()
    pygame.display.set_caption("Crochet Pattern Maker")
    dt = 0
    clock = pygame.time.Clock()

    # referenced https://github.com/pygame-community/pygame-ce/issues/1221 to 
    # access, store, and use device screen dimensions
    get_device_size = pygame.display.Info()
    device_width = get_device_size.current_w
    device_height = get_device_size.current_h
    device_size = (device_width, device_height)
    window_resolution = (device_width//2, device_height//2)
    flag = pygame.SCALED
    screen = pygame.display.set_mode(window_resolution, flag)

    running = True
    f_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # referenced https://github.com/pygame-community/pygame-ce/issues/1221 
                # to fix windows resizing issue when toggling between the 
                # minimized window and fullscreen 
                elif event.key == pygame.K_f:
                    if f_count == 1:
                        minimize_window(window_resolution, flag)
                        f_count = 0
                    else:
                        toggle_to_fullscreen(device_size, flag)
                        f_count += 1            
        screen.fill('Black')
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()