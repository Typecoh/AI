clc
clear
% ��ȡ�������е�����
load('CityPosition1.mat')
pos1=X;
load('CityPosition2.mat')
pos2 = X;
load('CityPosition3.mat')
pos3 = X;

 % ��ʼ�Գ���λ�ý��п��ӻ�
x = pos1(:,1);
y = pos1(:,2);
plot(x,y,'o');
xlabel('���к�����');
ylabel('����������');
grid on;
 
NIND = 100;         %��Ⱥ��С
MAXGEN = 100;       %����������
Pc = 0.9;           %������ʣ��൱�ڻ����Ŵ���ʱ��Ⱦɫ�彻��
Pm = 0.05;          %Ⱦɫ�����
GGAP = 0.9;         %����Ǵ�����ͨ���Ŵ���ʽ�õ����Ӵ���Ϊ������*GGAP
D = Distance(pos1);    %ͨ������������Լ���i,j����֮��ľ���
N = size(D,1);      %�����ж��ٸ������
%%��ʼ����Ⱥ
Chrom = InitPop(NIND,N);    %Chrome�������Ⱥ
%%����������·��ͼ
DrawPath(Chrom(1,:),pos1)
pause(0.0001)
%���������·�ߺ��ܾ���
disp('��ʼ��Ⱥ�е�һ�����ֵ')
OutputPath(Chrom(1,:));%����һ������
Rlength = PathLength(D,Chrom(1,:));
disp(['�ܾ���;',num2str(Rlength)]);
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
%�Ż�
gen = 0;
trace = zeros(1,MAXGEN);
title('�Ż�����')
xlabel('��������')
ylabel('��ǰ���Ž�')
ObjV = PathLength(D,Chrom);%���㵱ǰ·�߳��ȣ������������������Щ����·��
preObjV = min(ObjV);%��ǰ���Ž�
while gen<MAXGEN
    %%������Ӧ��
    ObjV = PathLength(D,Chrom);     %����·�߳���
    pause(0.0001);
    preObjV = min(ObjV);
    trace(1,gen+1)=preObjV;
    %trace=[trace preObjV];
    FitnV = Fitness(ObjV);
    %ѡ��
    SelCh = Select(Chrom,FitnV,GGAP);
    %�������
    SelCh = Recombin(SelCh,Pc);
    %����
    SelCh = Mutate(SelCh,D,Pm);
    Chrom = Reins(Chrom,SelCh,ObjV);
    gen = gen + 1;
end
%�������Ž��·��ͼ
ObjV = PathLength(D,Chrom);     %����·�߳���
[minObjV,minInd] = min(ObjV);
DrawPath(Chrom(minInd(1),:),pos1)
figure();
plot([1:MAXGEN],trace(1,:));
%%������Ž��·�ߺ;���
disp('���Ž�:')
p = OutputPath(Chrom(minInd(1),:));
disp(['�������߹����ܾ��룺',num2str(ObjV(minInd(1)))]);
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')








