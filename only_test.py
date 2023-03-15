# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:26:09 2023

@author: 22193
"""

from github import Github

# 使用个人访问令牌或用户名和密码进行认证
g = Github("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")
# 或者使用匿名认证
#g = Github()

# 根据仓库名称和所有者名称获取仓库对象
repo = g.get_repo("owner/repo")



















