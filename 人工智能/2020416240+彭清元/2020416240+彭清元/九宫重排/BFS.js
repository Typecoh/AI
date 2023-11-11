/**
 * 创建一些全局变量
 */

ch = []
s = ''
answer = ''
count = 0
set = new Set()

/**
 *     创建一个节点 node
 */
class BFSNode {
    s = '';
    pos = 0;
    swap_num = 0;

    constructor(ss, ppos, num) {
        this.s = ss;
        this.pos = ppos;
        this.swap_num = num;
    }
}

/**
 * 创建一个 交换函数
 * @param x
 * @param y
 */
function swap(x, y) {
    t = ch[x - 1];
    ch[x - 1] = ch[y - 1];
    ch[y - 1] = t;
}

/**
 * 创建一个 Queue
 * @constructor
 */

// 基于数组封装队列类
function Queue() {
    // 属性
    this.items = []

    // 方法
    // 1.add():将元素加入到队列中
    Queue.prototype.add = element => {
        this.items.push(element)
    }

    // 2.pop():从队列中删除前端元素
    Queue.prototype.pop = () => {
        return this.items.shift()
    }

    // 3.poll():查看前端的元素
    Queue.prototype.poll = () => {
        return this.items[0]
    }

    // 4.isEmpty:查看队列是否为空
    Queue.prototype.isEmpty = () => {
        return this.items.length == 0;
    }

    // 5.size():查看队列中元素的个数
    Queue.prototype.size = () => {
        return this.items.length
    }

    // 6.toString():将队列中元素以字符串形式输出
    Queue.prototype.toString = () => {
        let resultString = ''
        for (let i of this.items) {
            resultString += i + ' '
        }
        return resultString
    }
}

/**
 * 使用bfs 进行搜索
 * @param e
 */
function bfs(e) {

    // console.log(e)
    let que = new Queue();

    let iString = ''

    que.add(e)

    let t = null;

    while (!que.isEmpty()) {
        // 查看元素
        t = que.poll();
        // 删除元素
        que.pop()

        ch = t.s.split("");
        count++;

        // console.log("第" + count + "步")

        // console.log(ch)
        // 判断 位置
        // t.pos - 3 表示 空格上面
        if ((t.pos - 3) > 0) {
            swap(t.pos, t.pos - 3);
            // 将字符数组转成 字符串
            iString = ch.join("")
            if (answer === iString) {
                IsFind = true
                set.add(answer)
                count++;
                // console.log("第" + count + "步")
                // console.log(ch)
                return t.swap_num + 1;
            }

            if (!set.has(iString)) {
                set.add(iString);
                que.add(new BFSNode(iString, t.pos - 3, t.swap_num + 1));
            }

            swap(t.pos - 3, t.pos);
        }

        // 检查空格右侧的元素 如果时最右侧的 则 % 3 == 0
        if ((t.pos % 3) != 0) {
            swap(t.pos, t.pos + 1);
            iString = ch.join("")
            if (answer == iString) {
                IsFind = true
                set.add(answer)
                count++;
                // console.log("第" + count + "步")
                // console.log(ch)
                return t.swap_num + 1;
            }
            if (!set.has(iString)) {
                set.add(iString);
                que.add(new BFSNode(iString, t.pos + 1, t.swap_num + 1));
            }
            swap(t.pos + 1, t.pos);
        }

        // 如果是最左侧 现在 的位置 减去 1 就是 上一层 最后的那个元素的位置
        if ((t.pos - 1) % 3 != 0)   //检查空格左侧的元素
        {
            swap(t.pos, t.pos - 1);
            iString = ch.join("")
            if (answer == iString) {
                IsFind = true
                set.add(answer)
                count++;
                // console.log("第" + count + "步")
                // console.log(ch)
                return t.swap_num + 1;
            }
            if (!set.has(iString)) {
                set.add(iString);
                que.add(new BFSNode(iString, t.pos - 1, t.swap_num + 1));
            }
            swap(t.pos - 1, t.pos);
        }

        // t.pos+3<10 表示 不在 最下

        if (t.pos + 3 < 10)       //检查空格下面的元素
        {
            swap(t.pos, t.pos + 3);
            iString = ch.join("")
            if (answer == iString) {
                IsFind = true
                set.add(answer)
                count++;
                // console.log("第" + count + "步")
                // console.log(ch)
                return t.swap_num + 1;
            }
            if (!set.has(iString)) {
                set.add(iString);
                que.add(new BFSNode(iString, t.pos + 3, t.swap_num + 1));
            }
            swap(t.pos + 3, t.pos);
        }
    }
    return -1;
}

/**
 * 主函数
 * @param starNumber
 * @param endNumber
 */
function main1(starNumber, endNumber) {

    let time1 = new Date().getTime()
    ch = []
    s = ''
    answer = ''
    count = 0

    IsFind = false

    let begin = new Array(3);
    let end = new Array(3);
    for (let i = 0; i < begin.length; i++) {
        begin[i] = new Array(3)
        end[i] = new Array(3)
    }

    // console.log("将 初始状态 和 终止状态 进行 赋值")

    for (let i = 0; i < begin.length; i++) {
        for (let j = 0; j < begin[i].length; j++) {
            begin[i][j] = starNumber[3 * i + j]
            s += starNumber[3 * i + j]
            end[i][j] = endNumber[3 * i + j]
            answer += endNumber[3 * i + j]
        }
    }

    // console.log("初始状态是 == > " + s)
    // console.log("结束状态是 == > " + answer)

    n = new BFSNode(s, s.indexOf("0") + 1, 0)
    // console.log(n)
    set.add(s);
    bfs(n);

    let time2 = new Date().getTime()


    let time = time2 - time1

    let obg = {
        time: time,
        set,
        IsFind
    }
    return obg
}

// main1()