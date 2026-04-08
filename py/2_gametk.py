import tkinter as tk
import random as rnd

asd = 0

def init_game():
    global player_x,player_y, player_size,player_speed
    global target_x,target_y, target_size, target_speed
    global money, start_game,over_game, direction,obstacles
    global bonusm_size,bonusm_x,bonusm_y,bonusm_speed,the_live,    the_life


    player_x = 300
    player_y = 400
    player_size = 30
    player_speed = 5

    target_size = 30
    target_x = rnd.randint(0,500)
    target_y = 0
    target_speed = 4

    bonusm_size = 50
    bonusm_x = rnd.randint(0,500)
    bonusm_y = -5000
    bonusm_speed = 6

    the_life = 3


    money = 0
    start_game = False
    over_game = False
    obstacles = []
    direction = "stop"

    for i in range(7):
        obstacles.append({
            'x': rnd.randint(0, 470),
            'y': rnd.randint(-100, -50),
            'width': rnd.randint(30, 80),
            'height': rnd.randint(20, 40),
            'speed': rnd.uniform(1, 3)
        })

# окно
root = tk.Tk()
root.title("вирус")
root.geometry("610x630")
root.resizable(False,False)

canvas = tk.Canvas(root,width=500,height=500,background="black")
canvas.pack(pady=1)
canvas.focus_set()

score = 0
b = tk.Label(root,text=f"счет: {score}")
b.pack(pady=8)

start_button = tk.Button(root, text="Начать игру", command=lambda: game_start())
start_button.pack(pady=10)

player_x, player_y = 0, 0
player_size = 30
target_x, target_y = 0, 0
target_size = 20
over_game = False
direction = "stop"
obstacles = []
start_game = False
player_speed = 5
the_life = 3

init_game()
# управление
def key_press(event):
    global direction
    if event.keysym.lower() == 'a':
        direction = "left"
    elif event.keysym.lower() == 'd':
        direction = "right"
    elif event.keysym.lower() == 'w':
        direction = "up"
    elif event.keysym.lower() == 's':
        direction = "down"

root.bind("<KeyPress>", key_press)

#новое
def check_life():
    global over_game
    if the_life <= 0:
        print("У вас больше нет жизней вы проиграли!!")
        over_game = True

def anti_life():
    global the_life
    the_life -= 1
    print(f"ТЫ врезался в препядствие твоя жизньи: {the_life}")
    akw.config(text=f"Hp: {the_life}", font=("Arial", 20))

akw = tk.Label(root,text=f"Hp: {the_life}",font=("Arial",20))

akw.pack(pady=5,padx=10)


# движение игрока
def move_moment():
    global player_x,player_y

    if direction == "left":
        player_x -= player_speed
    elif direction == "right":
        player_x += player_speed
    # границы окна
    if player_x < 0: player_x = 0
    if player_y < 0: player_y = 0
    if player_x > 500 - player_size: player_x = 500 - player_size
    if player_y > 500 - player_size: player_y = 500 - player_size

    canvas.coords(player,
                  player_x, player_y,
                  player_x + player_size,
                  player_y + player_size)

def obj_move():
    global over_game,anti_life
    for object in obstacles:
        object["y"] += object["speed"]
        canvas.coords(
            obstacles_dict[id(object)],
            object["x"], object["y"],
            object["x"] + object["width"],
            object["y"] + object["height"]
        )
    #если упала то обратно
        if object["y"] >= 500:
            object["y"] = -object["height"]
            object["x"] = rnd.randint(0, 500 - object["width"])

        player_left = player_x
        player_right = player_x + player_size
        player_top = player_y
        player_bottom = player_y + player_size
        if not (
                player_right < object["x"] or
                player_left > object["x"] + object["width"] or
                player_bottom < object["y"] or
                player_top > object["y"] + object["height"]
        ):
                anti_life()




