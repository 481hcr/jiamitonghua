import easygui
# 询问加密代码
word = easygui.enterbox("你想加密什么字母？（仅支持英文）")
# 询问凯撒移位信息
moveNumbers = int(easygui.enterbox("移动几位？"))
# 加密信息
numbersList = []
for i in word:
    numbersList.append(ord(i) + moveNumbers)
#转十六进制
hexNumbersList = []
for i in numbersList:
    hexNumbersList.append(hex(i))
# 处理信息
endStr = ""
for i in hexNumbersList:
    endStr += i+" "
# 创建文件
fileName = easygui.enterbox("请问要生成的文件名是什么？")
_print = open(fileName+".txt","w+")
_print.write(endStr)
easygui.msgbox("已生成名为"+_print.name+"的文件")
_print.close()