#[icourse爬虫](https://gitee.com/merak0514/python/tree/master/project/icourse)
+ 其中[icouse.py](https://gitee.com/merak0514/python/blob/master/project/icourse/icourse.py)是自动下载其中所有的pdf文件
使用方法：修改其中的school_id, tid即可下载。原始demo为高等数学。
+ [download_code.py](https://gitee.com/merak0514/python/blob/master/project/icourse/download_code.py)是自动下载其中每学期每次作业所有学生的每一份【代码】的爬虫。需要提供教师账号。主要用于后期代码是否抄袭的分析处理。
1. 首先需要在data/account.json中写入账号信息。格式为 `{"username": , "passwd": ,}`
2. 在main中设置开始的学期，单元和学生（一般用于中断后接着下载或debug），默认可不填。

学生的所有代码会按照目录结构[H://data/term(number)/(unit_name)/(student_nickname)_(student_realname)/(code).cpp]的形式保存
学生的信息储存在[H://data/term(number)/(unit_name)/(student_nickname)_(student_realname)/information.json]

+ [random_useragent](https://gitee.com/merak0514/python/blob/master/project/icourse/random_useragent)是随机生成一个header的浏览器列表。[使用方式](https://gitee.com/merak0514/python/blob/master/project/icourse/random_useragent)
+ [新增连接数据库模块](https://gitee.com/merak0514/python/blob/master/project/icourse/ModuleIcourse.py)（未完成）
