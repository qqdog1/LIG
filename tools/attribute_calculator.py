user = {1: {'hp': 10, 'atk': 3, 'def': 0, 'spd': 10},
        2: {'hp': 19, 'atk': 6, 'def': 0, 'spd': 10},
        3: {'hp': 31, 'atk': 10, 'def': 0, 'spd': 10},
        4: {'hp': 52, 'atk': 17, 'def': 1, 'spd': 10},
        5: {'hp': 76, 'atk': 25, 'def': 1, 'spd': 10},
        6: {'hp': 112, 'atk': 37, 'def': 2, 'spd': 10},
        7: {'hp': 157, 'atk': 52, 'def': 2, 'spd': 10},
        8: {'hp': 205, 'atk': 68, 'def': 2, 'spd': 10},
        9: {'hp': 265, 'atk': 88, 'def': 3, 'spd': 10},
        10: {'hp': 325, 'atk': 108, 'def': 4, 'spd': 10},
        11: {'hp': 385, 'atk': 128, 'def': 4, 'spd': 10},
        12: {'hp': 445, 'atk': 148, 'def': 5, 'spd': 10},
        13: {'hp': 517, 'atk': 172, 'def': 5, 'spd': 10},
        14: {'hp': 592, 'atk': 197, 'def': 6, 'spd': 10},
        15: {'hp': 682, 'atk': 227, 'def': 6, 'spd': 10},
        16: {'hp': 784, 'atk': 261, 'def': 7, 'spd': 10},
        17: {'hp': 910, 'atk': 303, 'def': 8, 'spd': 10},
        18: {'hp': 1036, 'atk': 345, 'def': 8, 'spd': 10},
        19: {'hp': 1180, 'atk': 393, 'def': 9, 'spd': 10},
        20: {'hp': 1312, 'atk': 437, 'def': 10, 'spd': 10}}

boss = {1: {'hp': 10, 'atk': 2, 'def': 0, 'spd': 10},
        2: {'hp': 35, 'atk': 3, 'def': 1, 'spd': 10},
        3: {'hp': 50, 'atk': 6, 'def': 1, 'spd': 10},
        4: {'hp': 112, 'atk': 9, 'def': 1, 'spd': 10},
        5: {'hp': 168, 'atk': 12, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        7: {'hp': 350, 'atk': 28, 'def': 2, 'spd': 10},
        8: {'hp': 462, 'atk': 36, 'def': 2, 'spd': 10},
        9: {'hp': 602, 'atk': 47, 'def': 2, 'spd': 10},
        10: {'hp': 749, 'atk': 50, 'def': 1, 'spd': 11},
        11: {'hp': 882, 'atk': 68, 'def': 2, 'spd': 10},

        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10},
        6: {'hp': 252, 'atk': 20, 'def': 1, 'spd': 10}}

speed_bar = 100
user_lv = 11
boss_lv = 11


def print_fighting_process():
    user_data = user[user_lv]
    boss_data = boss[boss_lv]

    user_hp = user_data['hp']
    boss_hp = boss_data['hp']

    user_run = 0
    boss_run = 0

    while True:
        print('---------------------------------------------------')
        print('user hp: ' + str(user_hp) + ' ,boss hp: ' + str(boss_hp))
        user_run += user_data['spd']
        boss_run += boss_data['spd']

        if user_run >= speed_bar:
            user_run -= speed_bar
            boss_hp -= user_data['atk'] - boss_data['def']
            if boss_hp <= 0:
                print('win')
                break

        if boss_run >= speed_bar:
            boss_run -= speed_bar
            user_hp -= boss_data['atk'] - user_data['def']
            if user_hp <= 0:
                print('lose')
                break


if __name__ == '__main__':
    print_fighting_process()
