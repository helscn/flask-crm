#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from flask_restful import reqparse

# Scheduler 任务相关请求参数
argParser = reqparse.RequestParser()

# 任务ID，此为任务对象的唯一标识，可以省略
argParser.add_argument('id', type=str)

# 任务名称
argParser.add_argument('name', type=str)

# 任务调用模块路径，格式按照 Python 模块格式使用 . 分隔文件夹，示例： folder.pyfile:func
# 任务执行文件必须放在 settings.py 配置文件中的 SCHEDULER_JOBS_PATH 路径中（不可指定外部路径）
# 程序会自动在路径前添加 SCHEDULER_JOBS_PATH 前缀
argParser.add_argument('func', type=str)

# 任务函数调用时传入的位置参数
argParser.add_argument('args',  type=list, location='json')

# 任务函数调用时传入的命名参数
argParser.add_argument('kwargs', type=dict, location='json')

# 计划任务开始时间
argParser.add_argument('start_date', type=str)

# 计划任务结束时间
argParser.add_argument('end_date', type=str)

# 判断任务是否过期的允许误差，单位：秒，当前时间与计划时间差值小于此值仍会按计划执行
argParser.add_argument('misfire_grace_time', type=int, default=1)

# 当一个任务出现过多次过期时，下次执行时否合并过期的任务并只执行一次
argParser.add_argument('coalesce', type=bool, default=True)

# 相同任务最多可同时运行的实例数量，超过此设置的任务实例不会执行
argParser.add_argument('max_instances', type=int, default=1)

# 触发器类别，内置有 date、interval、cron 三种触发器
argParser.add_argument('trigger', type=str)

# 计划任务时间的参数设置数组，作为 scheduler.add_job 的传入参数，不同触发器的字段设置不同：
# 1. date 触发器：
#   - run_date
# 2. interval 触发器：
#   - weeks
#   - days
#   - hours
#   - minutes
#   - seconds
# 3. cron 触发器：
#   - year
#   - month
#   - day
#   - week
#   - day_if_week
#   - hour
#   - minute
#   - second
argParser.add_argument('fields', type=dict, location='json')

# 设置任务时间的时区信息，现代浏览器可以通过 Intl.DateTimeFormat().resolvedOptions().timeZone 获取
argParser.add_argument('timezone', type=str, default=None)


######################################################################


# 请求任务日志的分页参数
logParser = reqparse.RequestParser()

# 当前页面
logParser.add_argument('page', type=int, default=1)

# 每页的记录数
logParser.add_argument('per_page', type=int, default=5)

# 需要排序的字段名称
logParser.add_argument('sort_by', type=str, default=None)

# 是否按降序排列
logParser.add_argument('descending', type=bool, default=False)

# 日志筛选的关键词字段
logParser.add_argument('filter', type=str, default=None)
