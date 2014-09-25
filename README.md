heroku
======
+ cd /c/hellodjango/venv/scripts/hellodjango
+ git init
+ git add .
+ git commit -m "my django app"
+ git pull
+ git git push origin master

1)
:Adams@ADAMS-PC /c/hellodjango/venv/scripts/hellodjango (master)
:git init
Reinitialized existing Git repository in c:/hellodjango/venv/scripts/hellodjango
/.git/

2)
Adams@ADAMS-PC /c/hellodjango/venv/scripts/hellodjango (master)
$ git remote add origin https://github.com/akipkemei/heroku.git

3)

Adams@ADAMS-PC /c/hellodjango/venv/scripts/hellodjango (master)
:git push -u origin master

Username for 'https://github.com': akipkemei@gmail.com
:
Counting objects: 25, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (22/22), done.
Writing objects: 100% (25/25), 3.97 KiB, done.
Total 25 (delta 7), reused 0 (delta 0)
To https://github.com/akipkemei/heroku.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
Adams@ADAMS-PC /c/hellodjango/venv/scripts/hellodjango (master)
