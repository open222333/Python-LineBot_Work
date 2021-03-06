from RoleCreate import *
from RoleInfo import *
from FightAction import *


knightskill = [
    {'技能名': '重力斬', '技能類型': '傷害', '技能數值': 2,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 5, '技能觸發機率': 20},
    {'技能名': '神龍斬', '技能類型': '傷害', '技能數值': 4,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 10, '技能觸發機率': 22},
    {'技能名': '突擊刺', '技能類型': '傷害', '技能數值': 8,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 15, '技能觸發機率': 25},
    {'技能名': '地裂斬', '技能類型': '傷害', '技能數值': 12,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 20, '技能觸發機率': 28},
    {'技能名': '體能強化', '技能類型': '傷害', '技能數值': 24,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 25, '技能觸發機率': 18},
    {'技能名': '火龍巨斬', '技能類型': '傷害', '技能數值': 57,
     '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 30, '技能觸發機率': 9}
]

megaskill = [
    {'技能名': '地獄火', '技能類型': '傷害', '技能數值': 2,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 8, '技能觸發機率': 20},
    {'技能名': '隕石術', '技能類型': '傷害', '技能數值': 4,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 16, '技能觸發機率': 22},
    {'技能名': '黑龍波', '技能類型': '傷害', '技能數值': 8,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 22, '技能觸發機率': 25},
    {'技能名': '賽爾波之光', '技能類型': '傷害', '技能數值': 30,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 20, '技能觸發機率': 28},
    {'技能名': '雷神之電', '技能類型': '傷害', '技能數值': 24,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 62, '技能觸發機率': 18},
    {'技能名': '水龍冰凍', '技能類型': '傷害', '技能數值': 57,
        '技能數值類型': '數值', '輔助作用屬性': '', '技能消耗MP': 98, '技能觸發機率': 9}
]

# 創造角色
testA_AP = CreateRole("測試A", "騎士").createRole()
testB_AP = CreateRole("測試B", "法師").createRole()

# 戰鬥前取得角色資訊
# testA_Info = RoleInfo(testA_AP).getRoleInfo()
# testB_Info = RoleInfo(testB_AP).getRoleInfo()

# 進入戰鬥
text = FightMessage()
message = text.getAttackMessage(testA_AP, knightskill, testB_AP)
print(message)

# text = FightRole(testA_AP)
# print(text.role["角色名"])

# while True:
#     if text.role["HP"] < 0:
#         text.role["HP"] = 0
#         print(text.role["HP"])
#         break
#     print(text.role["HP"])
#     text.role["HP"] -= 300
