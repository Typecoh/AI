/**
 * 将 样本从文本中读取出来 转化成 Json格式 存入 Json文件中
 * @type {{}}
 */

var yangben = {}
index = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}

const fs = require("fs")
const {writeFile} = require("fs");

function WriteData(number, path) {
    fs.readFile(path, 'utf8', (err, data) => {
        if (err) console.log('读取失败')
        else {
            yangben[index[number]] = {
                message: data
            }

            let len = Object.keys(yangben).length
            if (len == 4) {
                // console.log(yangben)
                const palce = './config.json';
                writeFile(palce, JSON.stringify(yangben, null), (error) => {
                    if (error) {
                        console.log('An error has occurred ', error);
                        return;
                    }
                    console.log('Data written successfully to disk');
                });
            }
        }
    })
}

function SendData() {
    for (let i = 1; i <= 4; i++) {
        WriteData(i, `样本${i}.md`)
    }
}

SendData()


