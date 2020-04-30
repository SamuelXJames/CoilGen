B_domain = readmatrix('bs_domain.csv');
B_domain = B_domain(2:end,2:end);
B = readmatrix('B.csv');
B = B(2:end,2:end);
B_mag = (sum(B.^2,2)).^0.5;
scatter3(B_domain(:,1),B_domain(:,2),B_domain(:,3),5,B_mag(:),'filled')
colorbar
%%
xy = -2.5 + 5*gallery('uniformdata',[200 2],0);
x = xy(:,1);
y = xy(:,2);
v = x.*exp(-x.^2-y.^2);
[xq,yq] = meshgrid(-2:.2:2, -2:.2:2);
vq = griddata(x,y,v,xq,yq);
mesh(xq,yq,vq)
hold on
plot3(x,y,v,'o')
xlim([-2.7 2.7])
ylim([-2.7 2.7])
%%
x = B_domain(1:100,1);
y = B_domain(1:100,2);
v = B_domain(1:100,3);
[xq,yq] = meshgrid(-400:2:400, -400:2:400);
vq = griddata(x,y,v,xq,yq);
%mesh(xq,yq,vq)

