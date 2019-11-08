import qqzhpt
import sys
if __name__ == '__main__' :
    if len(sys.argv) != 1:
        url = sys.argv[1]
    else:
        url = input("请输入套图首页URL\n")
    mission = qqzhpt.meitu(url)
    mission.run()
