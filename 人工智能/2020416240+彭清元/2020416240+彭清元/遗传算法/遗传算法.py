import numpy as np
import math

"""
导入数据，得到城市坐标信息
:param data_path: 数据文件地址 str
:return: 所有城市的坐标信息 二维 list
"""
def load_data(data_path):
    cities = []
    with open(data_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            x_str, y_str = line.split()[1:]
            x, y = int(x_str), int(y_str)
            cities.append((x, y))
    return cities


"""
计算两两城市的距离
:param cities: 所有城市的坐标 二维 list
:return: 城市距离矩阵 numpy数组
"""


def get_cities_distance(cities):
    dist_matrix = np.zeros((127, 127))  # 根据数据的长度来界定---127*127
    n_cities = len(cities)
    for i in range(n_cities - 1):
        for j in range(i + 1, n_cities):
            dist = get_two_cities_dist(cities[i], cities[j])  # 勾股定理求距离
            dist_matrix[i, j] = dist  # 城市i到城市j的距离
            dist_matrix[j, i] = dist
    return dist_matrix


"""
计算两个城市的距离
:param city1: 第一个城市 长度为2的list
:param city2: 第二个城市 长度为2的list
:return: 两城市的距离 double
"""


def get_two_cities_dist(city1, city2):
    x_1, y_1 = city1
    x_2, y_2 = city2
    return math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))


"""
计算某一路线的适应度
:param route: 路线 长度为城市个数的 ndarray
:param dist_matrix: 距离矩阵 ndarray
:return: 路线的适应度 double
"""


def get_route_fitness_value(route, dist_matrix):
    dist_sum = 0

    for i in range(len(route) - 1):
        dist_sum += dist_matrix[route[i], route[i + 1]]  # $$$$$对于一条路线的计算，此时的route为routes[i]

    dist_sum += dist_matrix[route[len(route) - 1], route[0]]  # 由于循环的局限性此处累加单拿出来

    return 1 / dist_sum  # 越短越好，自然选择用倒数


"""
计算所有路线的适应度
:param routes: 所有路线 ndarray
:param dist_matrix: 距离矩阵 ndarray
:return: 所有路线的适应度 ndarray
"""


def get_all_routes_fitness_value(routes, dist_matrix):
    fitness_values = np.zeros(len(routes))
    for i in range(len(routes)):
        f_value = get_route_fitness_value(routes[i], dist_matrix)  # 传入一系列数
        fitness_values[i] = f_value
    return fitness_values



"""
随机初始化路线
:param n_route: 初始化的路线数量 int
:param n_cities: 城市的数量 int
:return: 路线矩阵 二维ndarray
"""

#  随意  指定了 n_route 条路经 作为一个 初始化 值
def init_route(n_route, n_cities):
    routes = np.zeros((n_route, n_cities)).astype(int)
    for i in range(n_route):
        # 选择 n_route 条路径， 每一次选择 n_cities 中选择一个
        # np.random.choice 从 n_cities 当中 选取 size 个  范围是 n_cities 的 数据 ==》 返回的也就是一个一维数组
        routes[i] = np.random.choice(range(n_cities), size=n_cities, replace=False)
    return routes

"""
选择操作
:param routes: 所有路线 ndarray
:param fitness_values: 所有路线的适应度 ndarray
:return: 选择后的所有路线 ndarray
"""


def selection(routes, fitness_values):
    selected_routes = np.zeros(routes.shape).astype(int)
    probability = fitness_values / np.sum(fitness_values)
    n_routes = routes.shape[0]
    for i in range(n_routes):
        choice = np.random.choice(range(n_routes), p=probability)  # 概率越大，取值次数越多
        selected_routes[i] = routes[choice]
    return selected_routes


"""
交叉操作
:param routes: 所有路线 ndarray
:param n_cities: 城市数量 int
:return: 交叉后的所有路线 ndarray
"""


# in1d函数会返回布尔值。若表二的元素在比表一有的话，则会返回对值；是单个元素的判断

# 利用了numpy的特性，选出交叉值的列表，插入到对应值的列表，在合成

def crossover(routes, n_cities):
    for i in range(0, len(routes), 2):
        r1_new, r2_new = np.zeros(n_cities), np.zeros(n_cities)

        seg_point = np.random.randint(0, n_cities)
        cross_len = n_cities - seg_point

        r1, r2 = routes[i], routes[i + 1]
        r1_cross, r2_cross = r2[seg_point:], r1[seg_point:]

        r1_non_cross = r1[np.in1d(r1, r1_cross) == False]
        r2_non_cross = r2[np.in1d(r2, r2_cross) == False]

        r1_new[:cross_len], r2_new[:cross_len] = r1_cross, r2_cross
        r1_new[cross_len:], r2_new[cross_len:] = r1_non_cross, r2_non_cross

        routes[i], routes[i + 1] = r1_new, r2_new
    return routes


"""
变异操作，变异概率为 0.01
:param routes: 所有路线 ndarray
:param n_cities: 城市数量 int
:return: 变异后的所有路线 ndarray
"""


def mutation(routes, n_cities):
    prob = 0.01
    p_rand = np.random.rand(len(routes))  # 此处的长度的计算返回列表的行数
    # 此处的随机数是生成的01之间的小数，长度为1000
    for i in range(len(routes)):
        if p_rand[i] < prob:
            mut_position = np.random.choice(range(n_cities), size=2, replace=False)
            # 随机抽取不重复的两个数交换
            l, r = mut_position[0], mut_position[1]
            routes[i, l], routes[i, r] = routes[i, r], routes[i, l]
    return routes


if __name__ == '__main__':

    n_routes = 100  # 路线
    epoch = 100000  # 迭代次数
    prob = 0.01 # 变异的概率

    cities = load_data('cities.txt')  # 导入数据

    # 计算城市距离矩阵
    dist_matrix = get_cities_distance(cities)

    # 初始化所有路线 routes[0] 表示了第一种随机的127城市之间的路线 routes[0][0]的内容才表示一个城市
    routes = init_route(n_routes, dist_matrix.shape[0])

    # 计算所有初始路线的适应度 适应度与路线是一一对应的
    fitness_values = get_all_routes_fitness_value(routes, dist_matrix)

    # 用于返回数组的最大值的索引---倒数最大值自然路线最短
    best_index = fitness_values.argmax()

    # 保存最优路线及其适应度 -- 保存最优路线，保存最大适应度
    best_route, best_fitness = routes[best_index], fitness_values[best_index]

    # 开始迭代
    not_improve_time = 0
    for i in range(epoch):
        routes = selection(routes, fitness_values)  # 选择

        routes = crossover(routes, len(cities))  # 交叉

        routes = mutation(routes, len(cities))  # 变异

        fitness_values = get_all_routes_fitness_value(routes, dist_matrix)

        best_route_index = fitness_values.argmax()

        if fitness_values[best_route_index] > best_fitness:
            not_improve_time = 0
            best_route, best_fitness = routes[best_route_index], fitness_values[best_route_index]  # 保存最优路线及其适应度
        else:
            not_improve_time += 1

        if (i + 1) % 200 == 0:
            print('count_math: {}, 当前最优路线距离： {}'.format(i + 1, 1 / get_route_fitness_value(best_route, dist_matrix)))
        if not_improve_time >= 2000:
            print('连续2000次迭代都没有改变最优路线，结束迭代')
            break

    print('最优路线为：')
    print(best_route)
    print('总距离为： {}'.format(1 / get_route_fitness_value(best_route, dist_matrix)))

