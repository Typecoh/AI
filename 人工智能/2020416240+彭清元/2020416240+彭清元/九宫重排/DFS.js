/**
 * 深度搜搜
 */


// 创建一个 3 * 3 的 迷宫
count = 0;
// 创建一个 开始状态
star = []
// 创建一个 结束状态
end = []
// 上下左右四个状态移动
dp = []
// 将初始状态 和 终止状态 加入
starString = "";
// 将初始状态 和 终止状态 加入
endString = "";

IsFind = false;

ansString = []

/**
 * 实现hashMap
 */
function HashMap() {
    //定义长度
    var length = 0;
    //创建一个对象
    var obj = new Object();

    /**
     * 判断Map是否为空
     */
    this.isEmpty = function () {
        return length == 0;
    };

    /**
     * 判断对象中是否包含给定Key
     */
    this.containsKey = function (key) {
        return (key in obj);
    };

    /**
     * 判断对象中是否包含给定的Value
     */
    this.containsValue = function (value) {
        for (var key in obj) {
            if (obj[key] == value) {
                return true;
            }
        }
        return false;
    };

    /**
     *向map中添加数据
     */
    this.put = function (key, value) {
        if (!this.containsKey(key)) {
            length++;
        }
        obj[key] = value;
    };

    /**
     * 根据给定的Key获得Value
     */
    this.get = function (key) {
        return this.containsKey(key) ? obj[key] : null;
    };

    /**
     * 根据给定的Key删除一个值
     */
    this.remove = function (key) {
        if (this.containsKey(key) && (delete obj[key])) {
            length--;
        }
    };

    /**
     * 获得Map中的所有Value
     */
    this.values = function () {
        var _values = new Array();
        for (var key in obj) {
            _values.push(obj[key]);
        }
        return _values;
    };

    /**
     * 获得Map中的所有Key
     */
    this.keySet = function () {
        var _keys = new Array();
        for (var key in obj) {
            _keys.push(key);
        }
        return _keys;
    };

    /**
     * 获得Map的长度
     */
    this.size = function () {
        return length;
    };

    /**
     * 清空Map
     */
    this.clear = function () {
        length = 0;
        obj = new Object();
    };
}

map = new HashMap();

function DFS(x, y, arr) {

    if (IsFind == true) return;

    count++;

    s = ""

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr[i].length; j++) {
            s += arr[i][j];
        }
    }
    // 到达了 终点
    if (s == endString) {

        map.put(s, 1);
        ansString.push(s)
        console.log("over");

        IsFind = true;

        return;
    }

    // 如果走过 就 行不通
    if (map.containsKey(s) == true) {

        console.log("访问过");
        return;
    }

    map.put(s, 1);
    ansString.push(s)

    let Mapsize = map.size()

    temp = arr;

    for (let i = 0; i <= 3; i++) {

        state = dp[i];

        let newx = x + state[0];
        let newy = y + state[1];

        // console.log(newx + " " + newy);

        if (newx <= 2 && newx >= 0 && newy >= 0 && newy <= 2) {

            let value = temp[x][y];

            temp[x][y] = temp[newx][newy];

            temp[newx][newy] = value;

            t = "";

            for (let a = 0; a < temp.length; a++) {
                for (let b = 0; b < temp[a].length; b++) {
                    t += temp[a][b] + "";
                }
            }

            if (map.containsKey(t) == false) {

                DFS(newx, newy, temp);
                // 将数据恢复

                let v = temp[newx][newy];

                temp[newx][newy] = temp[x][y];

                temp[x][y] = v;

                // console.log("diyici");
            } else {

                let v = temp[newx][newy];

                temp[newx][newy] = temp[x][y];

                temp[x][y] = v;

                continue;
            }
        }
    }
}

function UnibformedSearch() {
    let x = 0;
    let y = 0;

    // 将初始状态加入到 map中
    for (let i = 0; i < star.length; i++) {
        for (let j = 0; j < star[i].length; j++) {
            if (star[i][j] == 0) {
                x = i;
                y = j;
                break;
            }
        }
    }
    try {
        DFS(x, y, star);
    } catch (e) {
        console.log(e)
    }

}

function main2(starNumber, endNumber) {

    // 创建一个 3 * 3 的 迷宫
    count = 0;
// 创建一个 开始状态
    star = []
// 创建一个 结束状态
    end = []
// 上下左右四个状态移动
    dp = []
// 将初始状态 和 终止状态 加入
    starString = "";
// 将初始状态 和 终止状态 加入
    endString = "";

    map.clear()

    IsFind = false;

    ansString = []

    let time1 = new Date().getTime()
    // 初始状态
    star = new Array(3);
    // 结束状态
    end = new Array(3);
    // 位置偏移
    dp = new Array(4);

    /**
     * 创建对应的数据组
     */
    for (let i = 0; i < star.length; i++) {
        star[i] = new Array(3)
        end[i] = new Array(3)
    }

    for (let i = 0; i < 4; i++) {
        dp[i] = new Array(2)
    }

    /**
     * 数值初始化
     */
    for (let i = 0; i < star.length; i++) {
        for (let j = 0; j < star[i].length; j++) {
            star[i][j] = starNumber[3 * i + j]
            end[i][j] = endNumber[3 * i + j]
        }
    }

    dp[0][0] = 0
    dp[0][1] = -1

    dp[1][0] = 0
    dp[1][1] = 1

    dp[2][0] = -1
    dp[2][1] = 0


    dp[3][0] = 1
    dp[3][1] = 0


    // 将终止状态加入到 map中
    for (let i = 0; i < end.length; i++) {
        for (let j = 0; j < end[i].length; j++) {
            endString += end[i][j] + "";
        }
    }

    // 使用 盲目搜索 进行 搜索展示
    UnibformedSearch();

    let time2 = new Date().getTime()
    let time = time2 - time1

    let obg = {
        time,
        ansString,
        IsFind
    }
    return obg

    return ansString

}


try { DFS(x, y, star); } catch (e) { console.log(e) }
