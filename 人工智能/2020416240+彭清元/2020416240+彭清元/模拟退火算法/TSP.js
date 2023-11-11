    // 定义城市坐标数组
    var cities = [
        // [60, 200],
        // [180, 200],
        // [80, 180],
        // [140, 180],
        // [20, 160],
        // [100, 160],
        // [200, 160],
        // [140, 140],
        // [40, 120],
        // [100, 120],
        // [180, 100],
        // [60, 80],
        // [120, 80],
        // [180, 60],
        // [20, 40],
        // [100, 40],
        // [200, 40],
        // [20, 20],
        // [60, 20],
        // [160, 20]
    ];

    // 计算两个城市之间的距离（欧氏距离）
    function getDistance(city1, city2) {
        var xDistance = Math.abs(city1[0] - city2[0]);
        var yDistance = Math.abs(city1[1] - city2[1]);
        return Math.sqrt(xDistance * xDistance + yDistance * yDistance);
    }

    // 计算当前路径的总长度
    function getPathLength(path) {
        var length = 0;
        for (var i = 0; i < path.length - 1; i++) {
            length += getDistance(cities[path[i]], cities[path[i + 1]]);
        }
        return length;
    }

    // 随机生成一个有效路径
    function generatePath(numCities) {
        var path = [];
        for (var i = 0; i < numCities; i++) {
            path.push(i);
        }
        for (var i = 0; i < numCities - 1; i++) {
            var j = Math.floor(Math.random() * (numCities - i)) + i;
            var temp = path[i];
            path[i] = path[j];
            path[j] = temp;
        }
        return path;
    }

    // 模拟退火算法
    function simulatedAnnealing(numCities, iterations, temperature, coolingRate) {
        var currentPath = generatePath(numCities);
        var currentLength = getPathLength(currentPath);
        var bestPath = currentPath.slice();
        var bestLength = currentLength;

        for (var i = 0; i < iterations; i++) {
            var newPath = currentPath.slice();

            // 随机交换两个城市的位置
            var j = Math.floor(Math.random() * numCities);
            var k = Math.floor(Math.random() * numCities);
            var temp = newPath[j];
            newPath[j] = newPath[k];
            newPath[k] = temp;

            var newLength = getPathLength(newPath);
            var delta = newLength - currentLength;

            if (delta < 0 || Math.exp(-delta / temperature) > Math.random()) {
                currentPath = newPath;
                currentLength = newLength;
                if (currentLength < bestLength) {
                    bestPath = currentPath.slice();
                    bestLength = currentLength;
                }
            }

            temperature *= coolingRate;
        }

        return {path: bestPath, length: bestLength};
    }

    // // 调用模拟退火算法求解TSP问题
    // var result = simulatedAnnealing(cities.length, 100000, 10000, 0.99);
    //
    // console.log(result.path); // 输出最优路径
    // console.log(result.length); // 输出最优路径的长度

    function main3(arr,iterations,temperature,coolingRate) {
        // console.log(cities)
        // console.log(arr)
        cities = []
        for (let i = 0; i < arr.length; i++) {

            let array = [];
            array.push(parseInt(arr[i][0]))
            array.push(parseInt(arr[i][1]))
            cities.push(array)
        }

        // 调用模拟退火算法求解TSP问题
        // var result = simulatedAnnealing(cities.length, 100000, 10000, 0.99);
        var result = simulatedAnnealing(cities.length, iterations, temperature, coolingRate);

        // console.log(result.path); // 输出最优路径
        // console.log(result.length); // 输出最优路径的长度

        return result;
    }
