=======================
reStructuredText教程
=======================

reStructuredText（简写：RST、ReST或reST）,
它是Python Doc-SIG（Documentation Special Interest Group）的 Docutils 项目的一部分。Docutils 可以从 Python 程序中提取注释和信息，并将它们格式化为各种形式的程序文档。


标题
-----------------------
标题用使用文字和特殊的标点符号下划线来创建的（上划线是可选的），符号的长度需要不小于文字。
可以用作标题使用的标点符号：! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ 
推荐使用的标点符号：= - ` : ' " ~ ^ _ * + # < >
最先出现的符号为一级标题，相同符号为同等级标题，下一个出现的符号为它的子标题，依次为h1，h2，h3，h4，h5，h6。
在相同符号中，有上划线标题的比没有上划线标题高一等级。
虽然没有规定符号对应标题的等级，但按照一种常用的写法不容易出错。一般一篇文档使用到三级标题即可，太多容易混乱。

也可以自己固定使用一种表示方式，如:

* =，有上划线，文章标题
* -，用作节
* ^，用作小节
* ~，用作子小节

使用如下::

    ================================
    文章标题 （一级标题 h1）
    ================================


    1第一节（二级标题 h2）
    ---------------------------------

    1.1第一小节 （三级标题 h3）
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    1.2第二小节 （三级标题 h3）
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    1.2.1第二子小节 （四级级标题 h4）
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    1.2.2第二子小节 （四级级标题 h4）
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    2第二节 （二级标题 h2）
    ---------------------------------

    2.1第一小节 （三级标题 h3）
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    2.2第二小节 （三级标题 h3）
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
转化为HTML后，显示效果：
 
暂不显示效果，会打乱该篇文章结构。


段落
---------------------------------

段落是reST文档中最基本的块。段落是由一个或多个空白行分离的简单的文本块。纯文本写法如下::

    这是一个段落。

    第二个段落，段落使用空行 
    分离，没有空行即使换行，
    还是会显示为一行为一个段落。行尾加反斜杠\
    可以消除每行自动拼接的空格。

    | 第三个段落，行首竖线和空格
    | 可以用来
    |     强制换行
    | 当然最上面还要一个空行。

转化为HTML后，显示效果：

这是一个段落。

第二个段落，段落使用空行 
分离，没有空行即使换行，
还是会显示为一行为一个段落。行尾加反斜杠\
可以消除每行自动拼接的空格。

| 第三个段落，行首竖线和空格
| 可以用来
|     强制换行
| 当然最上面还要一个空行。


行内文本样式    
---------------------------------

行内文本样式使用符号在需要改变的文字前后标记，与其他内容使用空格分离开，如果不需要空格使用转义符\\来消除空格。可使用文本样式如下：

* 斜体：使用1个星号*或包裹文字。
* 粗体：使用2个星号**或包裹文字。
* 等宽字体：使用2个反引号``包裹文字。

如果文本中有其他星号或反引号，可能会引起混淆，使用一个反斜杠进行转义，像\\* 。如下::

    标记前后各需一个空格：这是 *斜体* 文字，这是 **粗体** 文字，这是 ``等宽字体`` 。中间会有空格。

    增加反斜杠\\来消除空格：这是\ *斜体*\ 文字，这是\ **粗体**\ 文字，这是\ ``等宽字体``\ 。
    

标记前后各需一个空格：这是 *斜体* 文字，这是 **粗体** 文字，这是 ``等宽字体`` 。中间会有空格。

增加反斜杠\\来消除空格：这是\ *斜体*\ 文字，这是\ **粗体**\ 文字，这是\ ``等宽字体``\ 。


    


列表  
---------------------------------

无序列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

无需列表可以用符号"-", "\*" or "+"表示，符号和后面文字之间需要一个空格。列表第一行的前面和最后一行的都需要一个空行。下级列表具有相同的缩进，一般2个空格，而且与上级列表间要有一个空行。如果使用不同的符号，需要一个空行。一般使用自己常用的一个符号即可，如星号\*。无序列表使用如下::

    * 真菌
    * 动物
    
        * 狗
        * 猪
        
    * 植物
    
        - 苹果
        
        + 梨
        + 西瓜
        
转化为HTML后，显示效果：

* 真菌
* 动物 

  * 狗
  * 猪

* 水果

  - 苹果
  
  + 梨
  + 西瓜


有序列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
有序列表由数字或字母加上符号组成，符号和后面文字需加一个空格。可使用的数字或字母如下：

* 阿拉伯数字: 1，2，3，... (无上限)
* 大写字母: A, B, C, ..., Z
* 小写字母: a, b, c, ..., z
* 大写罗马数字: I, II, III, IV, ..., MMMMCMXCIX (4999)
* 小写罗马数字: i, ii, iii, iv, ..., mmmmcmxcix (4999)

可以使用的符号，点号".", 右括号 ")" ，左右括号"( )"。表示方式如下：

* 点号：1. ， A. ， a. 
* 右括号：1) ， A） ， a）
* 左右括号：(1) ， (A) ， (a)

不同需要表示需要方式要空一行。下级列表需要相同的缩进，一般2个空格。有序列表可以结合井号 # 自动生成序号。有序列表使用如下::

    1. 井号方法

        a) 使用井号#
        #) 可以自动
        #) 生成序号

    #. 关于序号

       (C) 序号可以从
       (D) 任意数字字母开始
       (E) 但需要顺序递增

    II) 空格
    
    (iv) 空行

转化为HTML后，显示效果：

1. 井号方法

    a) 使用井号#
    #) 可以自动
    #) 生成序号

#. 关于序号

   (C) 序号可以从
   (D) 任意数字字母开始
   (E) 但需要顺序递增

II) 空格

(iv) 空行


定义列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

和其他两个列表不同，定义列表是项目及其注释的组合。每个项目与其注释不空行，注释内容缩进4个空格。项目于项目之间空一行。使用如下::

    郑州商品交易所
        简称郑商所，成立于1990年10月12日，是中国的期货交易所之一。
        在现货交易成功运行两年以后，于1993年5月28日正式推出期货交易。

    大连商品交易所
        成立于1993年2月28日，是中国的期货交易所之一。

转化为HTML后，显示效果：

郑州商品交易所
    简称郑商所，成立于1990年10月12日，是中国的期货交易所之一。
    在现货交易成功运行两年以后，于1993年5月28日正式推出期货交易。

大连商品交易所
  成立于1993年2月28日，是中国的期货交易所之一。
  

无序列表对应html的<ul>标签，有序列表对应html的<ol>标签，定义列表对应html的<dl>标签。在chrome浏览器中，网页的某个位置点击右键选检查，可查看该位置对应的html代码。

文本块
---------------------------------
文本块内是不会经过任何转化，保留原有的内容和格式，一般可以用来显示代码，写诗。分为2中：

行内文本块：即上文的行内文本样式的等宽字体，使用前后各使用2各反引号包裹内容，前后与其他内容还需一个空格。

文本块：使用两个冒号和一个空行，文本块内容要缩进，最后使用一个空行。两个冒号位置可以有3中：

* 上一段文字的末尾且冒号前没空格。生成网页后，在该位置显示一个冒号。
* 上一段文字的末尾且冒号前有空格。生成网页后，没有冒号。
* 在单独的一行行首。生成网页后，没有冒号。

文本块使用如下::

    这是行内文本样式的等宽字体，如 ``里面\* * _任何都不会`` 处理。

    这里是正常文本，接下来是文本块::

       文本块里不会经过任何处理，除非
       空行加上行首有文字，就会退出文本行。


       可以任意多的空行。

    现在又是正常文本。
    
转化为HTML后，显示效果：

这是行内文本样式的等宽字体，如 `` 里面\* * _任何都不会`` 处理。

这里是正常文本，接下来是文本块::

   文本块里不会经过任何处理，除非
   空行加上行首有文字，就会退出文本行。

   可以任意多的空行。

现在又是正常文本。


表格
---------------------------------

有四种绘制表格的方法：网格表格，简单表格，列表表格，csv表格。

网格表格,需要“绘制”单元格网格，功能完整但写法复杂，使用如下::

    +------------+------------+-----------+
    | Header 1   |   Header 2 | Header 3  |
    +============+============+===========+
    | body row 1 | column 2   | column 3  |
    +------------+------------+-----------+
    | body row 2 | Cells may span columns.|
    +------------+------------+-----------+
    | body row 3 | Cells may  | - Cells   |
    +------------+ span rows. | - contain |
    | body row 4 |            | - blocks. |
    +------------+------------+-----------+
    
转化为HTML后，显示效果：

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

简单表格，使用如下::

    =====  =====  ======
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

转化为HTML后，显示效果：

=====  =====  ======
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

列表表格，简单使用如下::

    .. list-table::

        * - 1,1
          - 1,2
          - 1,3
        * - 2,1
          - 
          - 2,3
        * - 3,1
          - 3,2
          - 3,3
          
转化为HTML后，显示效果：

.. list-table::

    * - 1,1
      - 1,2
      - 1,3
    * - 2,1
      - 
      - 2,3
    * - 3,1
      - 3,2
      - 3,3
              
列表表格，增加一些设置，使用如下::

    .. list-table:: Frozen Delights!
       :widths: 15 10 30
       :header-rows: 1

       * - Treat
         - Quantity
         - Description
       * - Albatross
         - 2.99
         - On a stick!
       * - Crunchy Frog
         - 1.49
         - If we took the bones out, it wouldn't be
           crunchy, now would it?
       * - Gannet Ripple
         - 1.99
         - On a stick!

转化为HTML后，显示效果：

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!
     
CSV表格，使用如下::     

    .. csv-table:: 2020年02月03日期货交易数据
       :header: "品种月份", "昨结算", "今开盘"

       "AP005", 7392, 6895
       "CF005", 13515, 12570
       "TA005", 4808, 4470

转化为HTML后，显示效果：
     
.. csv-table:: 2020年02月03日期货交易数据
   :header: "品种月份", "昨结算", "今开盘"

   "AP005", 7392, 6895
   "CF005", 13515, 12570
   "TA005", 4808, 4470
  
     
     

超链接
---------------------------------

外部链接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

外部链接有两种写法，第一种是链接地址和链接显示文本写在一起，当不需要链接显示文本时直接写入链接地址即可，如下::
   
    `百度 <https://baidu.com/>`_
    
    http://example.com
    
