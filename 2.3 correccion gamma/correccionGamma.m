%////////////////////////////
%/correccion gamma
%//Autor: Bryan Medina
%////////////////////////////

f = imread('sigure.jpg');
f = rgb2gray(f);

%constante segun para poner en el mismo rango de la imagen pero no me
%funciono del todo, y la mayoria utiliza c = 1
c = 255/log(1 + 255);

gamma = 0.2;
gamma1 = 5;
% primero se realiza un escalamiento de la intensidad de la imagen de 0 a 1
% donde estos valores despues son mapeados a los 256 valores de intensidad
g = im2uint8(mat2gray(1 * double(f).^gamma));
g1 = im2uint8(mat2gray(1 * double(f).^gamma1));

% una mejor version, con funciones esta en python

figure;
subplot(1, 3, 1);
imshow(f);
title('gamma = 1');

subplot(1, 3, 2);
imshow(g);
title('gamma = 0.2');

subplot(1, 3, 3)
imshow(g1);
title('gamma = 5');

