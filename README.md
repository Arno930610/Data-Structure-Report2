<h1 align="center">暑修資料結構期末報告　11128004 林峻成 11124129吳張傑　</h1>
<h2 align="center">Python實現二叉搜尋樹</h2>



二叉搜尋樹（Binary Search Tree）是一種特殊的二叉樹，又稱為排序二叉樹、有序二叉樹。

二叉搜尋樹具有如下特性：

1. 如果二叉樹的左子樹不為空，則左子樹上所有節點的值均小於它的根節點的值。

2. 如果二叉樹的右子樹不為空，則右子樹上所有節點的值均大於它的根節點的值。

3. 如果獨立地看，左子樹、右子樹也分別為二叉搜尋樹。用遞迴的思想，直到樹的葉子節點。

下圖是一個二叉搜尋樹的例子，可以參照圖片來核對這三條特性，本文使用Python來實現二叉搜尋樹。


<img width="704" height="389" alt="1" src="https://github.com/Arno930610/Data-Structure-Report2/blob/main/1%E7%9A%84%E7%AF%80%E9%BB%9E.png] />


一、實現節點類

所有樹結構都是由一個個的節點構成的，本文使用鏈式的方式來實現二叉搜尋樹，所以先實現一個節點類。

<img width="716" height="491" alt="1節點" src="https://github.com/user-attachments/assets/48f14845-ea8f-4b02-bb6c-222846cbe468" />


結果


<img width="294" height="128" alt="1結果" src="https://github.com/user-attachments/assets/ab9e876d-3bd0-4250-8a2a-3a335276e1d5" />



在二叉樹中添加節點時，要先創建節點，有了節點類，實例化一個節點類的實例即可。節點初始化時是一個孤立的節點，指向的父節點、左子樹、右子樹都為空。將節點掛到樹上（添加到樹中）後，才屬於樹的一部分。

二、實現二叉搜尋樹類

實現一個二叉搜尋樹的類 SearchBinaryTree，創建二叉搜尋樹時，實例化一個 SearchBinaryTree 類的實例即可。

<img width="581" height="913" alt="2-1" src="https://github.com/user-attachments/assets/23f13333-9a6e-4cc4-91db-cd9e57955220" />

<img width="856" height="833" alt="2-2" src="https://github.com/user-attachments/assets/d42daa75-141e-40f4-89dc-ac6c6be9ce86" />

<img width="496" height="609" alt="2-3" src="https://github.com/user-attachments/assets/33e3e8d7-f62d-46a6-9f26-1e8d9d1b7b69" />

結果


<img width="392" height="317" alt="2結" src="https://github.com/user-attachments/assets/479e97e6-94ef-47cc-a54f-5c580ecb6b36" />


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

<img width="588" height="879" alt="3" src="https://github.com/user-attachments/assets/f3038e70-0914-4cdf-b0bd-fddf5d53c3ce" />

結果

<img width="280" height="356" alt="3結" src="https://github.com/user-attachments/assets/698bc39f-204d-4bbc-9086-71a6380258b2" />



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


<img width="695" height="831" alt="4" src="https://github.com/user-attachments/assets/bd03d996-2eb9-447d-b4dc-20b567df30f8" />

<img width="432" height="194" alt="4-1" src="https://github.com/user-attachments/assets/e337e1b4-f170-4e7c-b4be-07c08414e8be" />


結果

<img width="962" height="355" alt="4結" src="https://github.com/user-attachments/assets/728d3959-09eb-43a3-ab98-5ebc1a51c858" />


insert_normal(value): 二叉搜尋樹新增節點的非遞迴實現。理解了上面講述的非遞迴添加過程，程式碼就很好理解了，程式碼完全是按照上面的過程實現的。

上面的遞迴方式和非遞迴方式添加的方法中，都支援傳入一個節點或者入節點中保存的數值。

<img width="847" height="829" alt="5" src="https://github.com/user-attachments/assets/3246cb05-fb72-4a95-be96-2f466822c632" />


結果

<img width="319" height="230" alt="5結" src="https://github.com/user-attachments/assets/84af60eb-7c8c-4d58-a7ee-1740770882a7" />


新增節點後的二叉搜尋樹結構如上圖，在程式給出的原始數據列表中，有兩個 50 和 18，會出現新增節點時數值與已有節點的數值相同的情況，可以看到並沒有重複添加。


<img width="738" height="430" alt="1111" src="https://github.com/user-attachments/assets/e08d520c-478b-41da-9fd2-2a24d8f18760" />


程式碼已經實現了二叉搜尋樹的廣度優先遍歷和深度優先遍歷，現在新增了數據，可以看一下遍歷的結果。程式碼已經實現了二叉搜尋樹的廣度優先遍歷和深度優先遍歷，現在新增了數據，可以看一下遍歷的結果。


<img width="495" height="914" alt="6" src="https://github.com/user-attachments/assets/ecace23f-1638-4e62-922c-f970fc835356" />


結果

<img width="321" height="108" alt="6結" src="https://github.com/user-attachments/assets/de10a9a3-3cc4-4774-85a2-0ac1801c0710" />


四、二叉搜尋樹的額外功能：最大值和最小值

實現二叉搜尋樹的輔助函數，返回最大值節點和最小值節點的方法。


<img width="674" height="576" alt="7" src="https://github.com/user-attachments/assets/387ee583-70af-4f19-892d-b292900cdb58" />


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



結果


<img width="240" height="87" alt="7結" src="https://github.com/user-attachments/assets/2e7fb658-609e-47df-a0de-b9d3e4efc085" />



五、完整結果


<img width="555" height="618" alt="8" src="https://github.com/user-attachments/assets/b887fa63-302b-4381-8b2c-033823c59558" />


<img width="270" height="82" alt="8結" src="https://github.com/user-attachments/assets/3dbe2620-728e-4589-98f7-58e9fe275c42" />
