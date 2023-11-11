% 读取两个城市的坐标
load('CityPosition1.mat')
pos1=X;
load('CityPosition2.mat')
pos2 = X;
load('CityPosition3.mat')
pos3 = X;

 % 开始对城市位置进行可视化
x = pos1(:,1);
y = pos1(:,2);
plot(x,y,'o');
xlabel('城市横坐标');
ylabel('城市纵坐标');
grid on;

%计算城市间的距离
function D = Distance(a)
%计算两两城市之间的距离
%输入的数据为所有城市的x、y坐标位置矩阵city_location，输出为两两城市的距离构成的矩阵D
 
row = size(a,1);
 
D = zeros(row,row);
for i = 1:row
    for j = i+1:row
        D(i,j) = ((a(i,1)-a(j,1))^2+(a(i,2)-a(j,2))^2)^0.5;
        D(j,i) = D(i,j);
    end
end

%遗传算法初始化
%参数设置
NIND = 100;         %种群大小
MAXGEN = 100;       %最大迭代次数
Pc = 0.9;           %交叉概率，相当于基因遗传的时候染色体交叉
Pm = 0.05;          %染色体变异
GGAP = 0.9;         %这个是代沟，通过遗传方式得到的子代数为父代数*GGAP
%生成初始种群
function Chrom = InitPop(NIND,N)
%输入：
%NIND：种群大小
%N：个体染色体长度（城市个数）
%输出：初始种群
Chrom = zeros(NIND,N); % 定义存储种群的变量
for i = 1:NIND
    Chrom(i,:) = randperm(N);
end
%旅行商路线可视化
function DrawPath(Chrom,X)
%输入：
%待画路线
%城市的坐标位置
%输出：
%旅行商的路线
 
R =  [Chrom(1,:) Chrom(1,1)]; %第一个随机解（个体）【Chrom(1,:)取第一行数据】，一共有n个城市，但是这里R有n+1个值，因为后面又补了一个Chrom(1,1)，“是为了让路径最后再回到起点”
figure;
hold on
plot(X(:,1),X(:,2),'bo')%X(:,1)，X(:,2)分别代表的X轴坐标和Y轴坐标
%plot(X(:,1),X(:,2),'o','color',[1,1,1])%X(:,1)，X(:,2)分别代表的X轴坐标和Y轴坐标，
plot(X(Chrom(1,1),1),X(Chrom(1,1),2),'rv','MarkerSize',20)%标记起点
A = X(R,:);                         %A是将之前的坐标顺序用R打乱后重新存入A中
row = size(A,1);                    %row为坐标数+1
for i = 2:row
    [arrowx,arrowy] = dsxy2figxy(gca,A(i-1:i,1),A(i-1:i,2));    %dsxy2figxy坐标转换函数，记录两个点
    annotation('textarrow',arrowx,arrowy,'HeadWidth',5,'color',[0,0,1]);%将这两个点连接起来
end
hold off
xlabel('横坐标x')
ylabel('纵坐标y')
title('旅行商轨迹图')
box on

%%%
function varargout = dsxy2figxy(varargin) %%将两点坐标值转化至0,1之间
if length(varargin{1}) == 1 && ishandle(varargin{1}) ...
                            && strcmp(get(varargin{1},'type'),'axes')   
    hAx = varargin{1};
    varargin = varargin(2:end);
else
    hAx = gca;
end
if length(varargin) == 1
    pos = varargin{1};
else
    [x,y] = deal(varargin{:});
end
axun = get(hAx,'Units');
set(hAx,'Units','normalized'); 
axpos = get(hAx,'Position');
axlim = axis(hAx);
axwidth = diff(axlim(1:2));
axheight = diff(axlim(3:4));
if exist('x','var')
    varargout{1} = (x - axlim(1)) * axpos(3) / axwidth + axpos(1);
    varargout{2} = (y - axlim(3)) * axpos(4) / axheight + axpos(2);
