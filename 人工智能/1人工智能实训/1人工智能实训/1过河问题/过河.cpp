#include <iostream>

#define MAX_size 33

using namespace std; 

struct solution 								//����ṹ�� -- ����ֵ--- ����ʹ����Ұ�ˡ�����״̬ �� 
{
	int L_angel;
	int L_wild;
	int boat_state;
};

struct solution anxwer_plan[MAX_size]; 			//�����ṹ������--------------ִ������������� --- ״̬�� 
int index;										//������Ʊ��� -------------------���²����ṹ���·��ѡ��
int pache_count;								//·����
int flag; 										//��ʼ��һ�α�־λ 

void init()
{
	anxwer_plan[0].boat_state = 1;
	anxwer_plan[0].L_angel = 2;
	anxwer_plan[0].L_wild = 2;
	index = 0;
	pache_count = 0;
	flag = 0;
}

int A_M_DFS(solution temp_ans)//�жϵ�ǰ�ڵ��Ƿ�Ϸ�
{	
	if (temp_ans.L_angel == 0 && temp_ans.L_wild == 0) //�Ѿ��ﵽ�����յ�Ŀ�� --------------------�����ȷ״̬�������·�� 
	{
		pache_count++;
		
		cout<<"��"<<pache_count<<"�ֿ��з�ʽ\n";
		for (int i = 0; i < index+1; i++)
		{
			cout<<"("<<anxwer_plan[i].L_angel<<","<<anxwer_plan[i].L_wild<<","<<anxwer_plan[i].boat_state<<")";
		}
		
		cout<<endl;
		return 0;
	}
	
	
	//#####################################################�����ݹ�����������#################################################
	if (temp_ans.L_angel < 0 || temp_ans.L_wild < 0 || temp_ans.L_angel>2 || temp_ans.L_wild>2) //------------------------------ �������� 
	{
		return 0;
	}
		
	if((temp_ans.L_angel && temp_ans.L_wild > temp_ans.L_angel)
	|| ((2-temp_ans.L_angel) && (2 - temp_ans.L_angel) < (2 - temp_ans.L_wild))) //----------------------------------------------��ʹ�������� 
	{
		return 0; //���Ұ��������Ҫ���� 
	}
		
	for(int i = 0;i<index;i++) //------------------------------------------------------------------------------------------------�ݹ��������� 
	{
		if(temp_ans.L_angel == anxwer_plan[i].L_angel && temp_ans.L_wild == anxwer_plan[i].L_wild && temp_ans.boat_state == anxwer_plan[i].boat_state)
		{
			return 0;
		}
	}
	//##########################################################################################################################
	

	//С��״̬��ֵ����һ�ε�״ֵ̬���£���������ȡ�� 

	//����һ -----------------------------------------һ����ʹ��һ��Ұ�˹���---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //�ñ��Ϊ��ֵʱ��С�������ߣ���֮���� ---���ڸ��¼�¼���� 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state; 
	A_M_DFS(anxwer_plan[index]);
	index--; //����״̬�ڵ㣬�ھ����·�� 
	//------------------------------------------------------------------------------------------------------------------------------
	
	//##################################################################################################################################
	
	//������ -----------------------------------------��������ʹ����---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //�ñ��Ϊ��ֵʱ��С�������ߣ���֮���� ---���ڸ��¼�¼���� 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state*2;
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild;
	A_M_DFS(anxwer_plan[index]);
	index--; //����״̬�ڵ㣬�ھ����·�� 
	
	//###################################################################################################################################
	
	//������ -----------------------------------------������Ұ�˹���---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //�ñ��Ϊ��ֵʱ��С�������ߣ���֮���� ---���ڸ��¼�¼���� 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state*2; 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel; 
	A_M_DFS(anxwer_plan[index]);
	index--; //����״̬�ڵ㣬�ھ����·�� 
	
	//������-----------------------------------------һ����ʹ��---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //�ñ��Ϊ��ֵʱ��С�������ߣ���֮���� ---���ڸ��¼�¼���� 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild; 
	A_M_DFS(anxwer_plan[index]);
	index--; //����״̬�ڵ㣬�ھ����·�� 
	//------------------------------------------------------------------------------------------------------------------------------
	
	//������-----------------------------------------һ��Ұ�˹���---------------------------------------------------- 
	index++;
//	if(anxwer_plan[index].boat_state == 0)
//	{
//		anxwer_plan[index].boat_state = 1;
//	}
//	else
//	{
//		anxwer_plan[index].boat_state = 0;
//	}
	anxwer_plan[index].boat_state = -1*anxwer_plan[index-1].boat_state; //�ñ��Ϊ��ֵʱ��С�������ߣ���֮���� ---���ڸ��¼�¼���� 
	anxwer_plan[index].L_wild = anxwer_plan[index-1].L_wild - anxwer_plan[index-1].boat_state; 
	anxwer_plan[index].L_angel = anxwer_plan[index-1].L_angel; 
	A_M_DFS(anxwer_plan[index]);
	index--; //����״̬�ڵ㣬�ھ����·�� 
	//------------------------------------------------------------------------------------------------------------------------------
	
	
	return 0;
}

int main()
{	
	init();
	A_M_DFS(anxwer_plan[index]);	
	return 0;
}
