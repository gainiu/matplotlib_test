import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


#执行API调用并存储响应
URL='https://api.github.com/search/repositories?q=language:python&sort=star'
respons=requests.get(URL,timeout=30)
print('Status code',respons.status_code)
#将API响应存储在一个变量中
respons_dict=respons.json()
print('Total repositories:',respons_dict['total_count'])
#研究有关仓库的信息
repo_dicts=respons_dict['items']

names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Most-Starred Python Projects on Github'
chart.x_label=names

chart.add('',stars)
chart.render_to_file('python_repo.svg')