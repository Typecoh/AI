%% 计算两两城市之间的距离
%输入 a  各城市的位置坐标
%输出 D  两两城市之间的距离
function D=Distanse(pos1)
row=size(pos1,1);
D=zeros(row,row);
for i=1:row
    for j=i+1:row
        D(i,j)=((pos1(i,1)-pos1(j,1))^2+(pos1(i,2)-pos1(j,2))^2)^0.5;
        D(j,i)=D(i,j);
    end
end
