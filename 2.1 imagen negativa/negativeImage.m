% obtención del complemento de una imagen.

%cargar la imagen a la variable f (de tipo uint8 con 3 canales)
f = imread('chest.jpg');

%convertir la imagen a un solo canal (escala de grises)
f = rgb2gray(f);


x = (0:255);
y = 255 - x;

%transformacion complemento, en donde f(x, y) + g(x, y) debe ser igual a
%255, despejando, g(x, y) = 255 - f(x, y)

g = 255 - f;



%% cosillas para graficar
figure;
plot(x, y);
title('g(x, y) = 255 - f(x, y)');
xlabel('brillo - imagen de entrada f(x, y)');
ylabel('brillo - imagen de entrada g(x, y)');

figure;
subplot(1, 2, 1);
imshow(f);
title ('imagen de entrada f(x, y)');

subplot(1, 2, 2);
imshow(g);
title ('imagen de salida g(x, y)');



