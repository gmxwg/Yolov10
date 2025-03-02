1. 创建自己的项目
```git init```
生成的.git就是代码仓库（不能动.git)
2. 把abc.txt放入暂存区，类似快递把东西放进包里
```git add abc.txt```
把所有文件都提交到暂存区
```git add . ```

3. 把文件放入仓库
```git commit```
-m 可对文件进行备注，如
```git commit -m “第一版”```

4. 回溯版本
```git reset --hard[commit id]或git checkout[commit id]```
如git reset --hard f2ed21...

5. git分支
其实就算一个程序的多个版本，版本都依赖一个主干，但是各自略有不同，master一般用来保存经过测试的稳定代码，要想开发文件一般在master基础上复制出一个develop分支
```git branch```查看分支
```git checkout -b develop```创建develop分支

6. 在develop开发测试完毕后，将develop合并到master上
先提交修改，然后切换到master分支```git checkout master```
最后合并```git merge develop```

7. 关联github仓库
```git remote add origin git@github.com:gain-wyj/wyj_first.git```

8. 将代码推送到github上
```git push -u origin master```