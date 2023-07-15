import schedule
import time
import random
import datetime
import subprocess
import threading

def focus_clock(total_minutes, commit_interval):
    print("专注模式开始")
    end_time = time.time() + (total_minutes * 60)
    
    while time.time() < end_time:
        # 生成一个随机的提交日期
        commit_date = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365))

        # 使用 Git 命令创建一个空的提交
        subprocess.call(f'git commit --allow-empty --date="{commit_date}" -m "Keep GitHub Contribution"', shell=True)
        
        remaining_minutes = int((end_time - time.time()) / 60)  # 计算剩余分钟数
        
        # 显示剩余时间
        print(f"剩余时间: {remaining_minutes} 分钟", end="\r")
        time.sleep(commit_interval * 60)  # 暂停指定的提交间隔时间
    
    print("专注模式结束")

def run_focus_clock():
    # 设置总共专注时间为60分钟，每10分钟提交一次
    focus_clock(60, 10)

def schedule_task():
    # 在每天的特定时间段运行代码
    schedule.every().day.at("09:30").do(run_focus_clock)
    schedule.every().day.at("14:00").do(run_focus_clock)
    schedule.every().day.at("19:00").do(run_focus_clock)

    # 运行定时任务
    while True:
        schedule.run_pending()
        time.sleep(1)

# 启动定时任务线程
task_thread = threading.Thread(target=schedule_task)
task_thread.start()