显示效果如下：

`百度 <https://baidu.com/>`_

http://example.com

.. important:: 链接显示文本和\<符号之间必须要有一个空格。

第二种是链接和链接地址分开写，如下::

   这里有个 `链接`_ 可以点击。

   .. _链接: https://domain.invalid/

显示效果如下：

这里有个 `链接`_ 可以点击。

.. _链接: https://domain.invalid/


内部链接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



在sphinx中，内部链接使用特殊的规则。

链接到指定文档，可以使用 ``:doc:`文件名``` 会自动生成链接到指定文档，指定文件的文件名可以有两种写法：

* 相对路径，如果指定文档名称people.rst，为与该篇文档同一目录下，直接写文档名称： ``:doc:`people``` ，如果在上一级目录下，则使用： ``:doc:`../people``` 链接到people文档。
* 绝对路径，绝对路径以整个文档首页目录为根目录，如：``:doc:`/people``` 表示链接到根目录下的people文档。

链接的显示文字默认为指定文档的标题，如果要修改链接显示文字，使用 ``:doc:`链接显示文本 <文件名>```  表示。示例如下::

    点击这个链接： :doc:`sphinx` 可以到sphinx教程页面。
    
    点击这个链接： :doc:`链接显示文本 <sphinx>` 可以到sphinx教程页面。
    
