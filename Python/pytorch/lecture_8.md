# 前引

- tensorboard的**整体思路**

  - Python脚本中通过**summarywriter**将要记录的数据写入**event file**中

  - terminal中**运行tensorboard**，解析event file中的数据，进行可视化，转发到**6006端口**

    - ```
      tensoboard --logdir='' -->terminal中运行tensorboard
      ```



# SummaryWriter

- 一个写入event_file的高级抽象类 

- `SummaryWriter(log_dir,comment,filename_suffix)`

  - log_dir：指定event_file的存放位置

    - 当不指定时，在当前文件夹创建如下文件结构

      - ```
        runs
        |---date.....comment
        				  |---events.... --》event_file
        ```

  - comment：不指定log_dir时，文件夹的后缀

  - filename_suffix：event file的文件名后缀

# add_scalar