else
    pos(1) = (pos(1) - axlim(1)) / axwidth * axpos(3) + axpos(1);
    pos(2) = (pos(2) - axlim(3)) / axheight * axpos(4) + axpos(2);
    pos(3) = pos(3) * axpos(3) / axwidth;
    pos(4) = pos(4) * axpos(4 )/ axheight;
    varargout{1} = pos;
end
set(hAx,'Units',axun)


%编写函数将最优路径输出
function p=OutputPath(R)
%打印路线函数
%以1->2->3的形式在命令行打印路线
 
R = [R,R(1)];
N = length(R);
p = num2str(R(1));
for i = 2:N
    p = [p,'->',num2str(R(i))];
end
disp(p)

%目标函数及适应度函数   目标函数为个体经历的路径总和
function len = PathLength(D,Chrom)
%计算所有个体的路线长度
%输入
%D两两城市之间的距离
%Chrom个体的轨迹
 
[~,col] = size(D); %返回D的列数 
NIND = size(Chrom,1);%NIND等于初始种群
len = zeros(NIND,1);%初始化一个大小等于NIND的len来记录长度
for i = 1:NIND
    p = [Chrom(i,:) Chrom(i,1)];%构造p矩阵保存路线图 将第一行路线提出 再加上第一个构成回路
    i1 = p(1:end-1);%i1从第一个开始遍历到倒数第二个
    i2 = p(2:end);%i2从第二个开始遍历到倒数第一个
    len(i,1) = sum(D((i1-1)*col+i2));%计算出每种路线（种群的个体）的长度，这里相当于把D矩阵沿行展开
end

%计算个体的适应度，适应度用于评价个体的优劣程度，适应度越大个体越好，反之适应度越小则个体越差，这里将目标值的倒数作为适应度：
function FitnV = Fintness(len) %适应度函数
%输入：
%len 个体的长度（TSP的距离）
%输出：
%FitnV 个体的适应度值
FitnV = 1./len;


