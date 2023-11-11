#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#include <stack>

using namespace std;

#define N 100
typedef pair<int, int> PII;
#define x first
#define y second

int people_n = 3; // angle and people number
int ship_n = 2;   // ship
int a[N][N][4];   // state
int stay[4];
int flag = 0; // zhao dao
PII q[100];   // shu chu
int cnt = 0;  // ji shu

void init();                               // chu shi
void dfs();                                // shen sou
int judge(int a1, int b1, int c1, int d1); // pan duan
int main()
{
  // chu shi hu
  init();
  //		for(int i = 0 ; i <= people_n*2 + 1 ; i ++)
  //	{
  //		for(int j = 0 ; j <= people_n ; j ++ )
  //		{
  //			for(int k = 0 ; k < 4 ; k ++)
  //			{
  //				printf("%d",a[i][j][k]);
  //			}
  //			printf(" ");
  //		}
  //		printf("\n");
  //	}
  stay[0] = people_n, stay[1] = people_n, stay[2] = 1, stay[3] = 0;
  q[0].x = 3, q[0].y = 3;
  dfs();

  init();
  cnt = 0;
  stay[0] = people_n, stay[1] = people_n, stay[2] = 1, stay[3] = 0;
  q[0].x = 3, q[0].y = 3;
  a[3][1][3] = -1;
  dfs();
}

void init()
{
  int num_a = people_n;
  int num_b = people_n;
  int num_c = 1;
  int num_d = 0;
  int jishu = 0;
  for (int i = 0; i <= people_n * 2 + 1; i++)
  {
    jishu++;
    if (jishu == 3)
    {
      num_a--;
      jishu = 1;
    }
    num_b = people_n;
    for (int j = 0; j <= people_n; j++)
    {

      for (int k = 0; k < 4; k++)
      {
        if (k == 0)
          a[i][j][k] = num_a;
        if (k == 1)
          a[i][j][k] = num_b;
        if (k == 2 && i % 2 == 0)
          a[i][j][k] = num_c;
        if (k == 2 && i % 2 == 1)
          a[i][j][k] = !num_c;
        if (k == 3)
          a[i][j][k] = num_d;
        if ((a[i][j][0] < a[i][j][1] && a[i][j][0] != 0 ||
             a[i][j][0] > a[i][j][1] && a[i][j][0] != people_n) &&
            k == 3)
          a[i][j][k] = -1; // weixian
      }
      num_b--;
    }
  }
}
void dfs()
{
  if (stay[0] == 0 && stay[1] == 0 && stay[2] == 0 && stay[3] == 0)
  {
    flag++;
    //    	if(flag==1)
    for (int i = 0; i <= cnt; i++)
    {
      printf("%d %d %d\n", q[i].x, q[i].y, (i + 1) % 2);
    }
    printf("\n");
    //	for(int i = 0 ; i <= people_n*2 + 1 ; i ++)
    //	{
    //		for(int j = 0 ; j <= people_n ; j ++ )
    //		{
    //			for(int k = 0 ; k < 4 ; k ++)
    //			{
    //				printf("%d",a[i][j][k]);
    //			}
    //			printf(" ");
    //		}
    //		printf("\n");
    //	}
    cnt--;
    stay[0] = q[cnt].x;
    stay[1] = q[cnt].y;
    stay[2] = !stay[2];
    //	  if(a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1)  //shi fang zou guo de
    //	    a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0 ;
    return; // tiaochu
  }
  if (stay[2] == 1) // go
  {
    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[0] - 2 >= 0 && judge(stay[0] - 2, stay[1], !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //		    	a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[0] = stay[0] - 2;
        stay[2] = 0;

        dfs();
      }
    }
    else
    {
      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[0] - 1 >= 0 && stay[1] - 1 >= 0 && judge(stay[0] - 1, stay[1] - 1, !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			   a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[0] = stay[0] - 1;
        stay[1] = stay[1] - 1;
        stay[2] = 0;
        dfs();
      }
    }

    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    //	    else return;

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[1] - 2 >= 0 && judge(stay[0], stay[1] - 2, !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			    a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[1] = stay[1] - 2;
        stay[2] = 0;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }
  }
  else // back
  {

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[0] + 2 <= people_n && judge(stay[0] + 2, stay[1], !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			    a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[0] = stay[0] + 2;
        stay[2] = 1;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[0] + 1 <= people_n && stay[1] + 1 <= people_n && judge(stay[0] + 1, stay[1] + 1, !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			   a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[0] = stay[0] + 1;
        stay[1] = stay[1] + 1;
        stay[2] = 1;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[1] + 2 <= people_n && judge(stay[0], stay[1] + 2, !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			    a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[1] = stay[1] + 2;
        stay[2] = 1;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    //	    else return;

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[0] + 1 <= people_n && judge(stay[0] + 1, stay[1], !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			    a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[0] = stay[0] + 1;
        stay[2] = 1;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }

    if (judge(stay[0], stay[1], stay[2], stay[3]))
    {

      q[cnt].x = stay[0];
      q[cnt].y = stay[1];

      if (stay[1] + 1 <= people_n && judge(stay[0], stay[1], !stay[2], stay[3]))
      {
        cnt++;
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 1; // biaoji
                                                                           //			    a[(people_n - stay[0]) * 2 + 1][people_n - stay[1]][3] = 1; // biaoji
        stay[1] = stay[1] + 1;
        stay[2] = 1;
        dfs();
      }
    }
    else
    {

      cnt--;
      stay[0] = q[cnt].x;
      stay[1] = q[cnt].y;
      stay[2] = !stay[2];
      if (a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] == 1) // shi fang zou guo de
        a[(people_n - stay[0]) * 2 + !stay[2]][people_n - stay[1]][3] = 0;
      return;
    }
  }
}
int judge(int a1, int b1, int c1, int d1)
{
  int i = (people_n - a1) * 2 + !c1;
  int j = people_n - b1;
  if (a[i][j][3] == -1 || a[i][j][3] == 1)
  {
    return 0; // no
  }

  return 1; // yes
}
