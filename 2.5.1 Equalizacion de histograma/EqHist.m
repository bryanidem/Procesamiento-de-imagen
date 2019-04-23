%//////////////////////////////////////
%/Ecualizacion de histograma
%/autor: Bryan Medina
%////////////////////////////////////


f = imread('zorro.jpg');
f = rgb2gray(f);

%calculo del histograma, bins son los niveles de intensidad
[histF, bins] = imhist(f);
%divido entre el numero de elementos de la imagen para normalizar (0 - 1)
histFNorm = histF./numel(f);

%realizo la sumatoria para calcular la funcion de transformacion, en este
%caso, una funcion de distribucion acumulada
cdf = cumsum(histFNorm);

[m, n] = size(f);
g = zeros(m, n);
%aqui mediante el valor de intensidad, accedo al valor de intensidad
%deseado (cdf) el cual tiene una distribucion de intensidades mas uniforme,
%resultando en un mejor contraste
for i = 1 : m
    for j = 1 : n
        g(i, j) = cdf(f(i, j)+1);
    end
end

% tambien esta la funcion en el toolbox
g1 = histeq(f, 256);

%graficar
figure();
subplot(131);
plot(bins, histF);
subplot(132);
plot(bins, cdf);

histG = imhist(g);
subplot(133);
plot(bins, histG);

figure();
subplot(121);
imshow(f);
subplot(122);
imshow(g);