%选择
function NewChrIx = Sus(FitnV,Nsel)
%输入：
%FitnV 个体的是适应度值
%Nsel 被选个体的数目
%输出：
%NewChrIx 被选择个体的索引号
[Nind,ans] = size(FitnV);%Nind为FitnV的行数也就是个体数 ans为列数1
cumfit = cumsum(FitnV);%对适应度累加 例如 1 2 3 累加后 1 3 6 用来计算累积概率
trials = cumfit(Nind)/Nsel * (rand + (0:Nsel-1)');%cumfit(Nind)表示的是矩阵cumfit的第Nind个元素 A.'是一般转置，A'是共轭转置 rand返回一个在区间 (0,1) 内均匀分布的随机数
%cumfit(Nind)/Nsel平均适应度 * （rand +(0:Nsel-1)'）从0开始到89的转置矩阵（行矩阵变列矩阵）加上每一项加上一个0-1的随机数
%生成随机数矩阵 用来筛选
Mf = cumfit(:,ones(1,Nsel));%将生成的累积概率 复制90份 生成一个100*90的矩阵
Mt = trials(:,ones(1,Nind))';
[NewChrIx,ans] = find(Mt<Mf & [zeros(1,Nsel);Mf(1:Nind-1,:)]<= Mt);%寻找满足条件的个体 返回返回数组 X 中每个元素的行和列下标
[ans,shuf] = sort(rand(Nsel,1));%生成Nsel*1的随机数矩阵  按升序对 A 的元素进行排序 返回选择的shuf 随机打乱个体顺序 保证后续遗传算子操作的随机性
NewChrIx = NewChrIx(shuf);%返回shuf索引的矩阵元素

function SelCh = Select(Chrom,FitnV,GGAP)
%输入：
%Chrom 种群
%FitnV 适应度值
%GGAP 选择概率
%输出：
%SelCh 被选择的个体
NIND = size(Chrom,1);%种群个体总数
NSel = max(floor(NIND * GGAP+.5),2);%确定下一代种群的个体数，如果不足二个就计为二个
ChrIx = Sus(FitnV,NSel);
SelCh = Chrom(ChrIx,:);

%交叉
function [a,b] = intercross(a,b)
%输入：
%a和b为两个待交叉的个体
%输出：
%a和b为交叉后得到的两个个体
L = length(a);
%随机产生交叉区段
r1 = randsrc(1,1,[1:L]); % 这里先随机选出两个位置，位置不能超过
r2 = randsrc(1,1,[1:L]); % 
if r1~=r2
    a0 = a;
    b0 = b;
    s = min([r1,r2]);
    e = max([r1,r2]);
    for i = s:e
        a1 = a;
        b1 = b;
        %第一次互换
        a(i) = b0(i);
        b(i) = a0(i);
        %寻找相同的城市
        x = find(a==a(i)); % 如果有相同的城市，x会得到包含i的两个值，y同理
        y = find(b==b(i));
        %第二次互换产生新的解
        i1 = x(x~=i);      % 将位置不是i但相同的城市标记出来
        i2 = y(y~=i);
        if ~isempty(i1)
            a(i1)=a1(i);
        end
        if ~isempty(i2)
            b(i2)=b1(i);   % 注意，原文这里有误，应该是b(i2)
        end
    end
end
% 这里增加一段代码，r1=r2时，两个个体只在一点交叉
if r1 == r2
    a0 = a;
    b0 = b;
    a(r1) = b0(r1);
    b(r1) = a0(r1);
    x = find(a==a(r1));
    y = find(b==b(r1));
    i1 = x(x~=r1);
    i2 = y(y~=r1);
    if ~isempty(i1)
        a(i1) = a0(r1);
    end
    if ~isempty(i2)
        b(i2) = b0(r1);
    end
end
%总的交叉函数
function SelCh = Recombin(SelCh,Pc)
%交叉操作
%输入：
%SelCh 被选择的个体
%Pc    交叉概率
%输出：
%SelCh 交叉后的个体
 
NSel = size(SelCh,1);
for i = 1:2:NSel - mod(NSel,2) % 若不减去余数且NSel如果是奇数，最后一个i会等于NSel，i+1报错
    if Pc>=rand %交叉概率PC
        [SelCh(i,:),SelCh(i+1,:)] = intercross(SelCh(i,:),SelCh(i+1,:));
    end
end

%变异
function SelCh = Mutate(SelCh,D,Pm)
%变异操作
%输入：
%SelCh  被选择的个体
%Pm  变异概率
%输出：
%SelCh  变异后的个体
index = SelCh;
col = size(SelCh,2); %返回SelCh的列数
%lenSelCh = [];
lenSelCh = PathLength(D,SelCh);
[NSel,L] = size(SelCh);
for i = 1:NSel
    if Pm >= rand
        R = randperm(L);
        index(i,R(1:2)) = index(i,R(2:-1:1)); % 将个体i中R(1)和R(2)这两个位置的城市互换
        p = [index(i,:) index(i,1)];
        i1 = p(1:end-1);
        i2 = p(2:end);
        DIndexi = sum(D((i1-1)*col+i2));              % 计算出变异后个体的路径距离
        if DIndexi < lenSelCh(i)                 % 如果变异后路径距离比变异前更小，则保留变异
            SelCh(i) = index(i);
        end
    end
end

%重插入
function Chrom = Reins(Chrom,SelCh,ObjV)
%重插入子代的种群
%输入：
%Chrom      父代的种群
%SelCh      子代的种群
%ObjV       父代适应度
%输出：
%Chrom      组合父代与子代后得到的新种群
NIND = size(Chrom,1);
NSel = size(SelCh,1);
[TobjV,index] = sort(ObjV);
Chrom =  [Chrom(index(1:NIND-NSel),:);SelCh];

