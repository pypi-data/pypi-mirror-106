#-*- codeing = utf-8 -*-
#@time : 2021-05-08 10:23
#@Author : liugeliang
#@File : V1.py
#@Software : PyCharm



import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def getPubMed_reference(chromedriver_path,disease_name,drugname_list_path,download_path):

  ##创建下载路径
  download_path = os.path.join(download_path,disease_name)
  os.mkdir(download_path)

  drug_nametxt = open(drugname_list_path, 'r')
  drug_name = drug_nametxt.read()
  drug_nametxt.close()
  drug_name_list = drug_name.split('\n')

  ##日志文件路径
  log_file_path  = os.path.join(download_path,'log/history.txt')
  no_result_file_path = os.path.join(download_path,'log/no_result_drug.txt')
  log_path  = os.path.join(download_path,'log')

  log_file = os.path.exists(log_file_path)
  no_result_file = os.path.exists(no_result_file_path)

  if log_file == True and no_result_file == True:
    print('已存在下载记录...')
    historytxt = open(log_file_path, 'r')
    history = historytxt.read()
    historytxt.close()
    history_list = set(history.split('\n')[:-1])

    noresulttxt = open(no_result_file_path, 'r')
    no_result = noresulttxt.read()
    noresulttxt.close()
    noresult_list = set(no_result.split('\n')[:-1])

    drug_name_list = list(set(drug_name_list) - noresult_list)
    drug_name_list = list(set(drug_name_list) - history_list)
    print(f'剩余下载{len(drug_name_list)}条...')
    print('=================================')
  elif log_file == True and no_result_file == False:
    print('已存在下载记录...')
    historytxt = open(log_file_path, 'r')
    history = historytxt.read()
    historytxt.close()
    history_list = set(history.split('\n')[:-1])
    drug_name_list = list(set(drug_name_list) - history_list)
    print(f'剩余下载{len(drug_name_list)}条...')
    print('=================================')
  else:
    os.mkdir(log_path)
    print("首次下载，不存在下载记录...")
    print(f"共需下载{len(drug_name_list)}条...")
    print('=================================')

  for i in drug_name_list:
    ##浏览器设置
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
      "download.default_directory": download_path,   ##设置浏览器下载路径
      "download.prompt_for_download": False,
    })
    chrome_options.add_argument("--headless")  ##设置无头浏览
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(options=chrome_options,executable_path = chromedriver_path)
    # driver=webdriver.Chrome(executable_path = chromedriver)
    url = f'https://pubmed.ncbi.nlm.nih.gov/?term=%28{disease_name}%29+AND+%28{i}%29'  #构筑URL
    driver.get(url)
    ##文件命名
    name_1 = disease_name.replace(" ", "")
    name_2 = i.replace(" ", "")
    name_len = len(name_1)
    if name_len >= 10:
      downloadfile_name = f'summary-{name_1[0:10]}-set.txt'
    elif name_len == 9:
      downloadfile_name = f'summary-{name_1}A-set.txt'
    elif name_len == 8:
      downloadfile_name = f'summary-{name_1}AN-set.txt'
    elif name_len == 7:
      downloadfile_name = f'summary-{name_1}AND-set.txt'
    else:
      name_3 = f'{name_1}AND{name_2}'
      downloadfile_name = f'summary-{name_3[0:10]}-set.txt'
    ##判断是否存在文献
    try:
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'save-results-panel-trigger')))
      driver.find_element_by_xpath('//*[@id="save-results-panel-trigger"]').click()
      flag = True
    except:
      flag = False
    paper_haveornot = flag
    ##判断是否仅有一篇文献
    try:
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'save-action-selection')))
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save-action-selection"]/option[2]')))
      driver.find_element_by_xpath('//*[@id="save-action-selection"]/option[2]').click()
      flag = False
    except:
      flag = True
    paper_only_one = flag

    ##存在多条文献
    if paper_haveornot == True and paper_only_one == False:
      # element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'save-results-panel-trigger')))
      print('1----页面加载成功')
      # driver.find_element_by_xpath('//*[@id="save-results-panel-trigger"]').click()  ##点击save
      # element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'save-action-selection')))
      # driver.find_element_by_xpath('//*[@id="save-action-selection"]').click()       ##点击选择页面
      # element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save-action-selection"]/option[2]')))
      # driver.find_element_by_xpath('//*[@id="save-action-selection"]/option[2]').click()  ##选择所有结果 （最多为1W条）
      print('2---选项调试成功')
      element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="save-action-panel-form"]/div[3]/button[1]')))
      driver.find_element_by_xpath('//*[@id="save-action-panel-form"]/div[3]/button[1]').click()
      print('3---已开始下载')
      downloadfile_path = os.path.join(download_path,downloadfile_name)
      while os.path.exists(downloadfile_path) == False:
        time.sleep(3)
      else:
        print(f'{disease_name}AND{i}下载成功')
        print('======================================================')
        os.rename(f'{download_path}/{downloadfile_name}',f'{download_path}/{i}.txt')
      with open(log_file_path, 'a') as one_result:
        one_result.write(i)  # 写入
        one_result.write('\n')

    ##目前仅存在一条文献
    elif paper_haveornot == True and paper_only_one == True:
      print('1----页面加载成功')
      print('2---选项调试成功')
      element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="full-view-identifiers"]/li[1]/span/strong')))
      pubid = driver.find_element_by_xpath('//*[@id="full-view-identifiers"]/li[1]/span/strong').text
      element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="save-action-panel-form"]/div[2]/button[1]')))
      driver.find_element_by_xpath('//*[@id="save-action-panel-form"]/div[2]/button[1]').click()
      print('3---已开始下载')
      downloadfile_path = os.path.join(download_path, f'summary-{pubid}.txt')
      while os.path.exists(downloadfile_path) == False:
        time.sleep(2)
      else:
        print(f'{disease_name}AND{i}下载成功')
        print('======================================================')
        os.rename(f'{download_path}/summary-{pubid}.txt',
                  f'{download_path}/{i}.txt')
      with open(log_file_path, 'a') as one_result:
        one_result.write(i)  # 写入
        one_result.write('\n')
    elif paper_haveornot == False:
      with open(no_result_file_path, 'a') as no_result:
        no_result.write(i)  # 写入
        no_result.write('\n')
  print('==============全部下载完成，请打开文件夹查看下载文件及日志文件==============')
