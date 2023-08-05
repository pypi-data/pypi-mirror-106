import time

loop = 99999999999999999 * 99999999999999999

def axy_loop(action):
    for num in range(loop):
        print(action)

def axy_loop_sleep(sleeptime_secs, action):
    for num in range(loop):
        print(action)
        time.sleep(sleeptime_secs)

def axy_loop_sleep_fps(fps, action):
    fps_calc = 1 / fps
    for num in range(loop):
        print(action)
        time.sleep(fps_calc)

def axy_loop_help():
    commands_list = "Avaible commands in axy loop module:\naxy_loop(action) - infinite for loop with actions like regular for loop\naxy_loop_sleep(sleep_time_in_seconds, action - infinite for loop with actions like in regular for loop and delay in seconds between repeating the action/s again\naxy_loop_sleep_fps(fps_amount, action) - infinite for loop with actions like in regular for loop and fps cap between actions, wil repeat the action/s as much in a second as you set the fps\n\nconsider checking out:\nhttp://axy-youtube.tk\nhttp://axysteam.tk\nhttps://dsc.gg/axy"
    print(commands_list)