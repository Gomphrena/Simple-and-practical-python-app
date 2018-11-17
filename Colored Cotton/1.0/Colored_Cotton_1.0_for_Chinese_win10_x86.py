import os
import time

#coding=utf-8

long_s_string = "\n=======================================\n\n\n"
long_z_string = "***************************************\n\n\n"

def count_down():
    print(long_z_string, "将在六秒钟后将自动刷新：", "6秒", end="", flush=True)
    time.sleep(0.6)
    print("\b\b\b5秒", end="", flush=True)
    time.sleep(0.8)
    print("\b\b\b4秒", end="", flush=True)
    time.sleep(0.8)
    print("\b\b\b3秒", end="", flush=True)
    time.sleep(0.8)
    print("\b\b\b2秒", end="", flush=True)
    time.sleep(0.9)
    print("\b\b\b1秒", flush=False)
    time.sleep(1)

while True:
    os.system("CLS")
    os.system("color FA")
    print("\t\t关于颜色的英文单词简易查询系统\n\n\n\n")
    print("请从以下中输入序号进行选择出您要翻译成的中文颜色：\n\n")
    print("1.白色  2.黑色  3.红色  4.黄色  5.绿色  6.蓝色 7.紫色  8.褐色  9.金黄色  10.粉红色  11.灰色\n\n")
    Chinese_color = input("您的选择是：")

    if Chinese_color == "1":
        print(long_s_string, " · 中文：白色\n\n · 英文：white\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "2":
        print(long_s_string, " · 中文：黑色\n\n · 英文：black\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "3":
        print(long_s_string, " · 中文：红色\n\n · 英文：red\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "4":
        print(long_s_string, " · 中文：黄色\n\n · 英文：yellow\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "5":
        print(long_s_string, " · 中文：绿色\n\n · 英文：green\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "6":
        print(long_s_string, " · 中文：蓝色\n\n · 英文：blue\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "7":
        print(long_s_string, " · 中文：紫色\n\n · 英文：purple\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "8":
        print(long_s_string, " · 中文：褐色\n\n · 英文：brown\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "9":
        print(long_s_string, " · 中文：金黄色\n\n · 英文：golden\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "10":
        print(long_s_string, " · 中文：粉红色\n\n · 英文：pink\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color == "11":
        print(long_s_string, " · 中文：灰色\n\n · 英文：gray\n\n", sep="")
        del Chinese_color
        count_down()
        continue

    if Chinese_color != "1" or Chinese_color != "2" or Chinese_color != "3" or Chinese_color != "4" or Chinese_color != "5" or Chinese_color != "6" or Chinese_color != "7" or Chinese_color != "8" or Chinese_color != "9" or Chinese_color != "10" or Chinese_color != "11":
        print(f"\n\n\033[1;31m{long_z_string}输入内容异常！请重新输入相关内容\n\n\n{long_z_string}\033[0m")
        del Chinese_color
        time.sleep(2.8)