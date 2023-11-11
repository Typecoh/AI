list = {}
Type = []
Director = []
Starring = []
Release = []
screenwriter = []
producer = []
firm = []
FilmingLocations = []
name = []
alias = []


async function getData() {

    /**
     * 将数据从json文件中获取出来
     * @type {*}
     */
    list = await axios.get("config.json")

    return list.data
}

async function init() {

    let data = await axios.get("data1.json")

    /**
     * 数据集的相关属性
     * @type {*|string[]}
     */
    Type = data.data.Types.split(" ")
    Director = data.data.Director.split(" ")
    Starring = data.data.Starring.split(" ")
    Release = data.data.Release.split(" ")
    screenwriter = data.data.screenwriter.split(" ")
    producer = data.data.producer.split(" ")
    alias = data.data.alias.split(" ")
    reads = data.data.reads.split(" ")
    discovers = data.data.discovers.split(" ")
    Info = data.data.Info.split(" ")
}

/**
 * 《芸汐传》是由林健龙 刘镇明导演的一部国产剧，
 * 芸汐传在大陆首映，
 * 并在2018第一时间上映，
 * 主要演员有鞠婧祎 张哲瀚 米热 林思意 王佑硕 卢星宇 许佳 等主演，
 * 樱花动漫为大家提供芸汐传全集完整版免费在线观看，
 * 支持手机、平板、电脑多终端高清免费播放，
 * 芸汐传现更新至已完结。
 * @param string
 * @constructor
 */

function Process1(string) {

    console.log(string)

    let str = string.split("，")

    /**
     * 判断 导演
     */

    Dir = []
    Sta = []
    Rel = []
    nam = []
    scr = []
    Tys = []


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Director.length; j++) {
            if (str[i].indexOf(Director[j]) != -1) {
                Dir.push(str[i].substring(str[i].indexOf("是由") + 2, str[i].indexOf("导演")).trim().split(" "))
            }
        }
    }

    let temp = []

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Starring.length; j++) {
            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "主要演员") {
                temp.push(str[i].substring(str[i].indexOf("主要演员有") + 5, str[i].indexOf("等")).trim().split(" "))
            }
        }
    }

    console.log(temp)
    for (let i = 0; i < temp.length; i++) Sta.push(...temp[i])


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Release.length; j++) {
            if (str[i].indexOf(Release[j]) != -1) {
                Rel.push(str[i].substring(str[i].indexOf("在") + 1, str[i].indexOf("第一时间")))
            }
        }
    }


    for (let i = 0; i < str.length; i++) {
        if (str[i].indexOf("是") != -1) {
            console.log(str[i].indexOf("是"))
            nam.push(str[i].substring(0, str[i].indexOf("是")))
        }
    }


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < screenwriter.length; j++) {
            if (str[i].indexOf(screenwriter[j]) != -1) {
                console.log(screenwriter[j])
                scr.push(str[i].substring(str[i].indexOf(",") + 1, str[i].indexOf("编剧")).trim().split(" "))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Type.length; j++) {
            if (str[i].indexOf(Type[j]) != -1) {
                console.log(Type[j])
                Tys.push(Type[j])
            }
        }
    }

    let obj = {
        导演: Dir == null ? "" : Dir,
        主演: Sta == null ? "" : Sta,
        发布时间: Rel == null ? "" : Rel,
        名称: nam == null ? "" : nam,
    }

    return obj;
}

