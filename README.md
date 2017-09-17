# Maturitni-projekt-OpenCV

## Postup
---
**16.9.**
* Instalace Ubuntu 16.04. ve VirtualBoxu
  - *OpenCV lze nainstalovat na Windows, Linux, Android, MacOS, FreeBSD, OpenBSD a mobily se systémem Android, Maemo, iOS. Já jsem zvolil Ubuntu, protože jsem se dočetl, že na Ubuntu je OpenCV méně problémové.*
* Instalace gcc
  - aktualní verze 6.3.0 (ověření příkazem `gcc -v`)
---  
**17.9.**
* Instalace OpenCV
  - instalace závislostí
  - *momentálně si nejsem jistý, jestli budu používat jen c++ nebo taky python, proto raději nainstaluju i python knihovny*
  - z GitHubu stáhnu OpenCV a OpenCV_contrib
  - *OpenCV_contrib je určeno k vývoji takzvaných "extra" modulů, které přispívají k funkčnosti. Nové moduly často nemají stabilní API a nejsou dobře testovány. Proto by neměli být uvolňovány jako součást oficiální distribuce OpenCV, protože se knihovna snaží udržovat dostatečný výkon, stabilitu a kompatibilitu.*
  - spuštění CMake
  - *CMake se používá ke kontrole procesu kompilace softwaru pomocí jednoduchých konfiguračních souborů nezávislých na platformě a kompilátoru a vytváření nativních makefile a pracovních prostorů, které lze použít v prostředí kompilátoru podle vašeho výběru.*
* Ověření funkčnosti OpenCV pomocí programu "displayImg.cpp"
    ```
    Mat img;    //objekt, ve kterém bude obrázek uložený
    img = imread(argv[1], CV_LOAD_IMAGE_COLOR);     //funkce "iamread" načte soubor
    namedWindow("Zobrazeny obrazek", WINDOW_AUTOSIZE);    //vytvoří okno pojmenované podle argumentu
    imshow("Zobrazeny obrazek", img);     //zobrazí obrázek uvnitř zvoleného okna  
    ```
    - *program kompiluju pomocí  g++ -std=c++11 nazevProgramu.cpp `pkg-config --libs --cflags opencv` -o nazevProgramu*
---    
## Zajímavé odkazy 
https://www.youtube.com/watch?v=4UTSEKzsSvM (Videotutorial k editaci souboru README)

https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91 (Instalace gcc)

http://www.learnopencv.com/install-opencv3-on-ubuntu/ (Instalace OpenCV na Ubuntu)
