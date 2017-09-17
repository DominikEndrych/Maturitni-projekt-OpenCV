#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
Mat img; //objekt, ve kterém bude obrázek uložený
img = imread(argv[1], CV_LOAD_IMAGE_COLOR); //funkce "iamread" načte soubor
namedWindow("Zobrazeny obrazek", WINDOW_AUTOSIZE); //vytvoří okno pojmenované podle argumentu
imshow("Zobrazeny obrazek", img); //zobrazí obrázek uvnitř zvoleného okna
waitKey(0); //okno nezmizí dokud nevyprší daný čas; 0=nekonečno, nezmizí dokud uživatel nezmáčkne
return 0;
}