function Process2(string) {

    console.log(string)

    let str = string.split("，")

    /**
     * 判断 导演
     */

    Dir = []
    Sta = []
    Rel = []
    nam = []
    scr = []
    Tys = []
    pro = []
    al = []


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Director.length; j++) {
            if (str[i].indexOf(Director[j]) != -1) {
                Dir.push(str[i].substring(0, str[i].indexOf("执导")).trim().split("、"))
            }
        }
    }

    let temp = []

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Starring.length; j++) {
            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "领衔主演") {
                temp.push(str[i].substring(0, str[i].indexOf("领衔主演")).trim().split(" "))
            }

            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "联袂主演") {
                temp.push(str[i].substring(0, str[i].indexOf("等")).trim().split("、"))
            }
        }
    }

    for (let i = 0; i < temp.length; i++) Sta.push(...temp[i])

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Release.length; j++) {
            if (str[i].indexOf(Release[j]) != -1) {
                Rel.push(str[i].substring(str[i].indexOf("于") + 1, str[i].indexOf("日") + 1))
            }
        }
    }


    for (let i = 0; i < str.length; i++) {
        if (str[i].indexOf("是") != -1) {
            // console.log(str[i].indexOf("是"))
            nam.push(str[i].substring(0, str[i].indexOf("是")))
        }
    }


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < screenwriter.length; j++) {
            if (str[i].indexOf(screenwriter[j]) != -1) {
                scr.push(str[i].substring(0, str[i].indexOf("编剧")))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < producer.length; j++) {
            if (str[i].indexOf(producer[j]) != -1) {
                pro.push(str[i].substring(str[i].indexOf("是由") + 2, str[i].indexOf("监制")))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Type.length; j++) {
            if (str[i].indexOf(Type[j]) != -1) {
                console.log(Type[j])
                Tys.push(Type[j])
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < alias.length; j++) {
            if (str[i].indexOf(alias[j]) != -1) {
                al.push(str[i].substring(str[i].indexOf("《"), str[i].indexOf("》") + 1))
            }
        }
    }


    let obj = {
        导演: Dir == null ? "" : Dir,
        主演: Sta == null ? "" : Sta,
        发布时间: Rel == null ? "" : Rel,
        名称: nam == null ? "" : nam,
        编剧: scr == null ? "" : scr,
        类型: Tys == null ? "" : Tys,
        监制: pro == null ? "" : pro,
        别名: al == null ? "" : al
    }

    return obj;
}

function Process3(string) {

    let str = string.trim().split(/,|，|。|\s+/)

    console.log(str)

    /**
     * 判断 导演
     */

    Dir = []
    Sta = []
    Rel = []
    nam = []
    scr = []
    Tys = []
    pro = []
    al = []
    rea = []
    dis = []


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Director.length; j++) {
            if (str[i].indexOf(Director[j]) != -1) {
                Dir.push(str[i].substring(0, str[i].indexOf("联合执导")).trim().split("、"))
            }
        }
    }

    let temp = []

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Starring.length; j++) {
            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "领衔主演") {
                temp.push(str[i].substring(0, str[i].indexOf("等领衔主演")).trim().split("、"))
            }

            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "联袂主演") {
                temp.push(str[i].substring(0, str[i].indexOf("等")).trim().split("、"))
            }
        }
    }

    for (let i = 0; i < temp.length; i++) Sta.push(...temp[i])

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Release.length; j++) {
            if (str[i].indexOf(Release[j]) != -1) {
                // console.log(str[i])
                Rel.push(str[i].substring(str[i].indexOf("于") + 1, str[i].indexOf("日") + 1))
            }
        }
    }


    for (let i = 0; i < str.length; i++) {
        if (str[i].indexOf("是") != -1) {
            // console.log(str[i].indexOf("是"))
            nam.push(str[i].substring(0, str[i].indexOf("是")))
        }
    }


    // for (let i = 0; i < str.length; i++) {
    //     for (let j = 0; j < screenwriter.length; j++) {
    //         if (str[i].indexOf(screenwriter[j]) != -1) {
    //             scr.push(str[i].substring(0, str[i].indexOf("编剧")))
    //         }
    //     }
    // }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < producer.length; j++) {
            if (str[i].indexOf(producer[j]) != -1) {
                pro.push(str[i].substring(str[i].indexOf("，"), str[i].indexOf("监制")))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Type.length; j++) {
            if (str[i].indexOf(Type[j]) != -1) {
                // console.log(Type[j])
                Tys.push(Type[j])
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < alias.length; j++) {
            if (str[i].indexOf(alias[j]) != -1) {
                al.push(str[i].substring(str[i].indexOf("《"), str[i].indexOf("》") + 1))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < reads.length; j++) {
            if (str[i].indexOf(reads[j]) != -1) {
                rea.push(str[i].substring(str[i].indexOf("阅读量") + 3))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < discovers.length; j++) {
            if (str[i].indexOf(discovers[j]) != -1) {
                dis.push(str[i].substring(str[i].indexOf("讨论量达") + 4))
            }
        }
    }


    let obj = {
        导演: Dir == null ? "" : Dir,
        主演: Sta == null ? "" : Sta,
        发布时间: Rel == null ? "" : Rel,
        名称: nam == null ? "" : nam, // "编剧": scr == null ? "" : scr,
        类型: Tys == null ? "" : Tys,
        监制: pro == null ? "" : pro,
        别名: al == null ? "" : al,
        阅读量: rea == null ? "" : rea,
        讨论量: dis == null ? "" : dis

    }
    return obj;
}

function Process4(string) {


    let str = string.split("，")

    // console.log(str)
    /**
     * 判断 导演
     */

    Dir = []
    Sta = []
    Rel = []
    nam = []
    scr = []
    Tys = []
    pro = []
    al = []
    rea = []
    dis = []
    info = []


    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Director.length; j++) {
            if (str[i].indexOf(Director[j]) != -1) {
                Dir.push(str[i].substring(0, str[i].indexOf("联合执导")).trim().split("、"))
            }
        }
    }

    let temp = []

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Starring.length; j++) {
            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "领衔主演") {
                temp.push(str[i].substring(0, str[i].indexOf("等领衔主演")).trim().split("、"))
            }

            if (str[i].indexOf(Starring[j]) != -1 && Starring[j] == "联袂主演") {
                temp.push(str[i].substring(0, str[i].indexOf("等")).trim().split("、"))
            }
        }
    }

    for (let i = 0; i < temp.length; i++) Sta.push(...temp[i])

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Release.length; j++) {
            if (str[i].indexOf(Release[j]) != -1) {
                // console.log(str[i])
                Rel.push(str[i].substring(str[i].indexOf("于") + 1, str[i].indexOf("日") + 1))
            }
        }
    }


    for (let i = 0; i < str.length; i++) {
        if (str[i].indexOf("是") != -1) {
            // console.log(str[i].indexOf("是"))
            nam.push(str[i].substring(0, str[i].indexOf("是")))
        }
    }


    // for (let i = 0; i < str.length; i++) {
    //     for (let j = 0; j < screenwriter.length; j++) {
    //         if (str[i].indexOf(screenwriter[j]) != -1) {
    //             scr.push(str[i].substring(0, str[i].indexOf("编剧")))
    //         }
    //     }
    // }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < producer.length; j++) {
            if (str[i].indexOf(producer[j]) != -1) {
                pro.push(str[i].substring(str[i].indexOf("，"), str[i].indexOf("监制")))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < Type.length; j++) {
            if (str[i].indexOf(Type[j]) != -1) {
                // console.log(Type[j])
                Tys.push(Type[j])
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < alias.length; j++) {
            if (str[i].indexOf(alias[j]) != -1) {
                let tempstr = str[i].substring(str[i].indexOf("改编") + 2)
                al.push(tempstr.substring(tempstr.indexOf("《"), tempstr.indexOf("》") + 1))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < reads.length; j++) {
            if (str[i].indexOf(reads[j]) != -1) {
                rea.push(str[i].substring(str[i].indexOf("阅读量") + 3))
            }
        }
    }

    for (let i = 0; i < str.length; i++) {
        for (let j = 0; j < discovers.length; j++) {
            if (str[i].indexOf(discovers[j]) != -1) {
                dis.push(str[i].substring(str[i].indexOf("讨论量达") + 4))
            }
        }
    }

    // for (let i = 0; i < str.length; i++) {
    //     for (let j = 0; j < Info.length; j++) {
    //         if (string.indexOf(Info[j]) != -1) {
    //             info.push(string.substring(str[i].indexOf("讲述了") + 3))
    //         }
    //     }
    // }
    //

    for (let j = 0; j < Info.length; j++) {
        if (string.indexOf(Info[j]) != -1) {
            let tString = string.substring(string.indexOf("讲述了") + 3, string.indexOf("。"))
            info.push(tString)
        }
    }


    let obj = {
        名称: nam == null ? "" : nam, // "编剧": scr == null ? "" : scr,
        别名: al == null ? "" : al,
        简介: info == null ? "" : info,
    }

    return obj;
}

