%%%一个旅行商人要拜访全国31个省会城市，需要选择最短的路径%%%%


%%%蚁群算法解决TSP问题%%%%%%%

clear all; %清除所有变量
close all; %清图
clc ;      %清屏
m=50;    %% m 蚂蚁个数
Alpha=1;  %% Alpha 表征信息素重要程度的参数
Beta=5;  %% Beta 表征启发式因子重要程度的参数
Rho=0.1; %% Rho 信息素蒸发系数
NC_max=200; %%最大迭代次数
Q=100;         %%信息素增加强度系数

C=[
1304 2312;
3639 1315;
4177 2244;
3712 1399;
3488 1535;
3326 1556;
3238 1229;
4196 1004;
4312 790;
4386 570;
3007 1970;
2562 1756;
2788 1491;
2381 1676;
1332 695;
3715 1678;
3918 2179;
4061 2370;
3780 2212;
3676 2578;
4029 2838;
4263 2931;
3429 1908;
3507 2367;
3394 2643;
3439 3201;
2935 3240;
3140 3550;
2545 2357;
2778 2826;
2370 2975
];                %%31个省会坐标
%%-------------------------------------------------------------------------
%% 主要符号说明
%% C n个城市的坐标，n×2的矩阵
%% NC_max 最大迭代次数
%% m 蚂蚁个数
%% Alpha 表征信息素重要程度的参数
%% Beta 表征启发式因子重要程度的参数
%% Rho 信息素蒸发系数
%% Q 信息素增加强度系数
%% R_best 各代最佳路线
%% L_best 各代最佳路线的长度
%%=========================================================================
%%第一步：变量初始化
n=size(C,1);%n表示问题的规模（城市个数）
D=zeros(n,n);%D表示完全图的赋权邻接矩阵
for i=1:n
    for j=1:n
        if i~=j
            D(i,j)=((C(i,1)-C(j,1))^2+(C(i,2)-C(j,2))^2)^0.5;
        else
            D(i,j)=eps;      %i=j时不计算，应该为0，但后面的启发因子要取倒数，用eps（浮点相对精度）表示
        end
        D(j,i)=D(i,j);   %对称矩阵
    end
end
Eta=1./D;          %Eta为启发因子，这里设为距离的倒数
Tau=ones(n,n);     %Tau为信息素矩阵

mm = 2;  
ag_tasknum = ceil(n/mm); 
NC=1;               %迭代计数器，记录迭代次数
R_best=zeros(NC_max,ag_tasknum);       %各代最佳路线
L_best=inf.*ones(NC_max,1);   %各代最佳路线的长度
L_ave=zeros(NC_max,1);        %各代路线的平均长度
                     %一個路徑目標中分配給幾個螞蟻
start1 = [1400 1400];
start2 = [1500 1500];

Tabu=zeros(m,ag_tasknum);   %存储并记录路径的生成
mmm = m/mm;                   %分割蟻群
 while NC<=NC_max        %停止条件之一：达到最大迭代次数，停止
  

%     if mod(n, mm) ~= 0
%         M = ag_tasknum; % 向上取整 一個螞蟻要走多少目標
%         N = M-1;          %另一個螞蟻要走的目標數
%     end
% 
%     Randpos=[];   %随即存取
%     Randpos1 = [start1, Randpos];
%     Randpos2 = [start1, Randpos];
%     Randpos=[Randpos,randperm(n)]; %Randpos是一個0到31的索引向量
%     half_len = ceil(n/2);
%     matrix1 = randperm_n(1:half_len);  % 第一个矩阵，取前半部分
%     matrix2 = randperm_n(half_len+1:end);  % 第二个矩阵，取后半部分
% 
%     for i=1:(ceil(mmm/M))  %%第二步：将mmm只蚂蚁放到其被分配的M个城市上
%         
%         for j=1:(ceil(mmm/N) )%% 将mmm只蚂蚁放到其被分配的N个城市上(M+N=n)
%         end
   
%     end

%     for i=1:(ceil(m/n))  %%第二步：将m只蚂蚁放到n个城市上
%         Randpos=[Randpos,randperm(n)];
%         %%将一个随机排列的长度为 n 的向量（表示将 n 个城市随机排序）添加到 Randpos 向量的末尾。这样，Randpos 向量会逐渐增长，存储了所有迭代中生成的随机位置索引。
%     end
disp(['first',num2str(size(Tabu))])
    %Tabu(:,1)=(Randpos(1,1:mm))';
    Tabu(1:mmm,1)=1;
    Tabu((mmm+1):m,1)=1;
    %%将 Randpos 向量的前 m 个元素作为列，赋值给名为 Tabu 的矩阵的第一列。这里，Tabu 矩阵用于存储蚂蚁在每个迭代中访问的城市的顺序。

disp(['first2',num2str(size(Tabu))])

    %%第三步：m只蚂蚁按概率函数选择下一座城市，完成各自的周游 "改成兩隻螞蟻要算兩次
    for j=2:ag_tasknum     %所在城市不计算
        for i=1:mmm
            visited=Tabu(i,1:(j-1)); %记录已访问的城市，避免重复访问
            J=zeros(1,(ag_tasknum-j+1));       %待访问的城市
            P=J;                      %待访问城市的选择概率分布
            Jc=1;
            for k=1:ag_tasknum
                if length(find(visited==k))==0   %开始时置0
                    J(Jc)=k;
                    Jc=Jc+1;                         %访问的城市个数自加1
                end
            end
            %下面计算待选城市的概率分布
            for k=1:length(J)
                P(k)=(Tau(visited(end),J(k))^Alpha)*(Eta(visited(end),J(k))^Beta);
            end
            P=P/(sum(P));
            %按概率原则选取下一个城市
            Pcum=cumsum(P);     %cumsum，元素累加即求和
            Select=find(Pcum>=rand); %若计算的概率大于原来的就选择这条路线
            to_visit=J(Select(1));
            Tabu(i,j)=to_visit;
        end
    end

