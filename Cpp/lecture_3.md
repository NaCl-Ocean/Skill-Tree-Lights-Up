**C++中对文件操作需要包含头文件 `fstream `**



操作文件的三大类:

1. ofstream：写操作
2. ifstream： 读操作
3. fstream ： 读写操作

# 写文件

   写文件步骤如下：

1. 包含头文件   

   `#include <fstream>`

2. 创建流对象  

   `ofstream ofs;`

3. 打开文件

   `ofs.open("文件路径",打开方式);`

4. 写数据

   `ofs << "写入的数据";`

5. 关闭文件

   `ofs.close();`

   

| 打开方式    | 解释                       |
| ----------- | -------------------------- |
| ios::in     | 为读文件而打开文件         |
| ios::out    | 为写文件而打开文件         |
| ios::ate    | 初始位置：文件尾           |
| ios::app    | 追加方式写文件             |
| ios::trunc  | 如果文件存在先删除，再创建 |
| ios::binary | 二进制方式                 |



# 读文件

读文件步骤如下：

1. 包含头文件   

   `#include <fstream>`

2. 创建流对象  

   `ifstream ifs;`

3. 打开文件并判断文件是否打开成功

   `ifs.open("文件路径",打开方式);`

4. 读数据

   四种方式读取

5. 关闭文件

   `ifs.close();`

```C++
int main(){
    ifstream ifs;
    ifs.open("test.txt",ios::in);
    if (!ifs.is_open()){
        cout<<"open file failed"<<endl;
        return 0;
    }

    char buf[1024]={0};
    
    /* method 1*/
    while(ifs >> buf){   --》ifs >> buf 的作用是 每次读一行传入buf中，并返回是否读到文件末尾，若读到末尾，则返回False
        cout<<buf<<endl;
    }
    
    /* method 2 */
    while (ifs.getline(buf,sizeof(buf))){
        cout << buf <<endl;
    }
    
    /* method 3 */
   	string buf;
	while (getline(ifs, buf))
	{
		cout << buf << endl;
	}
    ifs.close();

}
```

# 二进制写文件

- 打开文件指定为`ios::binary`

1. 包含头文件   

   `#include <fstream>`

2. 创建流对象  

   `ofstream ofs;`

3. 打开文件

   `ofs.open("文件路径",ios::binary|ios::out);`

4. 写数据

   ```C++
   Person p = {'张三'，18};
   ofs.write((const char *)&p,sizeof(p));
   		     首地址            长度
   ```

5. 关闭文件

   `ofs.close();`



# 二进制读文件

1. 包含头文件   

   `#include <fstream>`

2. 创建流对象  

   `ifstream ifs;`

3. 打开文件并判断文件是否打开成功

   `ifs.open("文件路径",ios::in|ios::binary);`

4. 读数据

   ```C++
   Person p;
   ifs.read((char*)&p,sizeof(p));
   ```

5. 关闭文件

   `ifs.close();`