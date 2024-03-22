from ast import Str
import os
from pickle import TRUE
import re
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import openpyxl
from tqdm import tqdm
import time
import random

# 存放搜索的关键字
global search
global PaperNum
class   MySpider:
    #TODO: (method)是否存在下一页Next_page
    def Next_page(self,web):
        try:
            WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'next'))
                )
            web.find_element(By.CLASS_NAME,'next')
            return True
        except:
            return False


    #TODO: (method)是否打开了子网页is_childpage
    def is_childpage(self,web):
        try:
            web.switch_to.window(web.window_handles[1])
            return True
        except:
            print("is_childpage报错")
            return False

    #TODO: (method)选择查询方式
    def Search_id(self,web,cc):
        count = 0
        strcls = 'search-option'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, strcls))
                )
                web.find_element(By.CLASS_NAME,strcls).click()
                print(cc+":===SUCCESS 点击查询方式成功===")
                break
            except:
                count += 1
                print(cc+":!!!EXCEPT 点击查询方式操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print(cc+":***EXCEPT 点击查询方式操作失败")
                    break
    
    #TODO: (method)选择分类号
    def U_Choose(self,web,cc):
        count = 0
        strnow = '/html/body/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[2]/li[9]'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print(cc+":===SUCCESS 选择中图分类号操作成功===")
                break
            except:
                count += 1
                print(cc+":!!!EXCEPT 选择中图分类号操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print(cc+":***EXCEPT 选择中图分类号操作失败")
                    break

    #TODO： 输入分类号
    def u_Class(self,web,str):
        count = 0
        inputcls = 'ivu-input'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, inputcls))
                )
                web.find_element(By.CLASS_NAME,inputcls).send_keys(str)
                print(str+":===SUCCESS 输入分类号:{}操作成功===".format(str))
                return True
            except:
                print(str+":!!!EXCEPT 输入分类号:{}操作失败，正在第{}次尝试。".format(str,count))
                count += 1
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print(str+":***EXCEPT 输入分类号{}操作失败。".format(str))
                    return False

    def Page_Papers(self,web):
        count = 0
        strnow = '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div/div'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 选择显示论文数量(Page_Papers)操作成功===")
                return True
            except:
                print("!!!EXCEPT 选择显示论文数量(Page_Papers)操作失败，正在第{}次尝试。".format(count))
                count += 1
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 选择显示论文数量(Page_Papers)操作失败。")
                    return False

    def Page_Papers_50(self,web):
        count = 0
        strnow = '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/div[2]/div/div/ul/li[3]'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 选择显示论文数量50(Page_Papers_50)操作成功===")
                return True
            except:
                print("!!!EXCEPT 选择显示论文数量50(Page_Papers_50)操作失败，正在第{}次尝试。".format(count))
                count += 1
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 选择显示论文数量50(Page_Papers_50)操作失败。")
                    return False

    def XueShu(self,web):
        count = 0
        strnow = '/html/body/div[3]/div[1]/div/ul[1]/li[1]/a'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 学术期刊(XueShu)操作成功===")
                return True
            except:
                print("!!!EXCEPT 学术期刊(XueShu)操作失败，正在第{}次尝试。".format(count))
                count += 1
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 学术期刊(XueShu)操作失败。")
                    return False

    #TODO: (method)点击文献分类Classification_click
    def Classification_click(self,web):
        count = 0
        strnow = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/a'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 点击文献分类(Classification_click)操作成功===")
                break
            except:
                count += 1
                print("!!!EXCEPT 点击文献分类(Classification_click)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 点击文献分类(Classification_click)操作失败")
                    break
            
    #TODO: (method)点击加号Plus_click
    def Plus_click(self,web):
        count = 0
        strnow = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[3]/div/i[1]'
        while True:
            try:
                WebDriverWait(web, 20).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click();
                # print("===SUCCESS 点击加号(Plus_click)操作成功===")
                break
            except:
                count += 1
                print("!!!EXCEPT 点击加号(Plus_click)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 点击加号(Plus_click)操作失败。")
                    break

    #TODO: (method)点击铁路运输的加号Railway_plus
    def Railway_plus(self,web):
        count = 0
        strnow = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[3]/ul/li[6]/div/i[1]'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click();
                # print("===SUCCESS 点击铁路运输的加号(Railway_plus)操作成功===")
                break
            except:
                count += 1
                print("!!!EXCEPT 点击铁路运输的加号(Railway_plus)操作失败，正在第{}次尝试。".format(count))
                if count > 15:
                    time.sleep(120)
                if count > 21:
                    print("***EXCEPT 点击铁路运输的加号(Railway_plus)操作失败。")
                    break


    #TODO: (method)点击标签Label_click
    def Label_click(self,web,strnow):
        count = 0
        while True:
            try:
                WebDriverWait(web, 15).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click();
                # print("===SUCCESS 点击标签(Label_click)操作成功===")
                break
            except:
                count += 1
                print("!!!EXCEPT 点击标签(Label_click)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 点击标签(New_search)操作失败。")
                    break
        
    #TODO: (method)点击检索Search
    def Search(self,web,cc):
        count = 0
        # strnow = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input'
        strcls = 'submit-btn'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, strcls))
                )
                web.find_element(By.CLASS_NAME,strcls).click()
                print(cc+":===SUCCESS 点击检索(Search)按钮成功===")
                break
            except:
                count += 1
                print(cc+":!!!EXCEPT 点击检索(Search)按钮失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print(cc+":***EXCEPT 点击检索(Search)按钮失败。")
                    break
    
    def Click_title(self,web,strnow,cc):
        count = 0

        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                time.sleep(5)
                web.find_element(By.XPATH,strnow).click()
                print(cc+":===SUCCESS 点击论文标题成功===")
                return True
            except:
                count += 1
                print(cc+":!!!EXCEPT 点击论文标题作失败,正在尝试刷新页面并重试第{}次".format(count))

                # strnow = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input'
                refreshbtn = 'submit-btn'
                try:
                    WebDriverWait(web, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, refreshbtn))
                    )
                    web.find_element(By.CLASS_NAME, refreshbtn).click()
                    print(cc+":刷新页面成功,正在重新点击论文标题")
                    continue
                except:
                    print(cc+":刷新页面失败")
                    return False
    #TODO: (method)获取当前页文章列表
    def Get_tr_list(self,web,strnow):
        count = 0
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                tr_list = web.find_elements(By.XPATH,strnow)
                print("===SUCCESS 获取当前页文章列表(Get_tr_list)操作成功===")
                return tr_list
            except:
                count += 1
                print("!!!EXCEPT 获取当前页文章列表(Get_tr_list)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(5)
                if count > 5:
                    print("***EXCEPT 获取当前页文章列表(Get_tr_list)操作失败。")
                    return []

    #TODO: (method)点击引用
    def Preference_click(self,web):
        count = 0
        strnow = '/html/body/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[1]/a/i'
        while True:
            try:
                WebDriverWait(web, 15).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 点击引用(Preference_click)操作成功===")
                return True
            except:
                count += 1
                print("!!!EXCEPT 点击引用(Preference_click)操作失败，正在第{}次尝试。".format(count))
                strnow = '/html/body/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/ul/li[1]/a/i'
                if count > 4:
                    web.refresh()
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 点击引用(Preference_click)操作失败。")
                    return False
    #TODO: (method)点击更多引用格式
    def More_reference_click(self,web):
        count = 0
        strnow = '/html/body/div[7]/div[2]/a'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 点击更多引用格式(More_reference_click)操作成功===")
                return True
            except:
                count += 1
                print("!!!EXCEPT 点击更多引用格式(More_reference_click)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    self.Preference_click(web)
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 点击更多引用格式(More_reference_click)操作失败。")
                    return False

    #TODO: (method)点击自定义
    def Self_defining(self,web):
        count = 0
        strnow = '/html/body/div[3]/div/div[1]/ul/li[12]/a'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 点击自定义(Self_defining)操作成功===")
                return True
            except:
                count += 1
                print("!!!EXCEPT 点击自定义(Self_defining)操作失败，正在第{}次尝试。".format(count))
                if count > 6:
                    web.refresh()
                    time.sleep(20)
                if count > 13:
                    print("***EXCEPT 点击自定义(Self_defining)操作失败。")
                    return False

    #TODO: (method)点击全选
    def All_select(self,web):
        count = 0
        strnow = '/html/body/div[3]/div/div[2]/div[2]/div/div/a[1]'
        # strnow = '/html/body/div[3]/div/div[2]/div[2]/div/label[6]'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 点击全选(All_select)操作成功===")
                return True
            except:
                count += 1
                print("!!!EXCEPT 点击全选(All_select)操作失败，正在第{}次尝试。".format(count))
                if count > 2:
                    self.Self_defining(web)
                if count > 8:
                    time.sleep(30)
                if count > 10:
                    print("***EXCEPT 点击全选(All_select)操作失败。")
                    return False

    #TODO: (method)预览
    def View(self,web):
        count = 0
        strnow = '/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a'
        while True:
            try:
                WebDriverWait(web, 10).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                # print("===SUCCESS 预览(View)操作成功===")
                web.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                return True
            except:
                count += 1
                print("!!!EXCEPT 预览(View)操作失败，正在第{}次尝试。".format(count))
                if count > 4:
                    time.sleep(20)
                if count > 10:
                    print("***EXCEPT 预览(View)操作失败。")
                    return False

    #TODO: (method)获取文本
    def Text(self,web):
        count = 0
        strnow = '//*[@id="result"]/ul/li'
        while True:
            try:
                WebDriverWait(web, 5).until(
                    EC.text_to_be_present_in_element((By.XPATH, strnow),"Keyword")
                )
                text = web.find_element(By.XPATH,strnow).text
                # print("===SUCCESS 获取文本(Text)操作成功===")
                return text
            except:
                count += 1
                if count > 3:
                    web.refresh()
                    print("!!!EXCEPT 获取文本(Text)操作失败".format(count))
                    return " "
                self.All_select(web)
                self.View(web)
                # if count > 7:
                #     time.sleep(30)
                # if count > 11:
                #     print("***EXCEPT 获取文本(Text)操作失败。")
                #     return " "
    
    def click_year(self,web):
        count = 0
        strnow = '/html/body/div[3]/div[2]/div[1]/div[3]/dl[3]/dt/i[1]'
        while True:
            try:
                WebDriverWait(web, 5).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 点击年份(click_year)操作成功===")
                return True
            except:
                count += 1
                if count > 3:
                    time.sleep(2)
                    print("!!!EXCEPT 点击年份(click_year)操作失败，正在第{}次尝试。".format(count))
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 点击年份(click_year)操作失败。")
                    return False

    def all_year(self,web):
        strnow = '//*[@id="divGroup"]/dl[3]/dd/div/ul/li'
        count = 0
        while True:
            try:
                WebDriverWait(web, 5).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                year_list = web.find_elements(By.XPATH,strnow)
                print("===SUCCESS 所有年份(all_year)操作成功===")
                return year_list
            except:
                count += 1
                if count > 3:
                    time.sleep(2)
                    print("!!!EXCEPT 所有年份(all_year)操作失败，正在第{}次尝试。".format(count))
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 所有年份(all_year)操作失败。")
                    return False
    def cancel_year(self,web):
        count = 0
        strnow = '/html/body/div[3]/div[2]/div[1]/div[3]/dl[3]/dd/div/ul/li/input'
        while True:
            try:
                WebDriverWait(web, 5).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 取消年份(cancel_year)操作成功===")
                return True
            except:
                count += 1
                if count > 3:
                    time.sleep(2)
                    print("!!!EXCEPT 取消年份(cancel_year)操作失败，正在第{}次尝试。".format(count))
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 取消年份(cancel_year)操作失败。")
                    return False
    def select_year(self,web,strnow):
        count = 0
        while True:
            try:
                WebDriverWait(web, 5).until(
                    EC.presence_of_element_located((By.XPATH, strnow))
                )
                web.find_element(By.XPATH,strnow).click()
                print("===SUCCESS 选择年份(select_year)操作成功===")
                return True
            except:
                count += 1
                if count > 3:
                    time.sleep(2)
                    print("!!!EXCEPT 选择年份(select_year)操作失败，正在第{}次尝试。".format(count))
                if count > 7:
                    time.sleep(30)
                if count > 11:
                    print("***EXCEPT 点击年份(select_year)操作失败。")
                    return False