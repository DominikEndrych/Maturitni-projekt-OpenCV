#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
	VideoCapture cap("wildlife.wmv"); //otevře zvolené video
	if(!cap.isOpened()) //jestli se video neotevře, program se ukončí
	{
		cout<<"Video se nepodarilo otevrit"<<endl;
		return -1;
	}
	while(1)
	{
		Mat frame;
		cap >> frame; //postupně zachycuje snímky
		if(frame.empty()) //jsetli je snímek prázdný,hned break
			break;
		imshow("Prehravane video", frame); //zobrazí aktualní snímek
		char c=(char)waitKey(25);
		if(c==27)	//po zmáčknutí "escape" se video ukončí
			break;
	}
	cap.release(); //když všechno skončí, objekt se uvolní
	destroyAllWindows(); //zavře všechny snímky

	return 0;
}
