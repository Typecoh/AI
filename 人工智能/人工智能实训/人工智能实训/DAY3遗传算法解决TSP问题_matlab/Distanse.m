%% ������������֮��ľ���
%���� a  �����е�λ������
%��� D  ��������֮��ľ���
function D=Distanse(pos1)
row=size(pos1,1);
D=zeros(row,row);
for i=1:row
    for j=i+1:row
        D(i,j)=((pos1(i,1)-pos1(j,1))^2+(pos1(i,2)-pos1(j,2))^2)^0.5;
        D(j,i)=D(i,j);
    end
end