disp(['first3',num2str(size(Tabu))])

     for j=2:(n-ag_tasknum)     %所在城市不计算
        for i=mmm:m
            visited=Tabu(i,1:(j-1)); %记录已访问的城市，避免重复访问
            J=zeros(1,(ag_tasknum-j+1));       %待访问的城市
            P=J;                      %待访问城市的选择概率分布
            Jc=1;
            for k=1:ag_tasknum
                if length(find(visited==k))==0   %开始时置0
                    J(Jc)=k;
                    Jc=Jc+1;                         %访问的城市个数自加1
                end
            end
            %下面计算待选城市的概率分布
            for k=1:length(J)
                P(k)=(Tau(visited(end),J(k))^Alpha)*(Eta(visited(end),J(k))^Beta);
            end
            P=P/(sum(P));
            %按概率原则选取下一个城市
            Pcum=cumsum(P);     %cumsum，元素累加即求和
            Select=find(Pcum>=rand); %若计算的概率大于原来的就选择这条路线
            to_visit=J(Select(1));
            Tabu(i,j)=to_visit;
        end
    end

    
disp(['first4',num2str(size(Tabu))])

    if NC>=2
        Tabu(1,:)=R_best(NC-1,:);
    end
    %%第四步：记录本次迭代最佳路线
    L=zeros(m,1);     %开始距离为0，m*1的列向量

    %如何把兩隻螞蟻的路線合併

    %先算兩隻中第一隻的距離
    for i=1:mmm
        R=Tabu(i,:); %位訪問程式有問題
        for j=1:(ag_tasknum-1)  %j=1:(n-1)
            L(i)=L(i)+D(R(j),R(j+1));    %原距离加上第j个城市到第j+1个城市的距离
            disp(i)
            disp(j)
        end
        L(i)=L(i)+D(R(1),R(ag_tasknum));      %一轮下来后走过的距离
        L(i)=L(i)+((start1(1,1)-Tabu(1,1))^2+(start1(1,2)-Tabu(1,2))^2)^0.5; %加上第一點與初始點距離
        %還要算第二隻螞蟻的距離


       % D(i,j)=((C(i,1)-C(j,1))^2+(C(i,2)-C(j,2))^2)^0.5;
    end

    disp(['first5',num2str(size(Tabu))])


    L_best(NC)=min(L);           %最佳距离取最小
    pos=find(L==L_best(NC));
    R_best(NC,:)=Tabu(pos(1),:); %此轮迭代后的最佳路线
    L_ave(NC)=mean(L);           %此轮迭代后的平均距离
    NC=NC+1                      %迭代继续

disp(['first6',num2str(size(Tabu))])


    %%第五步：更新信息素
    Delta_Tau=zeros(n,n);        %开始时信息素为n*n的0矩阵
    for i=1:mmm
        for j=1:(ag_tasknum-1)
            Delta_Tau(Tabu(i,j),Tabu(i,j+1))=Delta_Tau(Tabu(i,j),Tabu(i,j+1))+Q/L(i);
            %此次循环在路径（i，j）上的信息素增量
        end
        Delta_Tau(Tabu(i,ag_tasknum),Tabu(i,1))=Delta_Tau(Tabu(i,ag_tasknum),Tabu(i,1))+Q/L(i);
        %此次循环在整个路径上的信息素增量
    end
    Tau=(1-Rho).*Tau+Delta_Tau; %考虑信息素挥发，更新后的信息素
    %%第六步：禁忌表清零
    Tabu=zeros(m,ag_tasknum);             %%直到最大迭代次数
end
%%第七步：输出结果
Pos=find(L_best==min(L_best)); %找到最佳路径（非0为真）
Shortest_Route=R_best(Pos(1),:) %最大迭代次数后最佳路径
Shortest_Length=L_best(Pos(1)) %最大迭代次数后最短距离

figure(1) 
plot(L_best)
xlabel('迭代次数')
ylabel('目标函数值')
title('适应度进化曲线')


figure(2)
subplot(1,2,1)                  %绘制第一个子图形
   %画路线图
%%=========================================================================
%% DrawRoute.m
%% 画路线图
%%-------------------------------------------------------------------------
%% C Coordinate 节点坐标，由一个N×2的矩阵存储
%% R Route 路线
%%=========================================================================
N=length(R);
scatter(C(:,1),C(:,2));
 hold on
 plot([C(R(1),1),C(R(N),1)],[C(R(1),2),C(R(N),2)],'g')
 hold on
for ii=2:N
    plot([C(R(ii-1),1),C(R(ii),1)],[C(R(ii-1),2),C(R(ii),2)],'g')
     hold on
end
title('旅行商问题优化结果 ')

subplot(1,2,2)                  %绘制第二个子图形
plot(L_best)
hold on                         %保持图形
plot(L_ave,'r')
title('平均距离和最短距离')     %标题
