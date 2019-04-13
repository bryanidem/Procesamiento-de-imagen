%////////////////////////////
%/Logarithmic Transformation
%//Author: Bryan Medina
%////////////////////////////

f = imread('darkNetflix.jpg');
f = rgb2gray(f);

%constante c para obtener el rango mismo rango que la imagen de entrada
c = 255/log(1 + 255);

% Calculo de la tranformacion logaritmo
g = c * log(1 + double(f));
%conversion de la escala 0-1 a 0-255 para el correcto despliegue
g = im2uint8(mat2gray(g));

% grafica que muestra el mapeo de la funcion log
x = (0: 255);
y = log(1 + double(x));


%% cosillas para graficar
figure;
plot(x, y);
title('g(x, y) = c log(1 + f(x, y))');
xlabel('brillo - imagen de entrada f(x, y)');
ylabel('brillo - imagen de entrada g(x, y)');

figure;
subplot(1, 2, 1);
imshow(f);
title ('imagen de entrada f(x, y)');

subplot(1, 2, 2);
imshow(g);
title ('imagen de salida g(x, y)');