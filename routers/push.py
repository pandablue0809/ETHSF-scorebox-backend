'''Use threads to execute push-polling via PUSH'''
from requ.polling import *
from multiprocessing import Process


if __name__=='__main__':
    p1 = Process(target = run_score_update)
    p1.start()
    p2 = Process(target = run_leaderboard, args=('0x691C7c07A1B1698c56340d386d8cC7A823f6e2D8',))
    p2.start()