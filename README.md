<h1 align="center">暑修資料結構期末報告　11128004 林峻成 11124129吳張傑　</h1>
<h2 align="center">Python實現二叉搜尋樹</h2>



二叉搜尋樹（Binary Search Tree）是一種特殊的二叉樹，又稱為排序二叉樹、有序二叉樹。

二叉搜尋樹具有如下特性：

1. 如果二叉樹的左子樹不為空，則左子樹上所有節點的值均小於它的根節點的值。

2. 如果二叉樹的右子樹不為空，則右子樹上所有節點的值均大於它的根節點的值。

3. 如果獨立地看，左子樹、右子樹也分別為二叉搜尋樹。用遞迴的思想，直到樹的葉子節點。

下圖是一個二叉搜尋樹的例子，可以參照圖片來核對這三條特性，本文使用Python來實現二叉搜尋樹。


<img width="704" height="389" alt="1" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/%E4%BA%8C%E5%8F%89%E6%90%9C%E5%B0%8B%E6%A8%B9%E7%9A%84%E4%BE%8B%E5%AD%90.png"/>


一、實現節點類

所有樹結構都是由一個個的節點構成的，本文使用鏈式的方式來實現二叉搜尋樹，所以先實現一個節點類。

<img width="716" height="491" alt="1節點" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/1.png" />


執行結果


<img width="294" height="128" alt="1結果" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/1%E7%B5%90%E6%9E%9C.png" />



在二叉樹中添加節點時，要先創建節點，有了節點類，實例化一個節點類的實例即可。節點初始化時是一個孤立的節點，指向的父節點、左子樹、右子樹都為空。將節點掛到樹上（添加到樹中）後，才屬於樹的一部分。

二、實現二叉搜尋樹類

實現一個二叉搜尋樹的類 SearchBinaryTree，創建二叉搜尋樹時，實例化一個 SearchBinaryTree 類的實例即可。

<img width="581" height="913" alt="2-1" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/2-1.png" />

<img width="856" height="833" alt="2-2" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/2-2.png" />

<img width="496" height="609" alt="2-3" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/2-3.png" />

執行結果


<img width="392" height="317" alt="2結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/2%E7%B5%90%E6%9E%9C.png" />


程式碼中實現了判斷二叉樹是否為空的 is_empty() 方法、一對供實例物件獲取和設置根節點的 root() 方法，按樹形結構打印二叉樹的 show_tree() 方法，二叉樹的廣度優先遍歷方法和三種深度優先遍歷方法，這裡就不一一介紹了，可以參考本專欄中的其他文章。


三、二叉搜尋樹添加節點

本文開頭列出了二叉搜尋樹的特性，向二叉搜尋樹中添加新節點時，一定要保證二叉搜尋樹仍然滿足這些特性。所以，在添加節點前，要先判斷新節點中的數值大小，根據數值的大小來找到插入節點的位置。

向二叉搜尋樹中添加新節點的過程為：

  1. 如果二叉搜尋樹為空，則將新節點添加在根節點的位置。

  2. 如果二叉搜尋樹不為空，根據新節點中的數值大小，分別如下情況：

　　2.1 如果新節點中的數值小於根節點中的數值，則將新節點添加到二叉搜尋樹的左子樹中。

　　2.2 如果新節點中的數值大於根節點中的數值，則將新節點添加到二叉搜尋樹的右子樹中。

　　2.3 如果新節點中的數值等於根節點中的數值，按照需求進行處理，可以自己選擇不添加、添加到左子樹中或添加到右子樹中，本文採不添加處理。

  3.  左子樹和右子樹也是二叉搜尋樹，所以遞迴地使用 1、2 的步驟在左子樹和右子樹中找到新節點的添加位置，添加節點。

<img width="588" height="879" alt="3" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/3.png" />

執行結果

<img width="280" height="356" alt="3結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/3%E7%B5%90%E6%9E%9C.png" />



