%//////////////////////////////////////
%//Histograma
%//Autor: Bryan Medina
%/////////////////////////////////////

f = imread('zorro.jpg');
f = rgb2gray(f);

[m, n] = size(f);

hist = zeros(256, 1);
x = (1:256);

for i = 1:m
    for j = 1:n
        
        %aqui va el mas 1 por que los arrays empiezan en 1 en matlab, meh
        brillo = f(i, j) + 1 ;
        %se suma el pixel con este brillo en especifico, el histograma pues
        hist(brillo) = hist(brillo)+1;

    end
end

plot(x, hist);
xlabel('niveles de intensidad');
ylabel('numero de pixeles');
title('histograma');

% y pues matlab tambien tiene una funcion para calcular el histograma
matlabHist = imhist(f);
figure()
plot(x, matlabHist);
xlabel('niveles de intensidad');
ylabel('numero de pixeles');
title('histograma matlab');