# движение монеты
def mone1sy_move():
    global target_y, target_x, target_speed, mone1ta, score

    target_y += target_speed

    canvas.coords(
        mone1ta,
        target_x, target_y,
        target_x + target_size,
        target_y + target_size
    )

    # если упала то наверх
    if target_y > 500:
        target_y = -20
        target_x = rnd.randint(0,450)

    # координаты игрока
    player_left = player_x
    player_right = player_x + player_size
    player_top = player_y
    player_bottom = player_y + player_size

    # координаты монеты
    coin_left = target_x
    coin_right = target_x + target_size
    coin_top = target_y
    coin_bottom = target_y + target_size

    # столкновение
    if not (
        player_right < coin_left or
        player_left > coin_right or
        player_bottom < coin_top or
        player_top > coin_bottom
    ):
        score += 1
        b.config(text=f"счет: {score}")  # обновление счёта
        target_y = -20
        target_x = rnd.randint(0,450)
print(b)

#БОНУС МОНЕТА❤️❤️❤️❤️🥏🐽🐮😶‍🌫️😭
def bonusm_move():
    global bonusm_size,bonusm_x,bonusm_y,bonusm_speed,mone1ta8, score

    bonusm_y += bonusm_speed

    canvas.coords(
        mone1ta8,
        bonusm_x, bonusm_y,
        bonusm_x + bonusm_size,
        bonusm_y + bonusm_size
    )

    # если упала то наверх
    if bonusm_y > 500:
        bonusm_y = -20
        bonusm_x = rnd.randint(0,450)

    # координаты игрока
    player_left = player_x
    player_right = player_x + player_size
    player_top = player_y
    player_bottom = player_y + player_size

    # координаты монеты
    coin_left = bonusm_x
    coin_right = bonusm_x + target_size
    coin_top = bonusm_x
    coin_bottom = bonusm_y + target_size

    # столкновение
    if not (
        player_right < coin_left or
        player_left > coin_right or
        player_bottom < coin_top or
        player_top > coin_bottom
    ):
        score += 3
        b.config(text=f"счет: {score}")  # обновление счёта
        bonusm_y = -50
        bonusm_x = rnd.randint(0,450)
        bonusm_y = -999



def game_ovet():
    global start_game,over_game
    start_game = False
    #vb = tk.Label(canvas, text="GAME OVER", )
   # vb.pack(pady=1)
    canvas.create_text(250,250,text="GAME OVER",font=("tup",20),fill="red")


def lol_ez():
    global bonusm_move,bonusm_y
    if score == 7:
        bonusm_move()
        bonusm_y = -100



# игровой цикл
def game_loop():
    global start_game, over_game
    if over_game:
        game_ovet()

    if start_game and not over_game:
        move_moment()
        mone1sy_move()
        obj_move()
        lol_ez()
        bonusm_move()
        check_life()



        if score > 0 and score % 5 == 0:
            for obj in obstacles:
                obj["speed"] += 0.01
        root.after(30, game_loop)


# старт игры
def game_start():
    global start_game, over_game, player , mone1ta,obstacles_dict,bonusm_size,bonusm_x,bonusm_y,bonusm_speed,mone1ta8, score
    if not start_game:
        canvas.delete("all")
        init_game()

        player = canvas.create_rectangle(
            player_x, player_y,
            player_x + player_size,
            player_y + player_size,
            fill='blue'
        )

        mone1ta = canvas.create_oval(
            target_x, target_y,
            target_x + target_size,
            target_y + target_size,
            fill='green'
        )
        mone1ta8 = canvas.create_oval(
            bonusm_x, bonusm_y,
            bonusm_x + bonusm_size,
            bonusm_y + bonusm_size,
            fill='yellow'
        )
        # препидствие
        obstacles_dict = {}
        for object in obstacles:
            obj = canvas.create_rectangle(
                object["x"],
                object["y"],
                object["x"] + object["width"],
                object["y"] + object["height"],
                fill="red"
            )
            obstacles_dict[id(object)] = obj




        start_game = True
        over_game = False
        game_loop()

root.mainloop()