insert(root, value)：二叉搜尋樹新增節點的迭代實現。這個方法就是根據上面的添加過程，先找到要新增節點的位置，然後再插入節點。方法是從根節點開始，通過判斷當前子樹的根節點和新節點的大小，當遇到子樹的根節點為空時，就說明找到了要新增節點的位置。每次判斷當前節點的左或右返回，作為下一次遞迴的引數。

對於這個過程，如果感覺很難，可以將這個過程一步一步寫成添加，畫一下樹中節點一個個添加的過程，就可以理解了。

當然，也可以使用非遞迴的方式來實現。非遞迴的添加過程如下：

如果二叉搜尋樹為空，則將新節點添加在根節點的位置。

如果二叉搜尋樹不為空，先定義一個變數 current_node 表示當前節點，最開始的當前節點 current_node 為根節點。

然後進入一個無限迴圈，在迴圈中需要退出迴圈的條件。在無限迴圈中，根據新節點的數值大小，分別如下情況：

2.1 如果新節點的數值小於當前節點的數值，則判斷當前節點是否有左子節點：

如果有，則將當前節點設定為當前節點的左子節點，繼續迴圈；

如果沒有，則將新節點添加到當前節點的左子樹，退出迴圈。

2.2 如果新節點的數值大於當前節點的數值，則判斷當前節點是否有右子節點，處理方式同上。

2.3 如果新節點的數值等於根節點中的數值，按照需求進行處理，可以自己選擇不新增。添加到左子樹中或添加到右子樹中，本文採不新增處理，直接退出無限迴圈即可。


<img width="695" height="831" alt="4" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/4-1.png" />

<img width="432" height="194" alt="4-1" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/4-2.png" />


執行結果

<img width="962" height="355" alt="4結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/4%E7%B5%90%E6%9E%9C.png" />


insert_normal(value): 二叉搜尋樹新增節點的非遞迴實現。理解了上面講述的非遞迴添加過程，程式碼就很好理解了，程式碼完全是按照上面的過程實現的。

上面的遞迴方式和非遞迴方式添加的方法中，都支援傳入一個節點或者入節點中保存的數值。

<img width="847" height="829" alt="5" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/5.png" />


執行結果

<img width="319" height="230" alt="5結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/5%E7%B5%90%E6%9E%9C.png" />


新增節點後的二叉搜尋樹結構如上圖，在程式給出的原始數據列表中，有兩個 50 和 18，會出現新增節點時數值與已有節點的數值相同的情況，可以看到並沒有重複添加。
<img width="319" height="230" alt="5結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/1111.png" />




程式碼已經實現了二叉搜尋樹的廣度優先遍歷和深度優先遍歷，現在新增了數據，可以看一下遍歷的結果。程式碼已經實現了二叉搜尋樹的廣度優先遍歷和深度優先遍歷，現在新增了數據，可以看一下遍歷的結果。
<img width="999" height="999" alt="1111" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/6-1.png" />

<img width="495" height="914" alt="6" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/6-2.png" />


執行結果

<img width="321" height="108" alt="6結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/6%E7%B5%90%E6%9E%9C.png" />


四、二叉搜尋樹的額外功能：最大值和最小值

實現二叉搜尋樹的輔助函數，返回最大值節點和最小值節點的方法。


<img width="674" height="576" alt="7" src="https://github.com/vi55c7a/0822/blob/main/7.png" />


功能說明：

search(root, data)：
判斷某個數值是否存在於二叉搜尋樹中。

如果二叉搜尋樹是空樹，回傳 False。

如果等於根節點，回傳 True。

否則根據數值大小，遞迴到左子樹或右子樹繼續查找。

get_max(root)：
回傳二叉搜尋樹中的最大值。

規則：最大值一定出現在最右側的節點。

get_min(root)：
回傳二叉搜尋樹中的最小值。

規則：最小值一定出現在最左側的節點。



執行結果


<img width="555" height="618" alt="8" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/7%E7%B5%90%E6%9E%9C.png" />



五、完整結果


<img width="555" height="618" alt="8" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/8.png" />


<img width="270" height="82" alt="8結" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/8%E7%B5%90%E6%9E%9C.png" />
