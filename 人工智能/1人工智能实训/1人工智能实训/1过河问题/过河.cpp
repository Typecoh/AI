#include <iostream>

#define MAX_size 33

using namespace std; 

struct solution 								//定义结构体 -- 三个值--- 左天使。左野人。船的状态 。 
{
	int L_angel;
	int L_wild;
	int boat_state;
};

struct solution anxwer_plan[MAX_size]; 			//操作结构体数组--------------执行深度搜索遍历 --- 状态数 
int index;										//坐标控制变量 -------------------更新操作结构体的路径选择
int pache_count;								//路径数
int flag; 										//初始化一次标志位 

void init()
{
	anxwer_plan[0].boat_state = 1;
	anxwer_plan[0].L_angel = 2;
	anxwer_plan[0].L_wild = 2;
	index = 0;
	pache_count = 0;
	flag = 0;
}

int A_M_DFS(solution temp_ans)//判断当前节点是否合法
{	
	if (temp_ans.L_angel == 0 && temp_ans.L_wild == 0) //已经达到了最终的目标 --------------------输出正确状态后产生的路径 
	{
		pache_count++;
		
		cout<<"第"<<pache_count<<"种可行方式\n";
		for (int i = 0; i < index+1; i++)
		{
			cout<<"("<<anxwer_plan[i].L_angel<<","<<anxwer_plan[i].L_wild<<","<<anxwer_plan[i].boat_state<<")";
		}
		
		cout<<endl;
		return 0;
	}
	
	
	//#####################################################搜索递归跳出的条件#################################################
	if (temp_ans.L_angel < 0 || temp_ans.L_wild < 0 || temp_ans.L_angel>2 || temp_ans.L_wild>2) //------------------------------ 人数限制 
	{
		return 0;
	}
		
	if((temp_ans.L_angel && temp_ans.L_wild > temp_ans.L_angel)
	|| ((2-temp_ans.L_angel) && (2 - temp_ans.L_angel) < (2 - temp_ans.L_wild))) //----------------------------------------------天使被吃限制 
	{
		return 0; //左右岸的情况都要考虑 
	}
		
	for(int i = 0;i<index;i++) //------------------------------------------------------------------------------------------------递归跳出限制 
	{
		if(temp_ans.L_angel == anxwer_plan[i].L_angel && temp_ans.L_wild == anxwer_plan[i].L_wild && temp_ans.boat_state == anxwer_plan[i].boat_state)
		{
			return 0;
		}
	}
	//##########################################################################################################################
	

	//小船状态的值由上一次的状态值更新，不可自行取反 

	//操作一 -----------------------------------------一个天使和一个野人过河---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //该标记为正值时，小船向左走；反之右走 ---便于更新记录数量 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state; 
	A_M_DFS(anxwer_plan[index]);
	index--; //更新状态节点，挖掘多种路径 
	//------------------------------------------------------------------------------------------------------------------------------
	
	//##################################################################################################################################
	
	//操作二 -----------------------------------------两个个天使过河---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //该标记为正值时，小船向左走；反之右走 ---便于更新记录数量 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state*2;
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild;
	A_M_DFS(anxwer_plan[index]);
	index--; //更新状态节点，挖掘多种路径 
	
	//###################################################################################################################################
	
	//操作三 -----------------------------------------两个个野人过河---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //该标记为正值时，小船向左走；反之右走 ---便于更新记录数量 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state*2; 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel; 
	A_M_DFS(anxwer_plan[index]);
	index--; //更新状态节点，挖掘多种路径 
	
	//操作四-----------------------------------------一个天使河---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //该标记为正值时，小船向左走；反之右走 ---便于更新记录数量 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild; 
	A_M_DFS(anxwer_plan[index]);
	index--; //更新状态节点，挖掘多种路径 
	//------------------------------------------------------------------------------------------------------------------------------
	
	//操作五-----------------------------------------一个野人过河---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //该标记为正值时，小船向左走；反之右走 ---便于更新记录数量 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel; 
	A_M_DFS(anxwer_plan[index]);
	index--; //更新状态节点，挖掘多种路径 
	//------------------------------------------------------------------------------------------------------------------------------
	
	
	return 0;
}

int main()
{	
	init();
	A_M_DFS(anxwer_plan[index]);	
	return 0;
}