转化为显示效果如下：    

点击这个链接： :doc:`sphinx` 可以到sphinx教程页面。

点击这个链接： :doc:`链接显示文本 <sphinx>` 可以到sphinx教程页面。

链接到整个文档任意位置，使用

This is the text of the section.

It refers to the section itself, see :ref:`my-reference-label`.

更多信息阅读：
* `restructuredtext文档：超链接 <https://docutils.sourceforge.io/docs/user/rst/quickref.html#hyperlink-targets>`_


参考文献
---------------------------------

* `简书：seay - reStructuredText(rst)快速入门语法说明 <https://www.jianshu.com/p/1885d5570b37>`_
* `bary.com：白杉 - 用reStructuredText写作：快速入门指南 <http://www.bary.com/doc/a/228277572381775842/>`_
* `sphinx.org.cn：restructuredtext翻译文档 <https://www.sphinx.org.cn/usage/restructuredtext/basics.html>`_
* `pythondoc.com：restructuredtext翻译文档 <http://www.pythondoc.com/sphinx/rest.html/>`_
* `维基百科：ReStructuredText <https://zh.wikipedia.org/zh-cn/ReStructuredText>`_

.. _my-reference-label:

网站
---------------------------------
* `restructuredtext官网 <https://docutils.sourceforge.io/rst.html>`_
* `restructuredtext文档：快速开始 <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
* `restructuredtext文档：快速参考 <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
* `sphinx文档：restructuredtext入门 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Python开发者指南：编写Python文档 <https://devguide.python.org/documenting/>`_
