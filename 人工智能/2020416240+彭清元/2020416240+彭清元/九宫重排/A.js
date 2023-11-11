/*
 * @Descripttion: my project
 * @version: 1.0
 * @Author: Typecoh
 * @Date: 2023-05-16 14:46:26
 * @LastEditors: Typecoh
 * @LastEditTime: 2023-05-16 15:54:58
 */
class Node {
    state = [];
    parent = null;
    value = 0;
    depth = 0;
}

class Stack {
    constructor() {
        this.items = []
    }

    // 新增元素
    add(el) {
        this.items.push(el)
    }

    // 删除栈顶的元素并返回其值
    pop() {
        return this.items.pop()
    }

    // 返回栈顶的元素
    peek() {
        return this.items[this.items.length - 1]
    }

    // 清空栈
    clear() {
        this.items = []
    }

    // 栈的大小
    size() {
        return this.items.length
    }

    // 栈是否为空
    isEmpty() {
        return this.items.length === 0
    }
}

class PriorityQueue {
    constructor(compare) {

        if (typeof compare !== 'function') {
            throw new Error('compare function required!')
        }

        this.data = []
        this.compare = compare

    }

    //二分查找 寻找插入位置
    search(target) {
        let low = 0, high = this.data.length
        while (low < high) {
            let mid = low + ((high - low) >> 1)
            if (this.compare(this.data[mid], target) > 0) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low;
    }

    //添加
    add(elem) {
        let index = this.search(elem)
        this.data.splice(index, 0, elem)
        return this.data.length
    }

    //取出最优元素
    poll() {
        return this.data.pop()
    }

    //查看最优元素
    peek() {
        return this.data[this.data.length - 1];
    }
}

// function

var openTable = new PriorityQueue((B, A) => ((A.value + A.depth) - (B.value + B.depth)))
var closeTable = new Stack()

Path = new Stack();
var num = 9

var count1 = 0;
var count2 = 0;

function Judge(S, G) {

    S.parent = null;
    S.value = 0;
    S.depth = 0;

    G.parent = null;
    G.value = 0;
    G.depth = 0;

    // System.out.println("请输入初始状态");
    // 0 1 2 3 4 5 6 7 8

    // 1 2 0 3 4 5 6 7 8
    // S.state[0] = 0
    // S.state[1] = 1
    // S.state[2] = 2
    // S.state[3] = 3
    // S.state[4] = 4
    // S.state[5] = 5
    // S.state[6] = 6
    // S.state[7] = 7
    // S.state[8] = 8
    //
    // G.state[0] = 1
    // G.state[1] = 2
    // G.state[2] = 0
    // G.state[3] = 3
    // G.state[4] = 4
    // G.state[5] = 5
    // G.state[6] = 6
    // G.state[7] = 7
    // G.state[8] = 8

    return 0;
}

function equal(S, G)  //判断两个方阵是否相等。
{
    for (let i = 0; i <= 8; i++) {
        if (S.state[i] != G.state[i]) {
            return false;
        }
    }
    return true;
}

function value(A, G)//  计算每个数字当前状态与最终状态的曼哈顿距离 之和作为代价
{

    //count记录所有棋子移动到正确位置需要的步数
    let count = 0;

    let begin = new Array(3);
    let end = new Array(3);
    for (let i = 0; i < begin.length; i++) {
        begin[i] = new Array(3)
        end[i] = new Array(3)
    }
    //将一维数组的值转赋值给二维数组
    for (let i = 0; i < begin.length; i++) {
        for (let j = 0; j < begin[i].length; j++) {
            begin[i][j] = A.state[3 * i + j];
            end[i][j] = G.state[3 * i + j];
        }
    }

    for (let i = 0; i < 3; i++)   //检查当前图形的正确度
        for (let j = 0; j < 3; j++) {
            if (begin[i][j] != end[i][j]) {
                for (let k = 0; k < 3; k++) for (let w = 0; w < 3; w++) if (begin[i][j] == end[k][w]) count = (count + Math.abs(i - k * 1.0) + Math.abs(j - w * 1.0)); //累加计算每个数字当前状态与最终状态的曼哈顿距离
            } else {
                continue;
            }
        }

    return count + A.depth;   //返回估计值
}

function createNode(S, G) {
    /* 计算原状态下,空格所在的行列数，从而判断空格可以往哪个方向移动 */
    let blank; //定义0的下标
    for (blank = 0; blank < 9 && S.state[blank] != 0; blank++) ;//找到0的位置
    let x = Math.floor(blank / 3), y = blank % 3; //获取0所在行列编号
    for (let d = 0; d < 4; d++) //找到S扩展的子节点，加入open表中
    {
        let newX = x, newY = y;//

        tempNode = new Node();

        /*移动数字0*/
        if (d == 0) newX = x - 1;  //向左
        if (d == 1) newY = y - 1;  //向下
        if (d == 2) newX = x + 1;   //向右
        if (d == 3) newY = y + 1;   //向上

        let newBlank = newX * 3 + newY; //0新的位置

        if (newX >= 0 && newX < 3 && newY >= 0 && newY < 3) //如果移动合法
        {
            /* 交换格子的内容*/
            for (let i = 0; i < S.state.length; i++) {
                tempNode.state[i] = S.state[i];
            }
            //                tempNode = (Node)S.clone();

            // 将 0 和 要与 0 交换的那个值 进行交换
            tempNode.state[blank] = S.state[newBlank];
            tempNode.state[newBlank] = 0;

            if (S.parent != null && (S.parent).state[newBlank] == 0) //如果新节点和爷爷节点一样，舍弃该节点
                continue;

            /* 把子节点都加入open表中 */
            tempNode.parent = S;
            tempNode.value = value(tempNode, G);
            tempNode.depth = S.depth + 1;
            openTable.add(tempNode);
        }
    }
}


function main(star, end) {

    IsFind = false

    Path.clear()

    let time1 = new Date().getTime()

    S0 = new Node();
    Sg = new Node();

    for (let i = 0; i < star.length; i++) {
        S0.state[i] = star[i]
        Sg.state[i] = end[i]
    }

    // S0.state[0] = 0
    // S0.state[1] = 1
    // S0.state[2] = 2
    // S0.state[3] = 3
    // S0.state[4] = 4
    // S0.state[5] = 5
    // S0.state[6] = 6
    // S0.state[7] = 7
    // S0.state[8] = 8
    //
    // Sg.state[0] = 1
    // Sg.state[1] = 2
    // Sg.state[2] = 0
    // Sg.state[3] = 3
    // Sg.state[4] = 4
    // Sg.state[5] = 5
    // Sg.state[6] = 6
    // Sg.state[7] = 7
    // Sg.state[8] = 8

    Judge(S0, Sg);

    openTable.add(S0);

    while (true) {

        // 获取 open 表中最小的 那个值 也就是 第一个元素
        // 加入到 close 表中 之后 弹出去
        // console.log(openTable.peek())
        closeTable.add(openTable.peek());

        openTable.poll();

        if (equal(closeTable.peek(), Sg) == false) {
            createNode(closeTable.peek(), Sg);
        } else {
            IsFind = true
            break;
        }
    }

    // console.log("star")

    //临时变量暂存队前数据
    tempNode = closeTable.peek();  //back  返回队列的最后一个元素即最后入队的元素

    while (tempNode.parent != null) {
        Path.add(tempNode);//入栈
        tempNode = (tempNode.parent);//指向父节点
    }

    Path.add(tempNode);

    // console.log(Path.size())

    // /* 输出方案 */
    // while (Path.size() != 0) {
    //     // console.log(Path.peek().state)
    //     // for (let i = 0; i <= 8; i++) {
    //     // console.log(Path.peek().state[i] + " ")
    //     // if ((i + 1) % 3 == 0)
    //     //   console.log()
    //     // // System.out.print(Path.peek().state[i] + " ");
    //     // // if ((i + 1) % 3 == 0)
    //     // //   System.out.println();
    //     // }
    //     Path.pop();
    // }


    let time2 = new Date().getTime()

    let time = time2 - time1

    let obg = {
        time: time, Path,IsFind
    }

    console.log(obg)

    return obg;
}


// main()

