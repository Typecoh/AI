//��ʹҰ�˹�������    ��ʹ��Ұ�˵�������������ȡ 
#include<iostream>
#include <fstream>
#include<stdlib.h>

using namespace std;

struct zt
{
    int lm;//����ʹ��
    int lc;//��Ұ����
    int rm;//�Ұ���ʹ��
    int rc;//�Ұ�Ұ����
    int ship;//����λ�ã�1��ʾ���󰶣�0��ʾ���Ұ�
};
struct zt p, temp[1000]; 

int top = 0;  //��Ч�ڵ���
int all = 0;  //���ߵķ�����
int xx[5] = {0,0,1,1,2};
int yy[5] = {1,2,0,1,0};
ofstream outfile;

int IsSafe(zt temp)//�ж��Ƿ�Ϊ��Ч״̬��1��ʾ��Ч��0��ʾ��Ч 
{
    if((temp.lm>=temp.lc&&temp.rm>=temp.rc&&temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0)||
       (temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0&&temp.lm==0&&temp.rm>=temp.rc)||
       (temp.lm>=0&&temp.lc>=0&&temp.rm>=0&&temp.rc>=0&&temp.lm>=temp.lc&&temp.rm==0))
    {
        return 1;
    }
    return 0;
}

int pd(int top, zt p)//�ж�p�Ƿ���ǰ��Ľڵ��ظ���0��ʾ�ظ���1��ʾδ�ظ� 
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

//������ȱ�������ʼ�ڵ㣨x��y��0��0��1���� Ŀ��ڵ㣨0��0��x��x��-1�� 
void dfs(zt p, int lm, int lc)
{
    p.lm = lm;
    p.lc = lc;
	if(p.lc==0&&p.lm==0&&p.rc==temp[0].lc&&p.rm==temp[0].lm)//����Ŀ��ڵ� 
    {
        all++;
		//ofileAgain.open("result.txt",ios::app);
        outfile << "��" << all << "�ַ�����" << endl;
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
        if(p.ship == 1)//������
        {
            temp1.lm = p.lm-x;
            temp1.lc = p.lc-y;
            temp1.rm = p.rm+x;
            temp1.rc = p.rc+y;
            temp1.ship = -1;
            if(IsSafe(temp1) == 1 && pd(top, temp1) == 1)
	        {
	            temp[top++] = temp1;
	            dfs(temp1, temp1.lm, temp1.lc);//�ݹ� 
	            top--;//�ָ��ֳ� 
	        }
        }
        
        if(p.ship == -1)//�����Ұ�
        {
            temp1.lm = p.lm+x;
            temp1.lc = p.lc+y;
            temp1.rm = p.rm-x;
            temp1.rc = p.rc-y;
            temp1.ship = 1;
            if(IsSafe(temp1) == 1 && pd(top, temp1) == 1)
	        {
	            temp[top++] = temp1;
	            dfs(temp1, temp1.lm, temp1.lc);//�ݹ� 
	            top--;//�ָ��ֳ�	 
	        }
        }
        
    }
    
}

int main()
{
    ofstream fileout("result.txt",ios::trunc);//ios::trunc�����ԭ�ļ�����,�ɲ�д,Ĭ�Ͼ�����
    fileout.close();
	struct zt state;
    ifstream infile;
    outfile.open("result.txt");
    infile.open("num.txt"); //�����
    infile >> state.lm;
    infile >> state.lc;
    //printf("%d, %d\n", state.lm, state.lc);
    //scanf("%d", &state.lm);//��ʹ�� 
    //scanf("%d", &state.lc);//Ұ���� 
    state.rc = 0;
    state.rm = 0;
    state.ship = 1;
    temp[top++] = state;
    dfs(state, state.lm, state.lc);
    printf("����%d�ַ���\n", all);
    outfile.close();
    
    return 0;
}
