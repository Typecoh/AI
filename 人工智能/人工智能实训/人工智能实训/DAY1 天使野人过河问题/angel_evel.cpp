//天使野人过河问题    天使和野人的人数可以任意取 
#include<iostream>
#include <fstream>
#include<stdlib.h>

using namespace std;

struct zt
{
    int lm;//左岸天使数
    int lc;//左岸野人数
    int rm;//右岸天使数
    int rc;//右岸野人数
    int ship;//船的位置，1表示在左岸，0表示在右岸
};
struct zt p, temp[1000]; 

int top = 0;  //有效节点数
int all = 0;  //可走的方案数
int xx[5] = {0,0,1,1,2};
int yy[5] = {1,2,0,1,0};
ofstream outfile;

int IsSafe(zt temp)//判断是否为有效状态，1表示有效，0表示无效 
{
    if((temp.lm>=temp.lc&&temp.rm>=temp.rc&&temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0)||
       (temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0&&temp.lm==0&&temp.rm>=temp.rc)||
       (temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0&&temp.lm>=temp.lc&&temp.rm==0))
    {
        return 1;
    }
    return 0;
}

int pd(int top, zt p)//判断p是否与前面的节点重复，0表示重复，1表示未重复 
{
	for(int i=0;i<top;i++)
    {
        if(temp[i].lm==p.lm&&temp[i].lc==p.lc&&temp[i].rm==p.rm&&temp[i].rc==p.rc&&temp[i].ship==p.ship)
         {
             return 0;
         }
    }

    return 1;
}

//深度优先遍历，初始节点（x，y，0，0，1）， 目标节点（0，0，x，x，-1） 
void dfs(zt p, int lm, int lc)
{
    p.lm = lm;
    p.lc = lc;
	if(p.lc==0&&p.lm==0&&p.rc==temp[0].lc&&p.rm==temp[0].lm)//到达目标节点 
    {
        all++;
		//ofileAgain.open("result.txt",ios::app);
        outfile << "第" << all << "种方案：" << endl;
        outfile << temp[0].lm << ',' << temp[0].lc << ',' << temp[0].rm << ',' << temp[0].rc << ',' << temp[0].ship << endl;
        for(int i = 1; i < top; i++)
        {
            outfile << temp[i].lm << ',' << temp[i].lc << ',' << temp[i].rm << ',' << temp[i].rc << ',' << temp[i].ship << endl;
        }
    }

    for(int i = 0; i < 5; i++)
    {
        int x = xx[i];
        int y = yy[i];

        zt temp1;
        if(p.ship == 1)//船在左岸
        {
            temp1.lm = p.lm-x;
            temp1.lc = p.lc-y;
            temp1.rm = p.rm+x;
            temp1.rc = p.rc+y;
            temp1.ship = -1;
            if(IsSafe(temp1) == 1 && pd(top, temp1) == 1)
	        {
	            temp[top++] = temp1;
	            dfs(temp1, temp1.lm, temp1.lc);//递归 
	            top--;//恢复现场 
	        }
        }
        
        if(p.ship == -1)//船在右岸
        {
            temp1.lm = p.lm+x;
            temp1.lc = p.lc+y;
            temp1.rm = p.rm-x;
            temp1.rc = p.rc-y;
            temp1.ship = 1;
            if(IsSafe(temp1) == 1 && pd(top, temp1) == 1)
	        {
	            temp[top++] = temp1;
	            dfs(temp1, temp1.lm, temp1.lc);//递归 
	            top--;//恢复现场	 
	        }
        }
        
    }
    
}

int main()
{
    ofstream fileout("result.txt",ios::trunc);//ios::trunc是清除原文件内容,可不写,默认就是它
    fileout.close();
	struct zt state;
    ifstream infile;
    outfile.open("result.txt");
    infile.open("num.txt"); //程序打开
    infile >> state.lm;
    infile >> state.lc;
    //printf("%d, %d\n", state.lm, state.lc);
    //scanf("%d", &state.lm);//天使数 
    //scanf("%d", &state.lc);//野人数 
    state.rc = 0;
    state.rm = 0;
    state.ship = 1;
    temp[top++] = state;
    dfs(state, state.lm, state.lc);
    printf("共有%d种方案\n", all);
    outfile.close();
    
    return 0;
}
