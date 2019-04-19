%///////////////////////////////////
%/Transformacion lineal por partes
%/Autor: Bryan Medina
%/////////////////////////////////

f = imread('gordon.jpg');
f = rgb2gray(f);

r1 = 120; r2 = 121;
s1 = 1; s2 = 255;

%funciones de la pendiente en los distintos segmentos
a = (s1 - 0)/(r1 - 0);
b = (s2 - s1)/(r2 - r1);
c = (255 - s2)/(255 - r2);

%segmento a
xa = 0:r1;
ya = a*xa;
plot(xa, ya, 'r');

%segmento b
xb = r1:r2; 
yb = b * (xb - r1) + a * r1 ;
hold on;
plot(xb, yb, 'g');

%segmento c 
xc = r2:255;
yc = c * (xc - r2) + b * (r2 - r1) + a * r1;
plot(xc, yc, 'b');
title('mapeo de intensidades')
xlim([0 255])
ylim([0 255])

[m, n] = size(f);
for i = 1:m
    for j = 1:n
        if(f(i, j) >= 0 & f(i, j) <= r1)
            g(i, j) = f(i, j) * a;
        
        elseif(f(i, j) > r1 & f(i, j) <= r2)
            g(i, j) = (f(i, j) - r1) * b + a * r1;

        elseif(f(i, j) > r2 & f(i, j) <= 255)
            g(i, j) = c * (f(i, j) - r2) + b * (r2 - r1) + a * r1;
        end
    end
end

figure;
subplot(1, 2, 1);
imshow(f);
title('imagen de entrada f')
subplot(1, 2, 2);
imshow(g);
title('imagen de salida g')