function merge(string1, string2, string3, string4) {

    Dir = []
    Sta = []
    Rel = []
    nam = []
    scr = []
    Tys = []
    pro = []
    al = []
    rea = []
    dis = []
    info = []

    let obj = {
        导演: Dir, 主演: Sta, 发布时间: Rel, 名称: nam, 编剧: scr, 类型: Tys, 监制: pro, 别名: al, 阅读量: rea, 讨论量: dis, 简介: info,
    }

    for (item in obj) {

        for (it in string1) {
            if (it == item) {
                obj[item].push(...string1[it])
            }
        }

        for (it in string2) {
            if (it == item) {
                obj[item].push(...string2[it])
            }
        }

        for (it in string3) {
            if (it == item) {
                obj[item].push(...string3[it])
            }
        }

        for (it in string4) {
            if (it == item) {
                obj[item].push(...string4[it])
            }
        }
    }

    let arr = {};
    Dir.forEach(item => arr[item] = item);
    Dir = Object.values(arr);

    temp = Dir
    Dir = []

    for (let i = 0; i < temp.length; i++) Dir.push(...temp[i])


    arr = {};
    Sta.forEach(item => arr[item] = item);
    Sta = Object.values(arr);

    arr = {};
    Rel.forEach(item => arr[item] = item);
    Rel = Object.values(arr);

    arr = {};
    nam.forEach(item => arr[item] = item);
    nam = Object.values(arr);

    arr = {};
    scr.forEach(item => arr[item] = item);
    scr = Object.values(arr);

    arr = {};
    Tys.forEach(item => arr[item] = item);
    Tys = Object.values(arr);

    arr = {};
    pro.forEach(item => arr[item] = item);
    pro = Object.values(arr);

    arr = {};
    al.forEach(item => arr[item] = item);
    al = Object.values(arr);

    arr = {};
    rea.forEach(item => arr[item] = item);
    rea = Object.values(arr);

    arr = {};
    dis.forEach(item => arr[item] = item);
    dis = Object.values(arr);

    arr = {};
    info.forEach(item => arr[item] = item);
    info = Object.values(arr);


    obj.导演 = Dir
    obj.主演 = Sta
    obj.发布时间 = Rel
    obj.名称 = nam
    obj.别名 = al
    obj.监制 = pro
    obj.编剧 = scr
    obj.简介 = info
    obj.讨论量 = dis
    obj.阅读量 = rea
    obj.类型 = Tys

    return obj
}

init()