def draw_dinosaur(position):
    print(' ' * position + 'o-=')

def draw_obstacle(position):
    print(' ' * position + '|===|')

def main():
    dinosaur_position = 0
    score = 0
    obstacle_position = 40

    while True:
        clear_screen()

        draw_dinosaur(dinosaur_position)
        draw_obstacle(obstacle_position)

        if dinosaur_position == obstacle_position:
            print("Game Over!")
            break

        if keyboard.is_pressed('space'):
            if dinosaur_position == obstacle_position - 1:
                score += 1
            else:
                print("Jump too early! Game Over!")
                break

        time.sleep(0.1)

        dinosaur_position += 1
        obstacle_position -= 1

        if obstacle_position == 0:
            obstacle_position = 40

        print(f'Score: {score}')

if __name__ == "__main__":
    main()
